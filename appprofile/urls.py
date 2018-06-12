from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from . import views
urlpatterns = [
    path('login/',views.Login, name='login'),
    url(r'^send_otp/',views.send_otp),
    url(r'^retry_otp',views.retry_otp),
    url(r'^verify_otp/',views.verify_otp),
    path('register/', views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]
