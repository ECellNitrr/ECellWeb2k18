from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Profile,CA_Requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UserForm, UserProfileInfoForm, ContactForm, RequestApprovalForm
from django import forms
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm
from django.forms.models import model_to_dict
import jwt
import json
import http.client
from sendotp import sendotp
from server.decorators.login import login_req
from server.decorators.decoder import decoder
from decouple import config
from django.conf import settings as conf_settings
from social_django.models import UserSocialAuth
from .models import WebMsg
import multiprocessing
from . import send_mail
from random import randint
import requests

def event_detail(request, event_id):
	if (event_id == 'ignition'):
		event_id = 7
	return render(request, 'website/event_detail.html')

def homepage(request):
	return render(request, 'website/index.html')

def gallerypage(request):
	return render(request, 'website/gallery.html')

def privacy_policy_page(request):
	return render(request, 'website/privacy_policy.html')

def terms_page(request):
	return render(request, 'website/terms.html')

@csrf_exempt
def message(request):
	post = json.loads(request.body.decode('UTF-8'))
	msg = WebMsg(name=post['name'],email=post['email'],msg=post['msg'])
	print(post)
	msg.save()

	return JsonResponse({'success':True,'message':'Your response has been recorded successfully'})

@csrf_exempt
def applogin(request, *args, **kwargs):
	error_msg = {}
	error_msg['success'] = False

	if request.method=='POST':
		req_data = json.loads(request.body.decode('UTF-8'))
		email = req_data['email']
		password = req_data['password']

		try:
			obj = User.objects.filter(email=email)
			username = obj[0].username
			print(username)
			user = authenticate(username=username, password=password)
			print(user)
		except User.DoesNotExist:
			error_msg['message'] = "Please create an account to continue"
			return JsonResponse(error_msg)
		except Exception as e:
			print(e)
			error_msg['message'] = "Please try again later"
			return JsonResponse(error_msg)
		
		if user:
			user.profile.status=1
			login(request,user)
			payload = {
				'id' : user.id,
				'email': user.email,
			}

			jwt_token = jwt.encode(payload,conf_settings.SECRET_KEY)
			token = jwt_token.decode('utf-8')
			return JsonResponse({
				'success' : True,
				'message' : 'authentication successfull',
				'first_name' : user.first_name,
				'last_name' : user.last_name,
				'token' : token
			})

		else:
			print("Invalid credentials")
			error_msg['message'] = "Invalid Credentials"
			return JsonResponse(error_msg)
	return render(request,'login.html')

@csrf_exempt
def appregister(request):

	if request.method == "POST":
		req_data = request.body.decode('UTF-8')
		req_data = json.loads(req_data)
		email = req_data['email']
		password = req_data['password']
		contact_no = str(req_data['contact_no'])
		#Checking Duplicate records of Email or contact no
		conno = req_data['contact_no']
		if(Profile.objects.filter(contact_no=conno).exists()):
			return JsonResponse({
				'success':False,
				'message':'Contact No. must be unique',
			})
		print('First check')
		checkemail = req_data['email']
		if(User.objects.filter(email=checkemail).exists()):
			return JsonResponse({
				'success':False,
				'message':'email must be unique',
			})

		print('Second check')
		#Saving Data in Variables
		first = req_data['first_name']
		last = req_data['last_name']
		user = User.objects.create_user(
			username=first+last+'xx'+conno,
			first_name=first,
			last_name=last,
			email=email,
			password=password,
			is_active=False
			)

		user.save()

		user.profile.contact_no = req_data['contact_no']
		user.profile.status=0
	
		otp = str(randint(1000,9999))
		url = "http://www.merasandesh.com/api/sendsms"
		message = "Your OTP for E-Cell NIT Raipur APP is "+otp+""
		querystring = {"username":config('MSG_USERNAME'),"password":config('MSG_PASSWORD'),"senderid":"SUMMIT","message": message ,"numbers": contact_no,"unicode":"0"}

		response = requests.request("GET", url, params=querystring)

		print(response.text)
		user.profile.otp = otp
		user.profile.save()
		print(otp)
		payload = {
			'id' : user.id,
			'email': user.email,
		}
		jwt_token = jwt.encode(payload,conf_settings.SECRET_KEY)
		token = jwt_token.decode('utf-8')
		# print(token)
		return JsonResponse({
			'success' : True,
			'message' : 'Registration successfull',
			'token' : token
		})
	else:
		return JsonResponse({
				'success' :False,
				'message' : 'form method error',
			})

