from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Questionset, Question, Answer, Option, QuestionAcknowledge, Setting, RightAnswer,Leader
from .forms import AnswerForm
from appprofile.models import User,Profile
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
        user = Profile.objects.get(pk=user_id)
        try:
            option_id = req_data['optionId']
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
def leaderboard(request, *args, **kwargs):
    response = {}

    list_of_users = Leader.objects.all().order_by('score').reverse()
    response['success'] = True
    leaders = []
    for user in list_of_users:
        
        name = str(user.profile.user.first_name)+str(user.profile.user.last_name)
        leaders.append(name)
    # print(leaders)
    # print(list_of_users)
   
    response['leaders']= leaders
   
    for us in list_of_users:
        response[us.id] = us.score
    

    # leaderboard = Leader.objects.all().order_by('score').reverse()
    # for leader in leaderboard:
    #     response[leader.profile.id] = leader.score
   
    

    return JsonResponse(response)
    
@csrf_exempt
def calculate_score(request, *args, **kwargs):
    response = {}
    answers = Answer.objects.all()
    for answer in answers:
        right_ans = RightAnswer.objects.get(question=answer.question)
        if answer.option == right_ans.right_option :
            user = answer.user
            question = answer.question        
            points = question.score
            leader = Leader()

            leader.profile = user
            leader.questionset = answer.question.set
            leader.score = leader.score + points
            leader.save()
            user.cumulative_score = user.cumulative_score + points
            response[leader.profile.id] = leader.score
            user.save()
        else:
            leader = Leader()
            leader.profile = answer.user
            leader.questionset = answer.question.set
            leader.score = leader.score + 0
            leader.save()
            response[leader.profile.id] = leader.score


    return JsonResponse(response)
        

def calc_score(request):
    response = {}
    user = User.objects.all()
    for user in user:
        ans = Answer.objects.filter(user=user.profile)
        print(ans)
        leader = Leader()
        leader.profile = user.profile
        leader.score =0
        
        for answer in ans:

            right_ans = RightAnswer.objects.get(question=answer.question)
            if answer.option == right_ans.right_option :
                leader.questionset = answer.question.set
                question = answer.question        
                points = question.score
                
                
                leader.questionset = answer.question.set
                leader.score = leader.score + points
                leader.save()
            else:
                leader.questionset = answer.question.set
                leader.save()
    response[leader.profile.id] = leader.score
    return JsonResponse(response)