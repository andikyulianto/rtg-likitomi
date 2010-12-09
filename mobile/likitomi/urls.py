from django.conf.urls.defaults import *
from django.conf import settings
from general import login, index
from home import section
from newHome import allSection
from machine import report
from product import view
from line import start

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^likitomi/tryout/$', index),
    (r'^likitomi/$', index),
    #(r'^likitomi/general/login/$', login),
    (r'^likitomi/home/$', section),
    (r'^likitomi/home/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/newHome/$', allSection),
    (r'^likitomi/newHome/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/$', start),
    (r'^likitomi/line/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    #(r'^likitomi/home/cr/$',section),
    #(r'^likitomi/home/cv/$',section)
    #(r'^likitomi/home/pt/$',section)
    #(r'^likitomi/home/wh/$',section)
    #(r'likitomi/statusTracking/$',test)
    #(r'^likitomi/(.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    
    
	(r'^likitomi/product/$', view),
	(r'^likitomi/product/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    
    
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
