from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_puglia_sos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
    url(r'^events/', include('event.urls')),
    url(r'^polls/', include('poll.urls')),
    url(r'^social/', include('social.urls')),
)
