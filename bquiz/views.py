from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Questionset, Question, Answer, Option, QuestionAcknowledge
from .forms import AnswerForm
from appprofile.models import Profile
import random

@csrf_exempt
def get_quiz(request):
    questionset = Questionset.objects.all().values()
    #questionset = model_to_dict(questionset)
    #questionset['meta'] = str(questionset['meta'])
    #quiz = Questionset.objects.all().values()
    #quiz = model_to_dict(quiz)
    #questionset['question'] = ['dsdsd','asasa']
    questionset = list(questionset)
    length = len(questionset)
    for i in range(length):
        idy = questionset[i]['id']
        quiz = Question.objects.filter(set=idy).values()
        quiz = list(quiz)
        questionset[i]['questions'] = quiz
    
    return JsonResponse({
            'success':True,
            'Quizset':questionset
    }, safe=False)

@csrf_exempt
def view_quiz(request,id):
    quiz = Questionset.objects.get(id=id)
    quiz = model_to_dict(quiz)
    quiz['meta'] = str(quiz['meta'])

##-------------##

##-----------##
    
    questions = Question.objects.filter(q_set=id).values()
    #print(questions)
    #print(id)
    #print('HE')

    questions = list(questions)
    return JsonResponse({
        'success':True,
        'quiz':quiz,
        'questions':questions
    },safe=False)

@csrf_exempt
@login_req
def view_question(request,id,**kwargs):
    answer = Answer.objects.get(question_id=id,user_id=kwargs['user_id'])
    question = Question.objects.filter(id=id).first()
    question = model_to_dict(question)
    answer = model_to_dict(answer)
    question['meta'] = str(question['meta'])
    return JsonResponse({
        'success':True,
        'question': question,
        'answer' : answer
    })

@csrf_exempt
@login_req
def submit_ans(request,id,**kwargs):
    if request.method == 'POST':
        ans = Answer.objects.filter(user_id=kwargs['user_id'],question_id=id).count()
        if(ans!=0):
            answ = Answer.objects.filter(user_id=kwargs['user_id'],question_id=id).first()
            answer_form = AnswerForm(request.POST, instance=answ)
        else:
            answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.user_id_id = kwargs['user_id']
            answer.question_id_id = id
            answer.save()
            answer = model_to_dict(answer)
            return JsonResponse({
                'success':True,
                'answer':answer
            })
        else:
            return JsonResponse({
                'success':False,
                'message':'Form Invalid'
            })

    else:
        return JsonResponse({
            'success':False,
            'message':'method error'
        })

@csrf_exempt
# @login_req
def get_question(request, *args, **kwargs):
    response = {}
    response['success'] = True
    if Question.objects.filter(flag=True).exists():
        question = Question.objects.get(flag=True)
        response['message'] = "B-Quiz is live"
        response['isImageIncluded'] = False if question.type == 'TXT' else True
        scheme = 'https' if request.is_secure() else 'http'
        host = request.META['HTTP_HOST']
        response['imageUrl'] =  scheme + "://" + host + "/" + str(question.meta)
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
        try:
            user = Profile.objects.get(id = kwargs['user_id'])
            # Creating Acknowledgement
            acknowledge = QuestionAcknowledge(user=user, question=question)
            acknowledge.save()
        except Exception as e:
            print(str(e))
    else:
        response['message'] = "B-Quiz is not live please wait for the next update"
    return JsonResponse(response)