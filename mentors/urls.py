from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/',views.get_mentors, name='Get_Mentors'),
    url(r'^$', views.post_mentors, name='Post_Mentors')
    #path('view/<int:id>/',views.view_mentor, name='View_Mentor'),
]
