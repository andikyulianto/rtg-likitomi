from django.conf.urls.defaults import *
from mysite.weight.views import index
from mysite.weight.scale_views import scale
from mysite.weight.clamplift_views import clamplift, update, undo, changeloc, minclamp, minupdate, minundo, minchangeloc
from mysite.weight.plan_views import plan, wholeplan
from mysite.weight.now import now
from mysite.weight.showplan import showplan, showreq, reqhead, required, showdet, dethead, detail
from mysite.weight.stock_views import stock
from mysite.weight.inventory import inventory
from mysite.weight.longtry import orient, longtry

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', index),

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

	# (r'^another-time-page/$', current_datetime),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
