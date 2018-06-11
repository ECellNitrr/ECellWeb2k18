from django.conf.urls import url, include
from django.urls import path
from . import views
urlpatterns = [
    url(r'^list/', views.get_sponsors),
    #path('create/', views.create_spons),
    #path('view/<int:id>/', views.view),
    #path('delete/<int:id>/', views.delete_spons),
    #path('edit/<int:id>/', views.edit_spons),
]
