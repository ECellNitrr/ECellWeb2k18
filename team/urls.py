<<<<<<< HEAD
from django.conf.urls import url
from django.urls import path
=======
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
>>>>>>> 81cdb9c8421ab187806be8f969045707294e7b34
from . import views

urlpatterns = [
    path('list/',views.get_team, name='Get_Team'),
<<<<<<< HEAD
    url('website', views.team_site )
=======
    #url(r'^post/', views.post_team, name='Post_Team'),
>>>>>>> 81cdb9c8421ab187806be8f969045707294e7b34
]