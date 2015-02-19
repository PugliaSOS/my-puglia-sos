from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url': '/login/'},
        name='logout'),
    url(r'^password_change/$', auth_views.password_change,
        {
            'template_name': 'main/password.html',
            'post_change_redirect': '/'
        }, name='password_change'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^change_profile/$', views.change_profile, name='change_profile'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^status/$', views.status, name='status')
)
