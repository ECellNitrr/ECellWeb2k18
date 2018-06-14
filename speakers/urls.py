from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.get_speakers),
    #path('view/<int:id>/', views.view_speaker)
]