@csrf_exempt
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.profile.status=1
		user.is_active = True
		user.save()
		return JsonResponse({'success':True,'message':'Account Activated Successfully'})
	else:
		return JsonResponse({'success':False,'message':'Activation link is invalid!'})


@csrf_exempt
def weblogin(request):
	response = {}
	if request.method == 'POST':
		req_data = json.loads(request.body.decode('UTF-8'))
		email = req_data['email']
		password = req_data['password']
		print(email,password)
		try:
			user = User.objects.get(email=email)
			username = user.username
			print(username)
			user = authenticate(username=username, password=password)
			login(request,user, backend='django.contrib.auth.backends.ModelBackend')
			profile = user.profile
			status = profile.status
			request.session['username'] = username
			response['success'] = True
			response['message']	= 'Authentication Successfull'
			response['status'] = status
			response['first_name'] = user.first_name
			response['last_name'] = user.last_name
		except User.DoesNotExist:
			print("User Doesn't Exist")
			response['success'] = False
			response['message'] = "Please create an account to login"
		except Exception as e:
			print(e)
			response['success'] = False
			response['message'] = "Invalid Credentials"
	else:
		response['success']=False
		response['message']="Please Try Again"
	
	return JsonResponse(response)


@csrf_exempt
def webregister(request):

	if request.method == 'POST':
		req_data = json.loads(request.body.decode('UTF-8'))
		email = req_data['email']
		password = req_data['password']

		if User.objects.filter(email=email).exists():
			return JsonResponse({'success':False,'message':'Email already exists'})
		else:
			user = User()
			user.username = email
			user.email = email
			user.set_password(password)
			user.is_active = True
			user.first_name = req_data['first_name']
			user.last_name = req_data['last_name']
			user.save()
			contact_no = req_data['contact_no']
			user.profile.contact_no = contact_no
			otp = str(randint(1000,9999))
			url = "http://www.merasandesh.com/api/sendsms"
			message = "Your OTP for E-Cell NIT Raipur Website registeration is "+otp+""
			querystring = {"username":config('MSG_USERNAME'),"password":config('MSG_PASSWORD'),"senderid":"SUMMIT","message": message ,"numbers": contact_no,"unicode":"0"}

			response = requests.request("GET", url, params=querystring)
			print(otp)
			print(response.text)
			user.profile.otp = otp
			user.profile.status = False
			user.profile.save()




			return JsonResponse({
				'success' : True,
				'message' : 'registration successfull'
			})
	else:
		return JsonResponse({
		'success' :False,
		'message' : 'form method error',
		})


def logout_view(request):
	logout(request)
	return JsonResponse({'success':True,
						 'message':'User logged out successsfully'})

@csrf_exempt
def retry_otp(request):
	response = {}
	if request.method == "POST":
		req_data = request.body.decode('UTF-8')
		req_data = json.loads(req_data)
		email = req_data['email']
		contact_no = str(req_data['contact_no'])
		if User.objects.filter(email=email).exists():
			user = User.objects.get(email=email)
			otp = str(randint(1000,9999))
			url = "http://www.merasandesh.com/api/sendsms"
			message = "Your OTP for E-Cell NIT Raipur APP is "+otp+""
			querystring = {"username":config('MSG_USERNAME'),"password":config('MSG_PASSWORD'),"senderid":"SUMMIT","message": message ,"numbers": contact_no,"unicode":"0"}

			response_otp = requests.request("GET", url, params=querystring)

			print(response_otp.text)
			user.profile.otp = otp
			user.profile.save()
			print(otp)
			payload = {
				'id' : user.id,
				'email': user.email,
			}

			jwt_token = jwt.encode(payload,conf_settings.SECRET_KEY)
			token = jwt_token.decode('utf-8')
			response['success'] = True
			response['message'] = "OTP resent"
			response['token'] = token
		else:
			response['success'] = False
			response['message'] = "Please try to sign up after few minutes"
	else:
		response['success'] = False
		response['message'] = "Method not allowed"
	return JsonResponse(response)

