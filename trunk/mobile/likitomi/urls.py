from django.conf.urls.defaults import *
from django.conf import settings
from general import login, index
from home import section
from machine import report

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^likitomi/tryout/$', index),
    (r'^likitomi/$', index),
    #(r'^likitomi/general/login/$', login),
    (r'^likitomi/home/$', section),
    (r'^likitomi/home/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #(r'likitomi/statusTracking/$',test)
    
    #(r'^likitomi/(.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
    (r'^likitomi/machine/$', report),
    (r'^likitomi/machine/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #(r'^likitomi/LST/$',work_status),
    # Example:
    # (r'^likitomi/', include('likitomi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^likitomi/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
