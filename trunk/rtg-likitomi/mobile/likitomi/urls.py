from django.conf.urls.defaults import *
from django.conf import settings
from general import index
from home import section,display
from detail import pcdetail
from line import startCR,endCR, startCV,endCV,startPT,endPT,startWH,endWH
from update import startUpdate,endUpdate
from machine import machine_list

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^likitomi/tryout/$', index),
    (r'^likitomi/$', index),
    (r'^likitomi/home/$', section),
    (r'^likitomi/home/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/pcdetail/$', pcdetail),
    (r'^likitomi/pcdetail/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/cr/start/$', startCR),
    (r'^likitomi/line/cr/start/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/cr/end/$', endCR),
    (r'^likitomi/line/cr/end/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/cv/start/$', startCV),
    (r'^likitomi/line/cv/start/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/cv/end/$', endCV),
    (r'^likitomi/line/cv/end/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/pt/start/$', startPT),
    (r'^likitomi/line/pt/start/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/pt/end/$', endPT),
    (r'^likitomi/line/pt/end/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/wh/start/$', startWH),
    (r'^likitomi/line/wh/start/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/wh/end/$', endWH),
    (r'^likitomi/line/wh/end/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/update/start/$', startUpdate),
    (r'^likitomi/line/update/start/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/line/update/end/$', endUpdate),
    (r'^likitomi/line/update/end/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/machine/list/$', machine_list),
    (r'^likitomi/machine/list/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/product/list/$', endUpdate),
    (r'^likitomi/product/list/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    
    #(r'^likitomi/playandtry/$', playandtry),
    #(r'^likitomi/playandtry/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^likitomi/display/$', display),
    (r'^likitomi/display/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

    # Example:
    # (r'^likitomi/', include('likitomi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^likitomi/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
)
