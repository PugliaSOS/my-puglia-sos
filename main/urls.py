from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^$', auth_views.login, {'template_name': 'main/login.html'})
)
