from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/',views.get_team, name='Get_Team'),
    #url(r'^post/', views.post_team, name='Post_Team'),
]