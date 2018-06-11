from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/',views.get_mentors, name='Get_Mentors'),
    #path('view/<int:id>/',views.view_mentor, name='View_Mentor'),
]
