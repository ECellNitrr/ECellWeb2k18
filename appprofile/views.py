from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .forms import UserForm, UserProfileInfoForm, ContactForm
from django import forms
from django.shortcuts import render, redirect
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


def homepage(request):
    return render(request, 'website/index.html')

def gallerypage(request):
	return render(request, 'website/gallery.html')

def message(request):
	post = json.loads(request.body)
	msg = WebMsg(name=post['name'],email=post['email'],msg=post['msg'])
	print(post)
	msg.save()

	return JsonResponse({'success':True,'message':'message recieved by server'})


@csrf_exempt
def applogin(request, *args, **kwargs):

	error_msg = {
		'success' : False,
		'message' : 'Invalid credentials'
		}

	if request.method=='POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			obj = User.objects.filter(email=email)
			username = obj[0].username
		except:
			return JsonResponse(error_msg)
		try:
			user = authenticate(username=username, password=password)
		except User.DoesNotExist:
			return JsonResponse(error_msg)

		if user:
			user.is_active=True;
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
				'token' : token
			})

		else:
			return JsonResponse(error_msg)
	return render(request,'login.html')


@csrf_exempt
def appregister(request):

	registered = False
	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(request.POST,request.FILES)
		print("outside if\n\n\n\n")
		if user_form.is_valid() and profile_form.is_valid():
			print("inside if.\n.\n.\n.\n.")
			#Checking Duplicate records of Email or contact no
			conno = profile_form.cleaned_data.get('contact_no')
			if(Profile.objects.filter(contact_no=conno).exists()):
				return JsonResponse({
					'success':False,
					'message':'Contact No. must be unique',
				})
			checkemail = profile_form.cleaned_data.get('email')
			if(User.objects.filter(email=checkemail).exists()):
				return JsonResponse({
					'success':False,
					'message':'email must be unique',
				})

			#Saving Data in Variables
			first = request.POST['first_name']
			last = request.POST['last_name']
			user = user_form.save(commit=False)
			user.username = first+last+conno
			user = user_form.save()
			user.set_password(user.password)
			user.is_active=False;
			user.save()

			#User created, Creating a linked Profile of user
			user.profile.avatar = profile_form.cleaned_data.get('avatar')
			user.profile.contact_no = profile_form.cleaned_data.get('contact_no')
			user.profile.facebook = profile_form.cleaned_data.get('facebook')
			user.profile.linkedin = profile_form.cleaned_data.get('linkedin')
			user.profile.status=0
			user.profile.save()

			#Emailing the new user for confirmation Email
			current_site = get_current_site(request)
			mail_subject = "Activate your Ecell account"
			message = render_to_string('acc_active_email.html',{
				'user':user,
				'domain':current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})
			to_email = user.email
			email = EmailMessage(mail_subject,message,to=[to_email])
			email.send()


			payload = {
				'id' : user.id,
				'email': user.email,
			}

			jwt_token = jwt.encode(payload,conf_settings.SECRET_KEY)
			token = jwt_token.decode('utf-8')
			return JsonResponse({
				'success' : True,
				'message' : 'Registration successfull',
				'token' : token
			})

			#------------------

		else:
				return JsonResponse({
						'success' :False,
						'User Form Errors' : user_form.errors.as_json(),
						'Profile Form Errors' : profile_form.errors.as_json(),
						'message':'Invalid Form',
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
	error_msg = {
		'success' : False,
		'message' : 'Invalid credentials'
		}
	if request.method == 'POST':
		req_data = json.loads(request.body)
		email = req_data['email']
		password = req_data['password']
		print(email,password)

		try:
			obj = User.objects.filter(email=email)
			username = obj[0].username
		except:
			return JsonResponse(error_msg)

		user = authenticate(username=username, password=password)
		login(request,user)
		return JsonResponse({
			'success' : True,
			'message' : 'authentication successfull',

		})
	else:
		return render(request,'login.html')



@csrf_exempt
def webregister(request):

	if request.method == 'POST':
		req_data = json.loads(request.body)
		email = req_data['email']
		password = req_data['password']
		print(req_data)

		if User.objects.filter(email=email).exists():
			return JsonResponse({'success':False,'message':'Email already exists'})
		else:
			user = User()
			user.username = email
			user.email = email
			user.set_password(password)
			user.save()
			user.profile.contact_no = req_data['contactno']


			user.profile.save()

			return JsonResponse({
				'success' : True,
				'message' : 'registration successfull'
			})
	else:
		return render(request,'reg.html')


def logout_view(request):
	logout(request)
	return JsonResponse({'success':True,
						 'message':'User logged out successsfully'})




@csrf_exempt
@decoder
def send_otp(request, *args, **kwargs):


	if request.method =='POST':


		current_userid = kwargs['user_id']

		current_user = User.objects.get(id=current_userid)


		contact_no = request.POST.get('contact_no')
		contact_no = str(91)+str(contact_no)
		contact_no = int(contact_no)

		Atkey = config('Atkey')

		Msg = 'Your otp is {{otp}}. Respond with otp. Regards Team Ecell'
		otpobj =  sendotp.sendotp(Atkey,Msg)
		otp = otpobj.generateOtp()
		otp = int(otp)

		otpobj.send(contact_no,'ECelll',otp)
		#Don't change the name 'ECelll' in above line

		otps = otpobj.send(contact_no,'ECelll',otp)
		#Don't change the name 'ECelll' in above line


		contact_no = str(contact_no)

		otps = str(otps)


		profile = Profile.objects.get(user=current_user)
		profile.contact_no = contact_no
		profile.otp = otps
		profile.save()

		return JsonResponse({'success':True,'msg':'OTP sent successfully',})
	else:
		return render(request,'phone.html')


	return render(request,'phone.html')

@csrf_exempt
@login_req
def retry_otp(request, *args, **kwargs):
	current_userid = kwargs['user_id']

	current_user = User.objects.get(id=current_userid)


	profile = Profile.objects.get(user= current_user)
	contact_no = profile.contact_no
	contact_no = str(contact_no)
	contact_no = contact_no[0:12]
	contact_no = int(contact_no)

	Atkey = config('Atkey')

	Msg = 'Your otp is {{otp}}.'
	otpobj =  sendotp.sendotp(Atkey,Msg)


	otpobj.retry(contact_no,'ECelll')
	#Don't change the name 'ECelll' in above line

	return JsonResponse({'success':True,'msg':'OTP sent through call'})

@csrf_exempt
@decoder
def verify_otp(request, *args, **kwargs):

	current_userid = kwargs['user_id']
	current_user = User.objects.get(id=current_userid)
	profile = Profile.objects.get(user=current_user)
	contact_no = profile.contact_no
	contact_no = str(contact_no)
	contact_no = int(contact_no)
	totp = profile.otp
	totp = str(totp)

	if request.method == 'POST':

		otp = request.POST.get('otp')
		if(totp == otp):

			profile = Profile.objects.get(user=current_user)
			profile.contact_no = str(contact_no)
			profile.status = True
			profile.save()
			return JsonResponse({'success':True,'msg':'OTP verified successfully'})
		else:

			return JsonResponse({'success':False,'msg':'Invalid OTP'})



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






##########Event Registration ###############################

from django.contrib.auth.decorators import login_required
from events.models import Event, EventOrder, Cart


@csrf_exempt
@login_required
def add_to_cart(request, event_id):

	try:
		event = Event.objects.get(pk=event_id)
		print(event)

	except event.DoesNotExist:
		pass
	else:
		try:
			cart = Cart.objects.get(user=request.user, active=True)
			cart.add_to_cart(event_id)
		except :
			cart = Cart.objects.create(
			user= request.user
			)
			cart.save()
			cart.add_to_cart(event_id)

	return JsonResponse({'success':True,
						 'message':"Event added successfully"})


#Remove Event Function
@csrf_exempt
@login_required
def remove_from_cart(request, event_id):
	try:
		event = Event.objects.get(pk=event_id)
		print(request.user)
	except :
		pass
	else:
		cart=Cart.objects.get(user=request.user, active=True)
		print(cart)
		cart.remove_from_cart(event_id)

	return bag(request)


#View Cart/Event List Function
@csrf_exempt
@login_required
def bag(request):

	eventlist=[]

	cart= Cart.objects.filter(user=request.user, active=True)
	gre = list(EventOrder.objects.filter(cart=cart[0]))

	i=0

	for eve in gre:
		if eve.event.name not in eventlist:
			eventlist.append(eve.event.name)
		i=i+1

	context={
		'success':True,
		'message':'Event List Fetched Succesfully',
		'events':eventlist,

	}
	return JsonResponse(context)
