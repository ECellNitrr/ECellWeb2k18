from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Questionset,Question,Answer
from .forms import AnswerForm

@csrf_exempt
def get_quiz(request):
    questionset = Questionset.objects.all().values()
    questionset = list(questionset)

    return JsonResponse({
            'success':True,
            'Quizset':questionset
    }, safe=False)

@csrf_exempt
def view_quiz(request,id):
    quiz = Questionset.objects.get(id=id)
    quiz = model_to_dict(quiz)
    quiz['meta'] = str(quiz['meta'])
    questions = Question.objects.filter(q_set=id).values()
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