@csrf_exempt
@login_required
def web_verify_otp(request):
	print("OTP verification requested")
	if request.method == 'POST':
		
		req_data = json.loads(request.body.decode('UTF-8'))
		otp = req_data['otp']
		current_user = request.user
		print(current_user)
		profile = Profile.objects.get(user=current_user)
		contact_no = profile.contact_no
		contact_no = str(contact_no)
		contact_no = int(contact_no)
		totp = profile.otp
		totp = str(totp)
		if(totp == otp):
			profile = Profile.objects.get(user=current_user)
			profile.contact_no = str(contact_no)
			profile.status = True
			current_user.is_active = True
			current_user.save()

			profile.save()
			print("OTP Verified")
			return JsonResponse({'success':True,'message':'OTP verified successfully'})
		else:
			print("OTP not verified")
			return JsonResponse({'success':False,'message':'OTP verification failed'})
	else:
		return JsonResponse({
		'success' :False,
		'message' : 'form method error',
		})


@csrf_exempt
@login_required
def new_conno(request):
	if request.method == 'POST':
		req_data = json.loads(request.body.decode('UTF-8'))
		contact_no = req_data['contact_no']
		current_user = request.user
		print(current_user)
		profile = Profile.objects.get(user=current_user)
	
		otp = str(randint(1000,9999))
		url = "http://www.merasandesh.com/api/sendsms"
		message = "Your OTP for E-Cell NIT Raipur Website registeration is "+otp+""
		querystring = {"username":config('MSG_USERNAME'),"password":config('MSG_PASSWORD'),"senderid":"SUMMIT","message": message ,"numbers": contact_no,"unicode":"0"}

		response = requests.request("GET", url, params=querystring)
		print(otp)
		print(response.text)
		profile.contact_no = contact_no
		profile.otp = otp
		profile.status = False
		profile.save()


		return JsonResponse({
			'success' : True,
			'message' : 'otp sent successfully'
		})
	else:
		return JsonResponse({
		'success' :False,
		'message' : 'form method error',
		})


@csrf_exempt
@login_required
def resend_otp(request):
	user = request.user
	profile = user.profile
	print(profile.get_time_diff())
	time = profile.get_time_diff()
	contact_no = profile.contact_no
	if time <= 150:
		otp = profile.otp
		url = "http://www.merasandesh.com/api/sendsms"
		message = "Your OTP for E-Cell NIT Raipur Website registeration is "+otp+""
		querystring = {"username":config('MSG_USERNAME'),"password":config('MSG_PASSWORD'),"senderid":"SUMMIT","message": message ,"numbers": contact_no,"unicode":"0"}
		
		response = requests.request("GET", url, params=querystring)
		profile.save()
		print(otp)
		print(response.text)
	else:
		otp = str(randint(1000,9999))
		url = "http://www.merasandesh.com/api/sendsms"
		message = "Your OTP for E-Cell NIT Raipur Website registeration is "+otp+""
		querystring = {"username":config('MSG_USERNAME'),"password":config('MSG_PASSWORD'),"senderid":"SUMMIT","message": message ,"numbers": contact_no,"unicode":"0"}

		response = requests.request("GET", url, params=querystring)
		profile.save()
		print(otp)
		print(response.text)

	return JsonResponse({
		'success' :True,
		'message' : 'OTP sent successfully',
		})




			

