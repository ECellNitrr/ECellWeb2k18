from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/',views.get_event, name='Get_Event'),
    url(r'^add/', views.add_event),
    url(r'^edit/(?P<pk>[-\w]+)/$',views.edit_event),
    url(r'^(?P<pk>[-\w]+)/$',views.event_detail, name='detail'),
    url(r'^delete/(?P<pk>[-\w]+)/$',views.delete_event, name='delete'),
    

]
