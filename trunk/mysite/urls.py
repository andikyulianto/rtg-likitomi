from django.conf.urls.defaults import *
from mysite.weight.views import index
from mysite.weight.scale_views import scale
from mysite.weight.clamplift_views import clamplift, update, undo, changeloc, orient
from mysite.weight.plan_views import plan
from mysite.weight.now import now
from mysite.weight.showplan import showplan
from mysite.weight.stock_views import stock
from mysite.weight.inventory import inventory
from mysite.weight.map import stockmap

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
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
#	(r'^clamplift/manual/$', manual),
	(r'^clamplift/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^orient/$', orient),
	(r'^orient/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^now/$', now),
	(r'^plan/$', plan),
	(r'^plan/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^showplan/$', showplan),
	(r'^showplan/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	(r'^stock/$', stock),
	(r'^stock/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^inventory/$', inventory),
	(r'^inventory/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^map/$', stockmap),
	(r'^map/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	# (r'^another-time-page/$', current_datetime),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
