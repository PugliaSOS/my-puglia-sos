from django.conf.urls import patterns, include, url
from event import views

urlpatterns = patterns('',
    url(r'^$', views.get_all, name='event_list'),
    url(r'^joined/$', views.get_joined, name='event_list_joined'),
    url(r'^(?P<event>\d+)/$', views.get_event, name='event'),
    url(r'^(?P<event>\d+)/join/$', views.join, name='join_event'),
    url(r'^(?P<event>\d+)/unjoin/$', views.unjoin, name='unjoin_event')
)
