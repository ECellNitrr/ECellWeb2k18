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
            response['questionsetId'] = Questionset.objects.get(flag=True).pk
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
    response = {}
    try:
        id = request.GET.get('questionsetId')
        print(id)
        # Quick fix for existing bug
        if id == -1:
            id = 4
        question_set = Questionset.objects.get(pk=id)
        if Leader.objects.filter(questionset=question_set).exists():
            user_id = kwargs['user_id']
            user = Profile.objects.get(pk=user_id)
            leaderboard = []
            temp_leaderboard = Leader.objects.filter(questionset=question_set).order_by('score').reverse()
            for idx, temp_user in enumerate(temp_leaderboard):
                leader = {}
                leader['rank'] = idx + 1
                leader['name'] = str(temp_user.profile.user.first_name + " " + temp_user.profile.user.last_name)
                leaderboard.append(leader)
                if temp_user.profile == user:
                    response['userRank'] = idx + 1
            
            if response['userRank'] is None:
                response['userRank'] = 0
            response['leaderboard'] = leaderboard[:10]
            response['success'] = True
            response['message'] = "Leaderboard has been generated"
        else:
            response['success'] = False
            response['message'] = "Please wait while we generate the leaderboard"
    except Exception as e:
        print(e)
        response['success'] = False
        response['message'] = "Please try again later"
    print(response)
    return JsonResponse(response)

@csrf_exempt
def leaderboard(request, id):
    response = {}
    response['success'] = True

    list_of_users = Leader.objects.filter(questionset__id=id).order_by('score').reverse()
    #print(list_of_users)
    leaders = []
    for user in list_of_users:
        name = str(user.profile.user.first_name)+str(user.profile.user.last_name)
        leaders.append(name)
    response['leaders']= leaders
    scores = [x.score for x in list_of_users]
    response["scores"] = scores
    return JsonResponse(response)

@csrf_exempt
def calc_score(request, id):
    response = {}
    user = User.objects.all()
    for user in user:
        ans = Answer.objects.filter(user=user.profile)
        print(ans)
        leader = Leader()
        leader.profile = user.profile
        leader.score =0
        
        for answer in ans:

            if(answer.question.set.id == id):
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

    #response[leader.profile.id] = leader.score
    response["success"]= True
    return JsonResponse(response)

@csrf_exempt
def generate_leaderboard(request, id):
    response = {}
    try:
        question_set = Questionset.objects.get(pk=id)
        questions = Question.objects.filter(set=question_set)
        for question in questions:
            right_answer_pair = RightAnswer.objects.get(question=question)
            if Answer.objects.filter(question=right_answer_pair.question, option=right_answer_pair.right_option).exists():
                right_answers = Answer.objects.filter(question=right_answer_pair.question, option=right_answer_pair.right_option)
                for right_answer in right_answers:
                    if Leader.objects.filter(profile=right_answer.user, questionset=question_set).exists():
                        temp_profile = Leader.objects.get(profile=right_answer.user, questionset=question_set)
                        temp_profile.score = temp_profile.score + question.score
                        temp_profile.save()
                    else:
                        temp_profile = Leader(questionset=question_set, profile=right_answer.user, score=question.score)
                        temp_profile.save()
            else:
                wrong_answers = Answer.objects.filter(question=right_answer_pair.question)
                for wrong_answer in wrong_answers:
                    if not Leader.objects.filter(profile=wrong_answer.user, questionset=question_set).exists():
                        temp_profile = Leader(questionset=question_set, profile=wrong_answer.user, score=0)
                        temp_profile.save()
        response['success'] = True
        response['message'] = "Leaderboard generated"
        leaderboard = []
        temp_leaderboard = Leader.objects.filter(questionset=question_set).order_by('score').reverse()
        for idx, user in enumerate(temp_leaderboard):
            leader = {}
            leader['rank'] = idx+1
            leader['name'] = str(user.profile.user.first_name + " " + user.profile.user.last_name)
            leaderboard.append(leader)
        response['leaderBoard'] = leaderboard
    except Exception as e:
        print(e)
        response['success'] = False
        response['message'] = "It's not you its us. Give us a try again. Please try again later"
    return JsonResponse(response)

"""

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
"""