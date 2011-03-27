from django.conf.urls.defaults import *
from django.conf import settings
from statusTracking.general import login
from statusTracking.home import section,display
from statusTracking.detail import pcdetail
from statusTracking.line import startCR,endCR, startCV,endCV,startPT,endPT,startWH,endWH
from statusTracking.update import startUpdate,endUpdate
from statusTracking.machine import machine_list

#Weight
from weight.views import index
from weight.scale_views import scale
from weight.clamplift_views import clamplift, update, undo, changeloc, minclamp, minupdate, minundo, minchangeloc
from weight.plan_views import plan, wholeplan
from weight.now import now
from weight.showplan import showplan, showreq, reqhead, required, showdet, dethead, detail
from weight.stock_views import stock
from weight.inventory import inventory
from weight.longtry import orient, longtry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^likitomi/$', login),
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
	(r'^likitomi/display/$', display),
	(r'^likitomi/display/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^likitomi/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

	(r'^index/$', index),
	(r'^index/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^scale/$', scale),
	(r'^scale/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^clamplift/$', clamplift),
	(r'^clamplift/update/$', update),
	(r'^clamplift/update/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^clamplift/undo/$', undo),
	(r'^clamplift/changeloc/$', changeloc),
	(r'^clamplift/changeloc/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^clamplift/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^minclamp/$', minclamp),
	(r'^minclamp/update/$', minupdate),
	(r'^minclamp/update/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^minclamp/undo/$', minundo),
	(r'^minclamp/changeloc/$', minchangeloc),
	(r'^minclamp/changeloc/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^minclamp/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^now/$', now),
	(r'^plan/$', plan),
	(r'^plan/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^showplan/$', showplan),
	(r'^showplan/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^wholeplan/$', wholeplan),
	(r'^wholeplan/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^showreq/$', showreq),
	(r'^showreq/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^reqhead/$', reqhead),
	(r'^reqhead/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^required/$', required),
	(r'^required/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^showdet/$', showdet),
	(r'^showdet/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^dethead/$', dethead),
	(r'^dethead/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^detail/$', detail),
	(r'^detail/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^stock/$', stock),
	(r'^stock/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^inventory/$', inventory),
	(r'^inventory/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^orient/$', orient),
	(r'^orient/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^longtry/$', longtry),

	(r'^admin/', include(admin.site.urls)),
)