from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url': '/login/'},
        name='logout'),
    url(r'^signup/$', views.signup, name='signup')
)