@csrf_exempt
@decoder
def verify_otp(request, *args, **kwargs):
	print("OTP verification requested")
	current_userid = kwargs['user_id']
	current_user = User.objects.get(id=current_userid)
	profile = Profile.objects.get(user=current_user)
	contact_no = profile.contact_no
	contact_no = str(contact_no)
	contact_no = int(contact_no)
	totp = profile.otp
	totp = str(totp)
	print("API call successful")
	if request.method == 'POST':
		req_data = json.loads(request.body.decode('UTF-8'))
		otp = req_data['otp']
		if(totp == otp):
			profile = Profile.objects.get(user=current_user)
			profile.contact_no = str(contact_no)
			profile.status = True
			current_user.is_active = True
			current_user.save()

			profile.save()
			print("OTP Verified")
			return JsonResponse({'success':True,'message':'OTP verified successfully'})
		else:
			print("OTP not verified")
			return JsonResponse({'success':False,'message':'Invalid OTP'})
	print("Method not valid")
	return JsonResponse({'success':False,'message':'Invalid method'})

def social_settings(request):
	user = request.user
	try:
		facebook_login = user.social_auth.get(provider='facebook')
		payload = {
					'id' : facebook_login.extra_data.id,
					'email': user.username,
				}

		jwt_token = jwt.encode(payload,conf_settings.SECRET_KEY)
		token = jwt_token.decode('utf-8')
		return JsonResponse({
			'success' : True,
			'message' : 'authentication successfull',
			'token' : token
		})

	except:
		facebook_login = None
		return JsonResponse({
			'success' : False,
			'message' : 'authentication failed',

		})


@login_req
def password(request):
	if request.user.has_usable_password():
		PasswordForm = PasswordChangeForm
	else:
		PasswordForm = AdminPasswordChangeForm

	if request.method == 'POST':
		form = PasswordForm(request.user, request.POST)
		if form.is_valid():
			form.save()	
			update_session_auth_hash(request,'Your password was succesfully updated!')
			return redirect('password')

		else:
			messages.error(request,'Please correct the error below.')
	else:
		form = PasswordForm(request.user)
	return render(request,'password.html',{'form':form,})

@csrf_exempt
def request_approval(request):
	if request.user.profile.user_type == 'CA':
		if request.method == 'POST':
			form = RequestApprovalForm(request.POST, request.FILES)
			if form.is_valid():
				obj = form.save()
				obj.user = request.user.profile
				obj.save()
		profile = request.user.profile
		try:
			total_requests = profile.requests.all().count()
			accepted_requests = profile.requests.filter(status_flag=1).count()
			rejected_requests = profile.requests.filter(status_flag=-1).count()
			pending_requests = profile.requests.filter(status_flag=0).count()
		except:
			total_requests = 0
			accepted_requests = 0
			rejected_requests = 0
			pending_requests = 0

		return render(request, 'base_portal.html',context={
			't_req':total_requests,
			'a_req':accepted_requests,
			'r_req':rejected_requests,
			'p_req':pending_requests,
			})
	else:
		return redirect('loginweb')

@csrf_exempt
def confirm_approval(request):
	if request.user.profile.user_type in ['EXE','MNG','OC','HC']:
		ca_requests = CA_Requests.objects.filter(status_flag=0)
		return render(request, 'request_confirm.html', {'ca_requests': ca_requests})
	else:
		return redirect('loginweb')

@csrf_exempt
def approve_request(request,id):
	if request.user.profile.user_type in ['EXE','MNG','OC','HC']:
		ss = get_object_or_404(CA_Requests, id=id)   
		ss.status_flag = 1
		if ss.social_platform == 'FB':
			ss.user.ca_fb_score +=5
		elif ss.social_platform == 'LI':
			ss.user.ca_li_score +=5
		elif ss.social_platform == 'TW':
			ss.user.ca_tw_score +=5
		else:
			ss.user.ca_wp_score +=5
		ss.save()
		return redirect('confirm_approval')
	else:
		return redirect('loginweb')

@csrf_exempt
def decline_request(request,id):
	if request.user.profile.user_type in ['EXE','MNG','OC','HC']:
		ss = get_object_or_404(CA_Requests, id=id)   
		ss.status_flag = -1
		ss.save()
		return redirect('confirm_approval')
	else: 
		return redirect('loginweb')