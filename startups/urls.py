from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_startups),
    #path('view/<int:id>/', views.view_startup)
]
