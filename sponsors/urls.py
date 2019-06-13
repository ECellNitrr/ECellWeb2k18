from django.conf.urls import url, include
from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns = [
    url(r'^list/', views.get_sponsors),
    path('<int:year>/', views.post_sponsors, name='Post_Sponsors'),
    path('yearwise/', views.post_sponsors_yearwise_list, name='sponsors_yearwise'),
    path('', RedirectView.as_view(url='/sponsors/2018/', permanent=True)),
    # url(r'^$', views.post_sponsors, name='Post_Sponsors')
    #path('create/', views.create_spons),
    #path('view/<int:id>/', views.view),
    #path('delete/<int:id>/', views.delete_spons),
    #path('edit/<int:id>/', views.edit_spons),
]
