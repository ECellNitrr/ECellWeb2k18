from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.get_team, name='Get_Team'),
    url(r'^$', views.team_site )
]
