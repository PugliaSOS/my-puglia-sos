from django.conf.urls import patterns, include, url
from poll import views

urlpatterns = patterns('',
    url(r'^(?P<poll>\d+)/(?P<event>\d+)/$', views.get_poll, name='poll')
)
