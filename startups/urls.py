from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_startups),
    url(r'^post/', views.post_startups, name='Post_Startups')
    #path('view/<int:id>/', views.view_startup)
]
