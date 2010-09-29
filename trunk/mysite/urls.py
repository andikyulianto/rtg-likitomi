from django.conf.urls.defaults import *
from mysite.scale.views import weight, update, clamplift, undo, test, digit

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^weight/$', weight),
	(r'^weight/update/$', update),
	(r'^weight/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^clamplift/$', clamplift),
	(r'^clamplift/update/$', update),
	(r'^clamplift/undo/$', undo),
	(r'^clamplift/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	(r'^test/$', test),
	(r'^digit/$', digit),
	(r'^digit/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),

	# (r'^another-time-page/$', current_datetime),

    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
