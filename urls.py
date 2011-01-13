from django.conf.urls.defaults import *

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    url(regex=r'^$',
        view='core.views.index',
        name='index'),
    url(regex=r'^login/$',
        view='django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'core/login.html'}),
    url(regex=r'^logout/$',
        view='django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/login/'}),
    url(r'^home/', include('core.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^accounts/', include('accounts.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)