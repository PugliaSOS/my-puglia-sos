from django.conf.urls import patterns, include, url
from polls import views

urlpatterns = patterns('',
    url(r'^(?P<poll>\d+)/(?P<event>\d+)/$', views.get_poll, name='poll')
)
