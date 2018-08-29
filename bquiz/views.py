from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Questionset, Question, Answer, Option, QuestionAcknowledge, Setting
from .forms import AnswerForm
from appprofile.models import Profile
from django.conf import settings as conf_settings
from decouple import config
import random, json

@csrf_exempt
@login_req
def get_question(request, *args, **kwargs):
    response = {}
    try: 
        response['success'] = True
        # if Questionset.objects.filter(flag=True).exists() and request.GET.get('retryQuestion'):
        if Questionset.objects.filter(flag=True).exists():
            question_set = Questionset.objects.get(flag=True)
            if Question.objects.filter(flag=True, set=question_set).exists():
                user = Profile.objects.get(id = kwargs['user_id'])
                question = Question.objects.get(flag=True)
                print(request.GET['retryQuestion'])
                # if not Answer.objects.filter(user=user, question=question).exists() or request.GET['retryQuestion']:
                if not Answer.objects.filter(user=user, question=question).exists():
                # if not QuestionAcknowledge.objects.filter(user = kwargs['user_id'], question=question).exists() or request.GET.get('retryQuestion'):
                    response['message'] = Setting.objects.get(key='ON').text
                    response['isImageIncluded'] = False if question.type == 'TXT' else True
                    # scheme = 'https' if request.is_secure() else 'http'
                    # host = request.META['HTTP_HOST']
                    # response['imageUrl'] =  scheme + "://" + host + "/" + str(question.meta)
                    response['imageUrl'] =  config('HOST') + str(question.meta)
                    response['text'] = question.description
                    response['id'] = question.pk
                    response['time'] = question.time_limit
                    options = []
                    temp = Option.objects.filter(question = question)
                    for temp_option in temp:
                        option = {}
                        option['value'] = temp_option.option
                        option['key'] = temp_option.pk
                        options.append(option)
                    random.shuffle(options)
                    response['options'] = options
                    # Creating Acknowledgement
                    acknowledge = QuestionAcknowledge(user=user, question=question)
                    acknowledge.save()
                else:
                    response['success'] = False
                    response['message'] = Setting.objects.get(key='ANS').text
            else:
                response['success'] = False
                response['message'] = Setting.objects.get(key='ON').text
        else:
            response['success'] = False
            response['message'] = Setting.objects.get(key='OFF').text
    except Exception as e:
        response['success'] = False
        response['message'] = str(e)
    return JsonResponse(response)

def bquiz_status(request, *args, **kwargs):
    response = {}
    try:
        response['success'] = True
        if Questionset.objects.filter(flag=True).exists():
            response['message'] = Setting.objects.get(key='ON').text
            response['isActive'] = True
        else:
            response['isActive'] = False
            response['message'] = Setting.objects.get(key='OFF').text
    except Exception as e:
        response['success'] = False
        response['message'] = str(e)
    return JsonResponse(response)

@csrf_exempt
@login_req
def submit_answer(request, *args, **kwargs):
    response = {}
    if request.method == 'POST':
        req_data = json.loads(request.body.decode('UTF-8'))
        print(req_data)
        question_id = req_data['questionId']
        user_id = kwargs['user_id']
        question = Question.objects.get(pk=question_id)
        #------------------------------------------------------------------------------------
        right_answer = RightAnswer.objects.get(question = question_id).first()['right_option']
        #------------------------------------------------------------------------------------
        user = Profile.objects.get(pk=user_id)
        try:
            option_id = req_data['optionId']

            #LeaderBoard Changes-------------------------------------------------
            
            if option_id==right_answer :
                
                user.Profile.score = user.Profile.score+1   
            #user.Profile.cumulative_score = user.Profile.cumulative_score + score
            #--------------------------------------------------------------------

            
            option = Option.objects.get(pk=option_id)
        except Exception as e:
            print(e)
            option = Option.objects.get(option='NULL')
        if not Answer.objects.filter(user=user, question=question).exists():
            response['success'] = True
            response['message'] = Setting.objects.get(key='ANS').text
            answer = Answer(user=user, question=question, option=option)
            answer.save()
        else:
            response['success'] = False
            response['message'] = Setting.objects.get(key='ANS').text
    else:
        response['success'] = True
        response['message'] = "Invalid request"
    return JsonResponse(response)

@csrf_exempt    
@login_req
def individual_leaderboard(request, *args, **kwargs):
    user_id = kwargs['user_id']
    user = Profile.objects.get(pk=user_id)
    score = user.Profile.score
    cummulative_score = user.Profile.cummulative_score
    response = {}
    response['success'] = True
    response['dailyscore'] = score
    response['cummulativescore'] = cummulative_score
    return JsonResponse(response)

@csrf_exempt
def leaderboard(request):
    top_scores = Profile.objects.order_by('-score').values_list('score', flat=True)
    response = {}
    response['success'] = True
    response['leaders'] = top_scores
    return JsonResponse(response)


    
