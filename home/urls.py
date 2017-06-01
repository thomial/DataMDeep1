from django.conf.urls import url

from .forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload_file_csv, name='upload'),
    url(r'^post/(?P<id>\d+)/', views.post, name='post'),
    url(r'^delete/(?P<id>\d+)/', views.delete_post, name='delete'),
    url(r'^(?P<img_id>\d+).png$', views.chart, name='chart'),
    url(r'^login/$', auth_views.login,{'template_name':'home/login.html', 'authentication_form': LoginForm} ,name='login' ),
    url(r'^logout/$', auth_views.logout, name='logout'),
]