from django.conf.urls.defaults import *
from mysite.weight.views import index
from mysite.weight.scale_views import scale
from mysite.weight.clamplift_views import clamplift, update, undo, changeloc

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

	# (r'^another-time-page/$', current_datetime),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
