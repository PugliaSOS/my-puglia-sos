from django.conf.urls import patterns, include, url
from social import views

urlpatterns = patterns('',
    url(r'^$', views.get_registered, name='all_registered'),
)
