from django.conf.urls import patterns, include, url
from event import views

urlpatterns = patterns('',
    url(r'^$', views.get_all, name='event_list'),
    url(r'^(?P<event>[0-9]+)/$', views.get_event, name='event'),
    url(r'^join/(?P<event>[0-9]+)/$', views.join, name='join_event')
)
