from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.homepage),
    # url(r'^pass/', include('django.contrib.auth.urls')),
    path('event/<int:event_id>', views.event_detail, name='Event_Detail'),
    path('event/<str:event_id>', views.event_detail, name='Event_Detail'),
    path('message/',views.message),
    path('gallery/<int:id>/', views.gallerypagecat),
    path('sponsgallery/<int:id>/', views.sponsgallerypagecat),
    path('hc_sponsorship/', views.spons_hc_view),
    path('gallery/', views.gallerypage),
    path('startups/', TemplateView.as_view(template_name='website/startups.html')),
    path('terms/', views.terms_page),
    path('privacy_policy/', views.privacy_policy_page),
    path('applogin/',views.applogin, name='applogin'),
    path('loginweb/',views.weblogin, name='loginweb'),
    path('new_conno/',views.new_conno,name='new_conno'),
    #url(r'^send_otp/',views.send_otp),
    url(r'^retry_otp',views.retry_otp),
    path('verify_otp/',views.verify_otp),
    path('web_verify_otp/',views.web_verify_otp),
    path('appregister/', views.appregister, name='appregister'),
    path('register/', views.webregister, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
    path('resend_otp/', views.resend_otp, name='resend_otp'),

    path('forget_password_send_otp/', views.forget_password_send_otp),
    path('forget_password_verify_otp/', views.forget_password_verify_otp),

    path('gallery_api/', views.gallery_view, name='gallery_api'),
    path('sponsgallery_api/', views.spons_gallery_view, name='sponsgallery_api'),
    
    #Below Routes are for CA Portal
    path('request_approval/', views.request_approval, name='request_approval'),
    path('request_list/', views.user_request_list, name='request_list'),
    
    path('request_approved/', views.approved_status, name='approved_requests'),
    path('request_rejected/', views.rejected_status, name='rejected_requests'),
    path('request_pending/', views.pending_status, name='pending_requests'),
    
    path('request_confirm/<int:id>/', views.confirm_approval, name='confirm_approval'),
    path('approve_request/<int:userid>/<int:id>/',views.approve_request, name='approve_request'),
    path('decline_request/<int:userid>/<int:id>/',views.decline_request, name='decline_request'),
    path('leaderboard/',views.leaderboard, name='leaderboard'),

    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_rest_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    #url(r'^dashboard/',views.dashboard),
]