from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('view/<int:id>/',views.view_quiz, name='View_quiz'),
    #path('view/question/<int:id>/',views.view_question, name='View_question'),
    path('get_question/', views.get_question, name="get_live_question"),
    path('is_active/', views.bquiz_status, name="get_bquiz_status"),
    path('submit_answer/', views.submit_answer, name="submit_answer"),
    path('myscore/', views.individual_leaderboard, name="myscore"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('calculate/',views.calculate_score,name="calculate"),
    #path('calc/', views.calc_score),
    path('calc/<int:id>/', views.calc_score),
]
