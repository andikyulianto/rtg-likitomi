from django.conf.urls.defaults import *
from django.conf import settings
from statusTracking.general import login
from statusTracking.home import login_check,logout_view,section,display,normalPlanRefresher,lastUpdate,monthlyPlan
from statusTracking.detail import pcdetail
from statusTracking.line import startCR,endCR, startCV,endCV,startPT,endPT,startWH,endWH
from statusTracking.update import startUpdate,endUpdate
from statusTracking.machine import machine_list
#from statusTracking.plan import totalPlan, totalPlanSelectedDate
#from statusTracking.query import queryDateNotProcess, queryDateMissing

# Weight #
from weight.scale_views import scale
from weight.views import dashboard
from weight.showplan import showplan, required, detail
from weight.inventory import inventory
from weight.minclamp import minclamp, minupdate, minundo, minchangeloc, minassigntag
from weight.maxclamp import maxclamp, maxupdate, maxundo, maxchangeloc, maxassigntag
from weight.tagman import tagman, showtaglist, createnew, assigntag, writemore, loctag
from weight.longtry import orient, longtry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#	(r'^login/$', login),
	(r'^likitomi/$', 'statusTracking.views.login_user'),
	(r'^likitomi/auth/$', login_check),
	(r'^likitomi/auth/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^likitomi/logout/$', logout_view),
	(r'^likitomi/logout/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^likitomi/home/$', section),		
	(r'^likitomi/home/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
        (r'^likitomi/normalPlanRefresher/$', normalPlanRefresher),      
        (r'^likitomi/normalPlanRefresher/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
        (r'^likitomi/lastUpdate/$', lastUpdate),        
        (r'^likitomi/lastUpdate/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
        (r'^likitomi/monthlyPlan/$', monthlyPlan),      
        (r'^likitomi/monthlyPlan/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^likitomi/pcdetail/$', pcdetail),
	(r'^likitomi/pcdetail/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

#	(r'^likitomi/query/date/notprocess/$', queryDateNotProcess),
#	(r'^likitomi/query/date/notprocess/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
##	(r'^likitomi/query/date/missing/$', queryDateMissing),
#	(r'^likitomi/query/date/missing/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
##	(r'^likitomi/plan/plan/$', totalPlan),
#	(r'^likitomi/plan/plan/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
##	(r'^likitomi/plan/totalPlan/$', totalPlanSelectedDate),
#	(r'^likitomi/plan/totalPlan/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
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

# Weight #
	(r'^scale/$', scale),
	(r'^scale/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

	(r'^dashboard/$', dashboard),
	(r'^dashboard/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

	(r'^showplan/$', showplan),
	(r'^showplan/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^required/$', required),
	(r'^required/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^detail/$', detail),
	(r'^detail/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

	(r'^minclamp/$', minclamp),
	(r'^minclamp/update/$', minupdate),
	(r'^minclamp/undo/$', minundo),
	(r'^minclamp/changeloc/$', minchangeloc),
	(r'^minclamp/changeloc/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^minclamp/assigntag/$', minassigntag),
	(r'^minclamp/assigntag/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^minclamp/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^maxclamp/$', maxclamp),
	(r'^maxclamp/update/$', maxupdate),
	(r'^maxclamp/undo/$', maxundo),
	(r'^maxclamp/changeloc/$', maxchangeloc),
	(r'^maxclamp/changeloc/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^maxclamp/assigntag/$', maxassigntag),
	(r'^maxclamp/assigntag/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^maxclamp/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

	(r'^inventory/$', inventory),
	(r'^inventory/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

	(r'^tagman/$', tagman),
	(r'^tagman/createnew/$', createnew),
	(r'^tagman/createnew/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^tagman/loctag/$', loctag),
	(r'^tagman/loctag/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^tagman/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^showtaglist/$', showtaglist),
	(r'^showtaglist/assigntag/$', assigntag),
	(r'^showtaglist/assigntag/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^showtaglist/writemore/$', writemore),
	(r'^showtaglist/writemore/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^showtaglist/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),

#	(r'^orient/$', orient),
#	(r'^orient/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
	(r'^longtry/$', longtry),

	(r'^admin/', include(admin.site.urls)),
)
