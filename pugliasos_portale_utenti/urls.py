from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pugliasos_portale_utenti.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
    url(r'^events/', include('event.urls')),
    url(r'^polls/', include('poll.urls'))
)

if not settings.DEBUG:
    urlpatterns += patterns('', (
            r'^static/(?P<path>.*)$',
            'django.views.static.serve', {'document_root': settings.STATIC_ROOT}
        ),)
