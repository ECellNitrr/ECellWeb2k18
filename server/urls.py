"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from server import settings as sett
from django.conf.urls import url
from django.views import static as stat
from appprofile import views
from django.contrib.auth import views as auth_views
from app import views as app_views
from events import views as events_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/',views.login, name='login'),
    #path('register/', views.register, name='register'),
    url(r'^settings/$',views.social_settings, name='settings'),
    url(r'^settings/password/$',views.password, name='password'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('esummit/register/', events_views.register_esummit),
    path('events/', include('events.urls')),
    path('sponsors/', include('sponsors.urls')),
    path('mentors/', include('mentors.urls')),
    path('startups/', include('startups.urls')),
    path('speakers/', include('speakers.urls')),
    path('team/',include('team.urls')),
    path('bquiz/',include('bquiz.urls')),
    url(r'^is_update_available', app_views.latest_build),
    url('^', include('django.contrib.auth.urls')),
    # url(r'^password_reset/$', auth_views.password_reset),
    # url(r'^password_reset/done/$', auth_views.password_reset_done),
    # url(r'^reset/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm),
    # url(r'^reset/done/$', auth_views.password_reset_complete),
    url(r'^static/(?P<path>.*)$', stat.serve, {'document_root': settings.STATIC_ROOT}),
    path('',include('appprofile.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = settings.SITE_HEADER
