from django.conf.urls import patterns, include, url
from event import views

urlpatterns = patterns('',
    url(r'^$', views.get_registred, name='all_registred'),
)
