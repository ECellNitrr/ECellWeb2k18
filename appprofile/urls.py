from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.homepage),
    path('message/',views.message),
    path('applogin/',views.applogin, name='applogin'),
    path('login/',views.weblogin, name='login'),
    url(r'^send_otp/',views.send_otp),
    url(r'^retry_otp',views.retry_otp),
    url(r'^verify_otp/',views.verify_otp),
    path('appregister/', views.appregister, name='appregister'),
    path('register/', views.webregister, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]
