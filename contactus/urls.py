from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.get_messages),
    path('view/<int:id>/', views.view_message)
    #"""path('create/', views.create_message),
    #path('update/<int:id>/', views.edit_message),
    #path('delete/<int:id>/', views.delete_message)"""
]
