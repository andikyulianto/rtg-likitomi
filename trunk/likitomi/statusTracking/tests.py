"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
import unittest
from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from general import login
from models import  AuthGroup,AuthUser, StatusTracking, AuthUserGroups
import datetime

class SimpleTest(unittest.TestCase):
	def setUp(self):
		self.client = Client()
	def test_general(self):
		response = self.client.get('/likitomi/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['title'],'Welcome to Likitomi Status Tracking System')
		self.assertEqual(response.context['subcontent_header'],"Please scan or enter employee code")
		self.failUnlessEqual(response.context['subcontent_header'],"Please scan or enter employee code")
	def test_workerATPC(self):
		e = AuthUser(username='workerATPC',first_name='worker',last_name='PC',is_staff=0,is_active=1,is_superuser=0,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
		e.save()
		g = AuthGroup.objects.get(name="PC")
		gu = AuthUserGroups(user_id=e.id,group_id=g.id)
		gu.save()
		response = self.client.get('/likitomi/home/?user=workerATPC')
	#		print response.context['user']
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['user'],'workerATPC')
		self.assertEqual(response.context['page'],'PC')
	def test_workerATCV(self):
		e = AuthUser(username='workerATCV',first_name='worker',last_name='cv',is_staff=0,is_active=1,is_superuser=0,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
		e.save()
		e= AuthUser.objects.get(username='workerATCV')
	#		print e.username
		g = AuthGroup.objects.get(name="CV")
		gu = AuthUserGroups(user_id=e.id,group_id=g.id)
		gu.save()
		response = self.client.get('/likitomi/home/?user=workerATCV')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['user'],'workerATCV')
		self.assertEqual(response.context['user'],'workerATCV')
		self.assertEqual(response.context['page'],'CV')
	def test_workerATCR(self):
		e = AuthUser(username='workerATCR',first_name='worker',last_name='CR',is_staff=0,is_active=1,is_superuser=0,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
		e.save()
		g = AuthGroup.objects.get(name="CR")
		gu = AuthUserGroups(user_id=e.id,group_id=g.id)
		gu.save()
		response = self.client.get('/likitomi/home/?user=workerATCR')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['user'],'workerATCR')
		self.assertEqual(response.context['page'],'CR')
	def test_workerATPT(self):
		e = AuthUser(username='workerATPT',first_name='worker',last_name='PT',is_staff=0,is_active=1,is_superuser=0,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
		e.save()
		g = AuthGroup.objects.get(name="PT")
		gu = AuthUserGroups(user_id=e.id,group_id=g.id)
		gu.save()
		response = self.client.get('/likitomi/home/?user=workerATPT')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['user'],'workerATPT')
		self.assertEqual(response.context['page'],'PT')
	def test_workerATWH(self):
		e = AuthUser(username='workerATWH',first_name='worker',last_name='WH',is_staff=0,is_active=1,is_superuser=0,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
		e.save()
		g = AuthGroup.objects.get(name="WH")
		gu = AuthUserGroups(user_id=e.id,group_id=g.id)
		gu.save()
		response = self.client.get('/likitomi/home/?user=workerATWH')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['user'],'workerATWH')
		self.assertEqual(response.context['page'],'WH')

	#coding: utf-8
from django.test import TestCase
from django.test import Client
from django import template
from django.db.models import get_model
from models import  AuthGroup,AuthUser, StatusTracking, AuthUserGroups
import datetime
class Testmaker(TestCase):
	def setUp(self):
		self.client = Client()
		e = AuthUser(username='workerATPC',first_name='worker',last_name='PC',is_staff=0,is_active=1,is_superuser=0,last_login=datetime.datetime.now(),date_joined=datetime.datetime.now())
		e.save()
		g = AuthGroup.objects.get(name="PC")
		gu = AuthUserGroups(user_id=e.id,group_id=g.id)
		gu.save()
	def tearDown(self):
		eid = AuthUser.objects.get(username='workerATPC').id
		AuthUser.objects.filter(username='workerATPC').delete()
		AuthUserGroups.objects.get(user_id=eid).delete()

		#    fixtures = ["statusTracking_testmaker"]

	def test_likitomi_login(self):
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_pic"]), u"""thumbs/mail.png""")
		self.assertEqual(unicode(r.context["subcontent_header"]), u"""Please scan or enter employee code""")
		self.assertEqual(unicode(r.context["is_enable_arrow"]), u"""False""")
		self.assertEqual(unicode(r.context["item_name"]), u"""Item name""")
		self.assertEqual(unicode(r.context["la_user_name"]), u"""USERNAME""")
		self.assertEqual(unicode(r.context["content_header"]), u"""Login""")
		self.assertEqual(unicode(r.context["is_enable_login"]), u"""True""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""False""")
		self.assertEqual(unicode(r.context["is_enable_tributton"]), u"""False""")
		self.assertEqual(unicode(r.context["is_enable_link"]), u"""False""")
		self.assertEqual(unicode(r.context["flashMessage"]), u"""""")
		self.assertEqual(unicode(r.context["title"]), u"""Welcome to Likitomi Status Tracking System""")
		self.assertEqual(unicode(r.context["page"]), u"""login""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Welcome""")
	def test_likitomicssfal_stylecss_130760006487(self):
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomijavascriptflashjs_130760006494(self):
		r = self.client.get('/likitomi/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomihome_130760006883(self):

		r = self.client.get('/likitomi/home/', {'login': 'Login', 'user': 'workerATPC', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
		#       self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		#       self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:29.081686""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")

	def test_likitominormalplanrefresher_130760006998(self):
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:29.986100""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitomilastupdate_130760007047(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:30.484825""")
	def test_likitomipcdetail_13076000727(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""CR""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:32.726486""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")


	def test_likitomipcdetailjavascriptjqueryjs_130760007306(self):
		r = self.client.get('/likitomi/pcdetail/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailjavascriptjquery_ui_1811customminjs_130760007314(self):
		r = self.client.get('/likitomi/pcdetail/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcssfal_style2css_130760007323(self):
		r = self.client.get('/likitomi/pcdetail/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessjquery_ui_1810customcss_130760007328(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailjavascriptjqueryquicksearchjs_130760007333(self):
		r = self.client.get('/likitomi/pcdetail/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailjavascriptjquerydatatablesjs_130760007339(self):
		r = self.client.get('/likitomi/pcdetail/javascript/jquery.dataTables.js', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomilastupdate_13076000737(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:33.710415""")
	def test_likitomipcdetailcsssearch_iconpng_130760007377(self):
		r = self.client.get('/likitomi/pcdetail/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagesquitpng_130760007386(self):
		r = self.client.get('/likitomi/pcdetail/images/quit.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagescv_normalpng_130760007391(self):
		r = self.client.get('/likitomi/pcdetail/images/CV_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagespt_normalpng_130760007396(self):
		r = self.client.get('/likitomi/pcdetail/images/PT_normal.png', {})
		self.assertEqual(r.status_code, 200)	
	def test_likitomipcdetailimageswh_normalpng_130760007401(self):
		r = self.client.get('/likitomi/pcdetail/images/WH_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_icons_888888_256x240png_130760007406(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_icons_888888_256x240.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagesdjgpng_130760007413(self):
		r = self.client.get('/likitomi/pcdetail/images/djg.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_130760007418(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_130760007423(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_130760007429(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_130760007435(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_glass_75_e6e6e6_1x400.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagescr_normalpng_13076000744(self):
		r = self.client.get('/likitomi/pcdetail/images/CR_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagespc_normalpng_130760007446(self):
		r = self.client.get('/likitomi/pcdetail/images/PC_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssearch_iconpng_130760007377(self):
		r = self.client.get('/likitomi/pcdetail/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagesquitpng_130760007386(self):
		r = self.client.get('/likitomi/pcdetail/images/quit.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagescv_normalpng_130760007391(self):
		r = self.client.get('/likitomi/pcdetail/images/CV_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagespt_normalpng_130760007396(self):
		r = self.client.get('/likitomi/pcdetail/images/PT_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimageswh_normalpng_130760007401(self):
		r = self.client.get('/likitomi/pcdetail/images/WH_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_icons_888888_256x240png_130760007406(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_icons_888888_256x240.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagesdjgpng_130760007413(self):
		r = self.client.get('/likitomi/pcdetail/images/djg.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_130760007418(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_130760007423(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_130760007429(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_130760007435(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_glass_75_e6e6e6_1x400.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagescr_normalpng_13076000744(self):
		r = self.client.get('/likitomi/pcdetail/images/CR_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailimagespc_normalpng_130760007446(self):
		r = self.client.get('/likitomi/pcdetail/images/PC_normal.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetailcsssmoothnessimagesui_bg_glass_75_dadada_1x400png_130760007458(self):
		r = self.client.get('/likitomi/pcdetail/css/smoothness/images/ui_bg_glass_75_dadada_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_dadada_1x400png_130760007859(self):
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_dadada_1x400.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetail_130760009419(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:54.210875""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_130760009464(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#       self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:54.649419""")
	def test_likitomipcdetail_130760009762(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["page"]), u"""PT""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:57.647146""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760009804(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:14:58.046213""")
	def test_likitomipcdetailimagescv_blackpng_130760009812(self):
		r = self.client.get('/likitomi/pcdetail/images/CV_black.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetail_130760010124(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""WH""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:01.267739""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760010192(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:01.935450""")
	def test_likitomipcdetail_130760010568(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""CR""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:05.697315""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_13076001062(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:06.211677""")

	def test_likitomipcdetailimagescr_blackpng_130760010688(self):
		r = self.client.get('/likitomi/pcdetail/images/CR_black.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetail_130760010781(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""CR""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:07.830065""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760010827(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:08.284968""")

	def test_likitomipcdetail_130760011041(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:10.437439""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_130760011081(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:10.812250""")

	def test_likitomipcdetailimagespt_blackpng_130760011225(self):
		r = self.client.get('/likitomi/pcdetail/images/PT_black.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomipcdetail_13076001124(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
		self.assertEqual(r.status_code, 200)
		#       self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["page"]), u"""PT""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:12.422798""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760011289(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:12.902492""")
	def test_likitomipcdetailimageswh_blackpng_130760011299(self):
		r = self.client.get('/likitomi/pcdetail/images/WH_black.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomipcdetail_130760011373(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""WH""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:13.753798""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760011406(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:14.069169""")

	def test_likitomipcdetailimagespc_blackpng_130760011428(self):
		r = self.client.get('/likitomi/pcdetail/images/PC_black.png', {})
		self.assertEqual(r.status_code, 200)
	def test_likitomihome_130760011496(self):
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:15.081714""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitominormalplanrefresher_130760011576(self):
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:15.768325""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitomilastupdate_130760011621(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:16.214159""")


	def test_likitomipcdetail_130760011961(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:19.634909""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_130760012014(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:20.148306""")

	def test_likitomihome_13076001216(self):
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:21.713089""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitominormalplanrefresher_130760012217(self):
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:22.173076""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitomilastupdate_130760012261(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:22.622112""")

	def test_likitomipcdetail_130760012401(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:24.032179""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_130760012454(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:24.555077""")

	def test_likitomipcdetail_130760012535(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""CR""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:25.376307""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760012584(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:25.846340""")

	def test_likitomipcdetail_130760012721(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:27.233808""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_13076001276(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:27.611581""")

	def test_likitomipcdetail_130760012834(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["page"]), u"""PT""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:28.358351""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_13076001288(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:28.807214""")

	def test_likitomipcdetail_130760012944(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""WH""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:29.460604""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_13076001298(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:29.810382""")
	def test_likitomihome_130760013348(self):
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:33.603594""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitominormalplanrefresher_130760013434(self):
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:34.349896""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitomilastupdate_13076001348(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:34.808124""")

	def test_likitomipcdetail_130760013626(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["page"]), u"""PT""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:36.275657""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760013673(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:36.742137""")

	def test_likitomipcdetail_130760013971(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""CR""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:39.734603""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760014019(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:40.198867""")

	def test_likitomipcdetail_130760014088(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:40.904628""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_13076001413(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:41.309265""")

	def test_likitomipcdetail_130760014179(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["page"]), u"""PT""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:41.811637""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_13076001423(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:42.310711""")

	def test_likitomipcdetail_130760014279(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""WH""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:42.807677""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760014317(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:43.174710""")

	def test_likitomihome_130760014469(self):
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:44.795591""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitominormalplanrefresher_130760014548(self):
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		#        self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:45.485300""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitomilastupdate_130760014594(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:45.945665""")
	def test_likitomipcdetail_13076001476(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""WH""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:47.628577""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760014816(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:48.165045""")
		#    def test_faviconico_130760014823(self):
		#        r = self.client.get('/favicon.ico', {})
		#        self.assertEqual(r.status_code, 404)
	def test_likitomipcdetail_130760014966(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CR', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CR Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View corrugator plan""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""CR""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:49.683140""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760015012(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:50.123248""")

	def test_likitomipcdetail_130760015067(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'CV', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["title"]), u"""View convertor plan""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:50.696872""")
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""e""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""e""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for CV Login as worker PC""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["page"]), u"""CV""")
	def test_likitomilastupdate_13076001511(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:51.103919""")
		#    def test_faviconico_13076001512(self):
		#        r = self.client.get('/favicon.ico', {})
		#        self.assertEqual(r.status_code, 404)
	def test_likitomipcdetail_130760015157(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'PT', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for PT Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Pad and Partition""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["page"]), u"""PT""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:51.594111""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760015205(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:52.061187""")
		#    def test_faviconico_13076001522(self):
		#        r = self.client.get('/favicon.ico', {})
		#        self.assertEqual(r.status_code, 404)


	def test_likitomipcdetail_130760015258(self):
		r = self.client.get('/likitomi/pcdetail/', {'user': 'workerATPC', 'page': 'WH', })
		self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["section_title"]), u"""Homepage for WH Login as worker PC""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["title"]), u"""View Warehouse""")
		#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["itemsM"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["item_planM"]), u"""[]""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["item_plan"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["page"]), u"""WH""")
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:52.615290""")
		self.assertEqual(unicode(r.context["User"]), u"""workerATPC""")
	def test_likitomilastupdate_130760015297(self):
			r = self.client.get('/likitomi/lastUpdate/', {})
			self.assertEqual(r.status_code, 200)
		#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:52.979924""")
		#    def test_faviconico_130760015309(self):
		#        r = self.client.get('/favicon.ico', {})
		#        self.assertEqual(r.status_code, 404)
	def test_likitomihome_130760015889(self):
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC', })
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["thisMonth"]), u"""7""")
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["likitomi_url"]), u"""/likitomi/""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["title"]), u"""Homepage for PC Login as worker PC""")
	#        self.assertEqual(unicode(r.context["datetoinMonth"]), u"""2011-06-30 00:00:00""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
	#        self.assertEqual(unicode(r.context["datefrominMonth"]), u"""2011-07-01 00:00:00""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["strThisMonth"]), u"""July""")
		self.assertEqual(unicode(r.context["home_url"]), u"""/likitomi/home/""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["items"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
	#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:59.017152""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitominormalplanrefresher_130760015964(self):
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context["item_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["pos"]), u"""-2""")
		self.assertEqual(unicode(r.context["item_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["startList"]), u"""-3""")
		self.assertEqual(unicode(r.context["cr"]), u"""idle""")
		self.assertEqual(unicode(r.context["items_plan_cv"]), u"""[]""")
		self.assertEqual(unicode(r.context["cv"]), u"""idle""")
		self.assertEqual(unicode(r.context["size"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["item_plan_pt"]), u"""[]""")
		self.assertEqual(unicode(r.context["pcdetail_url"]), u"""/likitomi/pcdetail/""")
		self.assertEqual(unicode(r.context["endList"]), u"""0""")
		self.assertEqual(unicode(r.context["items_plan_cr"]), u"""[]""")
		self.assertEqual(unicode(r.context["cvThreeCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCL"]), u"""idle""")
		self.assertEqual(unicode(r.context["wh"]), u"""idle""")
		self.assertEqual(unicode(r.context["cvTwoCS"]), u"""idle""")
	#        self.assertEqual(unicode(r.context["user"]), u"""workerATPC""")
		self.assertEqual(unicode(r.context["cvThreeCW"]), u"""idle""")
		self.assertEqual(unicode(r.context["pt"]), u"""idle""")
		self.assertEqual(unicode(r.context["display_url"]), u"""/likitomi/display/""")
		self.assertEqual(unicode(r.context["is_enable_rightbutton"]), u"""True""")
		self.assertEqual(unicode(r.context["cvThreeCS"]), u"""idle""")
		self.assertEqual(unicode(r.context["item_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["is_enable_leftbutton"]), u"""True""")
	#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:15:59.651206""")
		self.assertEqual(unicode(r.context["items_plan_wh"]), u"""[]""")
		self.assertEqual(unicode(r.context["page"]), u"""PC""")
	def test_likitomilastupdate_130760016007(self):
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)
	#        self.assertEqual(unicode(r.context["today"]), u"""2011-06-09 13:16:00.081672""")





##
## second test
##

	def test_likitomi_131014162783(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")
#	def test_faviconico_131014162876(self): 
#		r = self.client.get('/favicon.ico', {})
#		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014163198(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
#		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
#		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:13:52.256067")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")


	def test_likitominormalplanrefresher_131014163517(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_13101416356(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014163576(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_131014163986(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014164022(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihome_131014164302(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:14:03.155706")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitominormalplanrefresher_131014164426(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014164461(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014164475(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_131014164918(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014164955(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014168566(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})

	def test_likitomihome_131014168606(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:14:46.208543")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomecssfal_style2css_131014168717(self): 
		r = self.client.get('/likitomi/home/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryjs_131014168725(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptflashjs_131014168729(self): 
		r = self.client.get('/likitomi/home/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014170027(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131014170234(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomicssfal_stylecss_131014170238(self): 
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomi_131014172248(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomicssfal_stylecss_131014172254(self): 
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomijavascriptjqueryjs_131014172254(self): 
		r = self.client.get('/likitomi/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomijavascriptflashjs_131014172255(self): 
		r = self.client.get('/likitomi/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomiimagesdjgpng_131014172256(self): 
		r = self.client.get('/likitomi/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_13101417227(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014172273(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014172604(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:15:26.184714")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomecssfal_style2css_131014172718(self): 
		r = self.client.get('/likitomi/home/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryjs_131014172719(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptflashjs_131014172719(self): 
		r = self.client.get('/likitomi/home/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessjquery_ui_1810customcss_13101417272(self): 
		r = self.client.get('/likitomi/home/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_144minjs_131014172722(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_ui_1811customminjs_131014172725(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryquicksearchjs_131014172726(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquerydatatablesjs_131014172726(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.dataTables.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomeimagesquitpng_131014172727(self): 
		r = self.client.get('/likitomi/home/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomeimagesdjgpng_131014172729(self): 
		r = self.client.get('/likitomi/home/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssearch_iconpng_131014172775(self): 
		r = self.client.get('/likitomi/home/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_131014172779(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_e6e6e6_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014172781(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014172817(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131014172832(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_131014172832(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_131014172833(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_dadada_1x400png_131014172894(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_dadada_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_icons_888888_256x240png_131014172956(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_icons_888888_256x240.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101417324(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014173278(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014173741(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014173781(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomi_131014175206(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomijavascriptjqueryjs_131014175214(self): 
		r = self.client.get('/likitomi/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014184368(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014185332(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:17:33.459395")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomecsssmoothnessjquery_ui_1810customcss_131014185444(self): 
		r = self.client.get('/likitomi/home/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_144minjs_131014185444(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_ui_1811customminjs_131014185445(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryquicksearchjs_131014185446(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014187121(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014187156(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014187171(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_13101418759(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014187624(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101418809(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014188122(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101418859(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014188628(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101418909(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014189129(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihome_131014189315(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})

	def test_faviconico_131014189378(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014189599(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014189672(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014190009(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})

	def test_faviconico_131014190051(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014190277(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131035788985(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomijavascriptflashjs_131035789055(self): 
		r = self.client.get('/likitomi/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomicssfal_stylecss_131035789062(self): 
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomijavascriptjqueryjs_131035789065(self): 
		r = self.client.get('/likitomi/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomiimagesdjgpng_131035789121(self): 
		r = self.client.get('/likitomi/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131035789127(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131035789479(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})

	def test_faviconico_131035789583(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036028332(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103602835(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_13103602868(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF360")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
#		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:06.939277")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomejavascriptjquerydatatablesjs_131036028885(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.dataTables.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131036028916(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131036028956(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_131036028972(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_e6e6e6_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131036028978(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_dadada_1x400png_131036029164(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_dadada_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_icons_888888_256x240png_131036029268(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_icons_888888_256x240.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131036029396(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_13103602943(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihome_131036029573(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF360")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
#		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:15.869840")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitominormalplanrefresher_131036029792(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131036029829(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131036029853(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036030056(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036030067(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036030341(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF360")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:23.444801")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131036030473(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036031279(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036031291(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036031759(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:37.603780")

	def test_faviconico_131036031848(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036032053(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036032065(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036033543(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:55.480615")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131036033578(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036033986(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036033998(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036034375(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:59:03.789621")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131036034492(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036037113(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036037148(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036055503(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103605555(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_admin_131036056169(self): 
		r = self.client.get('/admin/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036056192(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuseradd_131036056604(self): 
		r = self.client.get('/admin/auth/user/add/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/add/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036056616(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036056635(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser_131036056979(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036056993(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036057008(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser4_131036057412(self): 
		r = self.client.get('/admin/auth/user/4/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/4/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036057432(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036057451(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)


	def test_adminauthuser_131036057891(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036057905(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036057916(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser5_131036058071(self): 
		r = self.client.get('/admin/auth/user/5/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/5/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058091(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058112(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

#	def test_adminauthuser5_131036058286(self): 
#		r = c.post('/admin/auth/user/5/', {'username': 'workerATCV','first_name': ',''last_name': ',''_save': 'Save','is_active': 'on','initial-date_joined_1': '11:24:09','initial-date_joined_0': '2011-07-11','last_login_1': '11:24:09','last_login_0': '2011-07-11','date_joined_0': '2011-07-11','date_joined_1': '11:24:09','groups': '2','csrfmiddlewaretoken': '356259db856f4631d871552813c3e2fc','password': 'sha1$f6a3f$c8cc3f831c7e3bc4b1ff6efbe45df5bb198ef3b3','email': ',''initial-last_login_0': '2011-07-11','initial-last_login_1': '11:24:09'})

	def test_adminauthuser_131036058291(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058304(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058314(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser3_131036058448(self): 
		r = self.client.get('/admin/auth/user/3/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/3/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058469(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058494(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)



	def test_adminauthuser_13103605880(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058813(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058824(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser6_13103605893(self): 
		r = self.client.get('/admin/auth/user/6/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/6/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058951(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058972(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)


	def test_adminauthuser_13103605931(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036059332(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036059344(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser7_131036059439(self): 
		r = self.client.get('/admin/auth/user/7/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/7/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036059462(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036059478(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)



	def test_adminauthuser_131036059688(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036059701(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036059712(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131036061352(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID':'132','eID': '7'})

	def test_faviconico_131036061398(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131036062369(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131036063657(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '132','eID': '7'})

	def test_faviconico_13103606370(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039291157(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103929132(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039291743(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:01:57.509111")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039292074(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039292353(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:03.546692")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:03.534235")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_131039292367(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039292369(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_13103929237(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039292371(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039292372(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039292373(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039292374(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039292378(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039292379(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039292387(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039293437(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_13103929384(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039293851(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039294204(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:22.070411")

	def test_faviconico_131039294318(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039294465(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:24.673100")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:24.660887")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039294475(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039294476(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039294477(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039294483(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039294486(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039294487(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039294488(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_13103929449(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039294491(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039294495(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039295058(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039295336(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039295347(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039295859(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:38.616343")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_13103929599(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039296981(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:49.823277")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:49.817293")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_13103929699(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039296991(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_131039296993(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039296994(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039296996(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039296997(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039296998(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_13103929700(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039297002(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039297005(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039297569(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:55.709901")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:55.702226")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_131039297577(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039297578(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_13103929758(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039297581(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039297583(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039297584(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039297585(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039297587(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039297589(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039297593(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039297816(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039298064(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:00.668909")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039298201(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039298424(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:04.253531")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:04.246217")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_131039298432(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039298433(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_131039298435(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039298437(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039298438(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039298439(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_13103929844(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039298442(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039298444(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039298447(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039298691(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:03 p.m.','pID': '523','amount': '10100','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039298696(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:06.988627")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039298829(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039299033(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:10.349336")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:10.336873")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039299047(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039299048(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_13103929905(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039299051(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039299052(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_131039299053(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039299054(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_131039299057(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_131039299059(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039299062(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039299258(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:12.617670")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039299398(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039299597(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:15.979479")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:15.973340")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039299604(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039299606(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_131039299607(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039299608(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039299609(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_13103929961(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039299611(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_131039299618(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_13103929962(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039299622(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_13103929997(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:19.711749")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:19.702468")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039299978(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039299979(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_13103929998(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039299982(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039299983(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_131039299985(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039299986(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_13103929999(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_131039299991(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039299994(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039300118(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:03 p.m.','pID': '523','amount': '10100','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039300123(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:21.264070")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039300264(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039300598(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '524','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CA125")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"HKB160")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"1900")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"1")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting TOT720 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"200")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"1180")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:25.988098")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"1150*1900(SHEET)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:25.980748")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"HKS161")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"SHEET")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"TOSTEM THAI")

	def test_likitomilinecrstartcssfal_style2css_131039300605(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039300606(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_131039300608(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039300609(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039300611(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039300612(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039300614(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039300616(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039300618(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039300622(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_13103930149(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:03 p.m.','pID': '524','amount': '150','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039301497(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:34.995528")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039301632(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039301967(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '524','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CA125")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"HKB160")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"1900")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"1")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished TOT720 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"200")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"1180")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:39.684415")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"1150*1900(SHEET)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:39.678691")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"HKS161")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"SHEET")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"TOSTEM THAI")

	def test_likitomilinecrendcssfal_style2css_131039301977(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039301978(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_131039301979(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_13103930198(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039301981(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_131039301982(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039301983(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_131039301985(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_131039301986(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039301992(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039302923(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:03 p.m.','pID': '524','amount': '150','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039302927(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:49.301319")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_likitomiproductlist_131039303034(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:03 p.m.','pID': '524','amount': '150','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039303038(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:50.412119")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039303171(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039303486(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039303498(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039304047(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:00.496737")

	def test_faviconico_131039304145(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039304637(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:06.394511")

	def test_faviconico_131039304738(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039304767(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:07.683215")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:07.675293")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039304774(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039304775(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039304776(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039304778(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039304779(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_13103930478(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039304782(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039304794(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039304796(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039304802(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039305264(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:12.656756")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:12.647585")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039305271(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039305272(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039305273(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039305274(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039305275(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039305276(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039305277(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039305279(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039305281(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039305284(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039305711(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:17.138581")

	def test_faviconico_131039305814(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039305965(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:19.666668")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:19.658438")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039305973(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_131014163517(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_13101416356(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014163576(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_131014163986(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014164022(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihome_131014164302(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:14:03.155706")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitominormalplanrefresher_131014164426(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014164461(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014164475(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_131014164918(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014164955(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014168566(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})

	def test_likitomihome_131014168606(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:14:46.208543")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomecssfal_style2css_131014168717(self): 
		r = self.client.get('/likitomi/home/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryjs_131014168725(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptflashjs_131014168729(self): 
		r = self.client.get('/likitomi/home/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014170027(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131014170234(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomicssfal_stylecss_131014170238(self): 
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomi_131014172248(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomicssfal_stylecss_131014172254(self): 
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomijavascriptjqueryjs_131014172254(self): 
		r = self.client.get('/likitomi/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomijavascriptflashjs_131014172255(self): 
		r = self.client.get('/likitomi/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomiimagesdjgpng_131014172256(self): 
		r = self.client.get('/likitomi/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_13101417227(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014172273(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014172604(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:15:26.184714")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomecssfal_style2css_131014172718(self): 
		r = self.client.get('/likitomi/home/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryjs_131014172719(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptflashjs_131014172719(self): 
		r = self.client.get('/likitomi/home/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessjquery_ui_1810customcss_13101417272(self): 
		r = self.client.get('/likitomi/home/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_144minjs_131014172722(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_ui_1811customminjs_131014172725(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryquicksearchjs_131014172726(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquerydatatablesjs_131014172726(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.dataTables.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomeimagesquitpng_131014172727(self): 
		r = self.client.get('/likitomi/home/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomeimagesdjgpng_131014172729(self): 
		r = self.client.get('/likitomi/home/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssearch_iconpng_131014172775(self): 
		r = self.client.get('/likitomi/home/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_131014172779(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_e6e6e6_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014172781(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014172817(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131014172832(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_131014172832(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_131014172833(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_dadada_1x400png_131014172894(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_dadada_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_icons_888888_256x240png_131014172956(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_icons_888888_256x240.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101417324(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014173278(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014173741(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014173781(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomi_131014175206(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomijavascriptjqueryjs_131014175214(self): 
		r = self.client.get('/likitomi/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014184368(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014185332(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF290")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
##		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-08 23:17:33.459395")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-08 01:35:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomecsssmoothnessjquery_ui_1810customcss_131014185444(self): 
		r = self.client.get('/likitomi/home/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_144minjs_131014185444(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjquery_ui_1811customminjs_131014185445(self): 
		r = self.client.get('/likitomi/home/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomejavascriptjqueryquicksearchjs_131014185446(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131014187121(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014187156(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131014187171(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitominormalplanrefresher_13101418759(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014187624(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101418809(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014188122(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101418859(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014188628(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_13101418909(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131014189129(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihome_131014189315(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})

	def test_faviconico_131014189378(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014189599(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014189672(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131014190009(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})

	def test_faviconico_131014190051(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131014190277(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131035788985(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_likitomijavascriptflashjs_131035789055(self): 
		r = self.client.get('/likitomi/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomicssfal_stylecss_131035789062(self): 
		r = self.client.get('/likitomi/css/fal_style.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomijavascriptjqueryjs_131035789065(self): 
		r = self.client.get('/likitomi/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomiimagesdjgpng_131035789121(self): 
		r = self.client.get('/likitomi/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131035789127(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131035789479(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})

	def test_faviconico_131035789583(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036028332(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103602835(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_13103602868(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF360")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
#		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:06.939277")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitomihomejavascriptjquerydatatablesjs_131036028885(self): 
		r = self.client.get('/likitomi/home/javascript/jquery.dataTables.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131036028916(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131036028956(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_e6e6e6_1x400png_131036028972(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_e6e6e6_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131036028978(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihomecsssmoothnessimagesui_bg_glass_75_dadada_1x400png_131036029164(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_bg_glass_75_dadada_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihomecsssmoothnessimagesui_icons_888888_256x240png_131036029268(self): 
		r = self.client.get('/likitomi/home/css/smoothness/images/ui_icons_888888_256x240.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitominormalplanrefresher_131036029396(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_13103602943(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomihome_131036029573(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPC'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["thisMonth"]), u"7")
		self.assertEqual(unicode(r.context[-1]["item_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["pos"]), u"0")
		self.assertEqual(unicode(r.context[-1]["item_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["startList"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF360")
		self.assertEqual(unicode(r.context[-1]["items_plan_cv"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["items_plan_cr"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["items_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["likitomi_url"]), u"/likitomi/")
		self.assertEqual(unicode(r.context[-1]["item_plan_pt"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["pcdetail_url"]), u"/likitomi/pcdetail/")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PC Login as  ")
#		self.assertEqual(unicode(r.context[-1]["datetoinMonth"]), u"2011-07-31 00:00:00")
		self.assertEqual(unicode(r.context[-1]["endList"]), u"3")
		self.assertEqual(unicode(r.context[-1]["size"]), u"43")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:15.869840")
#		self.assertEqual(unicode(r.context[-1]["datefrominMonth"])[", u"2011-07-01 00:00:00")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPC")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["strThisMonth"]), u"July")
		self.assertEqual(unicode(r.context[-1]["home_url"]), u"/likitomi/home/")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items_plan_wh"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PC")

	def test_likitominormalplanrefresher_131036029792(self): 
		r = self.client.get('/likitomi/normalPlanRefresher/', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilastupdate_131036029829(self): 
		r = self.client.get('/likitomi/lastUpdate/', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131036029853(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036030056(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036030067(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036030341(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"EPF360")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:23.444801")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131036030473(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036031279(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036031291(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036031759(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"KFC940")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:37.603780")

	def test_faviconico_131036031848(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036032053(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036032065(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036033543(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:58:55.480615")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131036033578(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036033986(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036033998(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131036034375(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 11:59:03.789621")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131036034492(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036037113(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131036037148(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131036055503(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103605555(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_admin_131036056169(self): 
		r = self.client.get('/admin/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036056192(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuseradd_131036056604(self): 
		r = self.client.get('/admin/auth/user/add/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/add/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036056616(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036056635(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser_131036056979(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036056993(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036057008(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser4_131036057412(self): 
		r = self.client.get('/admin/auth/user/4/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/4/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036057432(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036057451(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)


	def test_adminauthuser_131036057891(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036057905(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036057916(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser5_131036058071(self): 
		r = self.client.get('/admin/auth/user/5/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/5/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058091(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058112(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

#	def test_adminauthuser5_131036058286(self): 
#		r = c.post('/admin/auth/user/5/', {'username': 'workerATCV','first_name': ',''last_name': ',''_save': 'Save','is_active': 'on','initial-date_joined_1': '11:24:09','initial-date_joined_0': '2011-07-11','last_login_1': '11:24:09','last_login_0': '2011-07-11','date_joined_0': '2011-07-11','date_joined_1': '11:24:09','groups': '2','csrfmiddlewaretoken': '356259db856f4631d871552813c3e2fc','password': 'sha1$f6a3f$c8cc3f831c7e3bc4b1ff6efbe45df5bb198ef3b3','email': ',''initial-last_login_0': '2011-07-11','initial-last_login_1': '11:24:09'})

	def test_adminauthuser_131036058291(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058304(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058314(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser3_131036058448(self): 
		r = self.client.get('/admin/auth/user/3/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/3/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058469(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058494(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)



	def test_adminauthuser_13103605880(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058813(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058824(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser6_13103605893(self): 
		r = self.client.get('/admin/auth/user/6/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/6/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036058951(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036058972(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)


	def test_adminauthuser_13103605931(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036059332(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036059344(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_adminauthuser7_131036059439(self): 
		r = self.client.get('/admin/auth/user/7/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/7/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036059462(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036059478(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)



	def test_adminauthuser_131036059688(self): 
		r = self.client.get('/admin/auth/user/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/auth/user/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_adminjsi18n_131036059701(self): 
		r = self.client.get('/admin/jsi18n/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["app_path"]), u"/admin/jsi18n/?test_client_true=yes")
		self.assertEqual(unicode(r.context[-1]["error_message"]), u"")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Log in")
		self.assertEqual(unicode(r.context[-1]["root_path"]), u"None")

	def test_faviconico_131036059712(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131036061352(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID':'132','eID': '7'})

	def test_faviconico_131036061398(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131036062369(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131036063657(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '132','eID': '7'})

	def test_faviconico_13103606370(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039291157(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103929132(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039291743(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:01:57.509111")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039292074(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039292353(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:03.546692")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:03.534235")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_131039292367(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039292369(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_13103929237(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039292371(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039292372(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039292373(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039292374(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039292378(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039292379(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039292387(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039293437(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_13103929384(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039293851(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039294204(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:22.070411")

	def test_faviconico_131039294318(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039294465(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:24.673100")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:24.660887")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039294475(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039294476(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039294477(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039294483(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039294486(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039294487(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039294488(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_13103929449(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039294491(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039294495(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039295058(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039295336(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039295347(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039295859(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:38.616343")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_13103929599(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039296981(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:49.823277")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:49.817293")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_13103929699(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039296991(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_131039296993(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039296994(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039296996(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039296997(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039296998(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_13103929700(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039297002(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039297005(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039297569(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:02:55.709901")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:02:55.702226")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_131039297577(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039297578(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_13103929758(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039297581(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039297583(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039297584(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039297585(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039297587(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039297589(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039297593(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039297816(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039298064(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:00.668909")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039298201(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039298424(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:04.253531")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:04.246217")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrstartcssfal_style2css_131039298432(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039298433(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_131039298435(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039298437(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039298438(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039298439(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_13103929844(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039298442(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039298444(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039298447(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039298691(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:03 p.m.','pID': '523','amount': '10100','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039298696(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:06.988627")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039298829(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039299033(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:10.349336")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:10.336873")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039299047(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039299048(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_13103929905(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039299051(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039299052(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_131039299053(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039299054(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_131039299057(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_131039299059(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039299062(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039299258(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:12.617670")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039299398(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039299597(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:15.979479")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:15.973340")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039299604(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039299606(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_131039299607(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039299608(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039299609(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_13103929961(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039299611(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_131039299618(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_13103929962(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039299622(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_13103929997(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '523','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CM150")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"CM190")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"350")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"396")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KFC930")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"4")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KFC930 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"10100")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"260")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:19.711749")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"Tang Orange 35g X 144 (PT000351)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:19.702468")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"KB30")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"523")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"3CM")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039299978(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039299979(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_13103929998(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039299982(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039299983(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_131039299985(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039299986(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_13103929999(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_131039299991(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039299994(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039300118(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:03 p.m.','pID': '523','amount': '10100','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039300123(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:21.264070")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039300264(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039300598(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '524','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CA125")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"HKB160")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"1900")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"1")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting TOT720 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"200")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"1180")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:25.988098")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"1150*1900(SHEET)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:25.980748")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"HKS161")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"SHEET")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"TOSTEM THAI")

	def test_likitomilinecrstartcssfal_style2css_131039300605(self): 
		r = self.client.get('/likitomi/line/cr/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryjs_131039300606(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptflashjs_131039300608(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartcsssmoothnessjquery_ui_1810customcss_131039300609(self): 
		r = self.client.get('/likitomi/line/cr/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_144minjs_131039300611(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjquery_ui_1811customminjs_131039300612(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartjavascriptjqueryquicksearchjs_131039300614(self): 
		r = self.client.get('/likitomi/line/cr/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesquitpng_131039300616(self): 
		r = self.client.get('/likitomi/line/cr/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstartimagesdjgpng_131039300618(self): 
		r = self.client.get('/likitomi/line/cr/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039300622(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_13103930149(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:03 p.m.','pID': '524','amount': '150','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039301497(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:34.995528")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039301632(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039301967(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '524','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CA125")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"HKB160")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"1900")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"1")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"TOT720")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"1")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished TOT720 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"200")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"1180")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:03:39.684415")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"1150*1900(SHEET)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:39.678691")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"HKS161")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"524")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"1150")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"SHEET")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"TOSTEM THAI")

	def test_likitomilinecrendcssfal_style2css_131039301977(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryjs_131039301978(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptflashjs_131039301979(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_13103930198(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_144minjs_131039301981(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_131039301982(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039301983(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesquitpng_131039301985(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrendimagesdjgpng_131039301986(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039301992(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039302923(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:03 p.m.','pID': '524','amount': '150','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039302927(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:49.301319")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_likitomiproductlist_131039303034(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:03 p.m.','pID': '524','amount': '150','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039303038(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:03:50.412119")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039303171(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039303486(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039303498(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039304047(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:00.496737")

	def test_faviconico_131039304145(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039304637(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:06.394511")

	def test_faviconico_131039304738(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039304767(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:07.683215")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:07.675293")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039304774(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039304775(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039304776(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039304778(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039304779(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_13103930478(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039304782(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039304794(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039304796(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039304802(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039305264(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:12.656756")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:12.647585")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039305271(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039305272(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039305273(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039305274(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039305275(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039305276(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039305277(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039305279(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039305281(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039305284(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039305711(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:17.138581")

	def test_faviconico_131039305814(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039305965(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:19.666668")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:19.658438")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039305973(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039305974(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039305975(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039305976(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039305977(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039305978(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039305979(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039305981(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039305983(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039305986(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039306233(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:04 p.m.','pID': '566','amount': '1000','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039306235(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:22.373921")

	def test_faviconico_131039306333(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039306571(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:25.724155")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:25.718284")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039306578(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039306579(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039306581(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039306582(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039306584(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039306585(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039306587(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039306589(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_13103930659(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039306595(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039306731(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:04 p.m.','pID': '566','amount': '1000','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039306734(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:27.362104")

	def test_faviconico_13103930683(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvend_13103930718(self): 
		r = self.client.get('/likitomi/line/cv/end/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished AAA010 in corvertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:31.814072")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:31.810323")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvendcssfal_style2css_131039307192(self): 
		r = self.client.get('/likitomi/line/cv/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjqueryjs_131039307194(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptflashjs_131039307195(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendcsssmoothnessjquery_ui_1810customcss_131039307196(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjquery_144minjs_131039307197(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjquery_ui_1811customminjs_131039307198(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjqueryquicksearchjs_131039307199(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendimagesquitpng_131039307202(self): 
		r = self.client.get('/likitomi/line/cv/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendimagesdjgpng_131039307203(self): 
		r = self.client.get('/likitomi/line/cv/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039307206(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039307415(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:34.173355")

	def test_faviconico_131039307516(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039307636(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting AAA010 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:36.379681")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:36.368703")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039307645(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039307646(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039307647(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039307649(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_13103930765(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039307651(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039307652(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039307654(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039307655(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039307659(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039308389(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:04 p.m.','pID': '566','amount': '900','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039308391(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:43.939213")

	def test_faviconico_131039308491(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvend_131039308717(self): 
		r = self.client.get('/likitomi/line/cv/end/', {'pID': '566','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished AAA010 in corvertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:47.178133")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:47.176202")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvendcssfal_style2css_131039308724(self): 
		r = self.client.get('/likitomi/line/cv/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjqueryjs_131039308726(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptflashjs_131039308727(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendcsssmoothnessjquery_ui_1810customcss_131039308728(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjquery_144minjs_131039308729(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjquery_ui_1811customminjs_13103930873(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjqueryquicksearchjs_131039308731(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendimagesquitpng_131039308733(self): 
		r = self.client.get('/likitomi/line/cv/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendimagesdjgpng_131039308735(self): 
		r = self.client.get('/likitomi/line/cv/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039308738(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039309152(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:04 p.m.','pID': '566','amount': '900','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039309155(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:51.579815")

	def test_faviconico_131039309257(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039309712(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '541','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"541")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"None")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"LIM660")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting LIM660 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"541")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"572")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:04:57.137740")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:57.130807")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvstartcssfal_style2css_131039309719(self): 
		r = self.client.get('/likitomi/line/cv/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryjs_131039309721(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptflashjs_131039309722(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartcsssmoothnessjquery_ui_1810customcss_131039309723(self): 
		r = self.client.get('/likitomi/line/cv/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_144minjs_131039309724(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjquery_ui_1811customminjs_131039309725(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartjavascriptjqueryquicksearchjs_131039309726(self): 
		r = self.client.get('/likitomi/line/cv/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesquitpng_131039309728(self): 
		r = self.client.get('/likitomi/line/cv/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstartimagesdjgpng_131039309729(self): 
		r = self.client.get('/likitomi/line/cv/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039309732(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039309892(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:04 p.m.','pID': '541','amount': '572','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039309895(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:04:58.976576")

	def test_faviconico_131039309996(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvend_131039310145(self): 
		r = self.client.get('/likitomi/line/cv/end/', {'pID': '541','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"541")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"None")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"LIM660")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished LIM660 in corvertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"541")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"572")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:01.459682")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:01.457782")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvendcssfal_style2css_131039310153(self): 
		r = self.client.get('/likitomi/line/cv/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjqueryjs_131039310154(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptflashjs_131039310155(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendcsssmoothnessjquery_ui_1810customcss_131039310157(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjquery_144minjs_131039310158(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjquery_ui_1811customminjs_131039310159(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendjavascriptjqueryquicksearchjs_13103931016(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendimagesquitpng_131039310162(self): 
		r = self.client.get('/likitomi/line/cv/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvendimagesdjgpng_131039310164(self): 
		r = self.client.get('/likitomi/line/cv/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039310167(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039310299(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:05 p.m.','pID': '541','amount': '572','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039310304(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:03.069224")

	def test_faviconico_131039310403(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039310814(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039310828(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_13103931159(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:15.955933")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039311638(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstart_131039311862(self): 
		r = self.client.get('/likitomi/line/pt/start/', {'pID': '566','eID': '6'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"PT")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Starting AAA010 in pad /partition")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:18.640929")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:18.629830")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilineptstartcssfal_style2css_131039311873(self): 
		r = self.client.get('/likitomi/line/pt/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjqueryjs_131039311875(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptflashjs_131039311876(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartcsssmoothnessjquery_ui_1810customcss_131039311877(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjquery_144minjs_131039311878(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjquery_ui_1811customminjs_131039311879(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjqueryquicksearchjs_13103931188(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartimagesquitpng_131039311884(self): 
		r = self.client.get('/likitomi/line/pt/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartimagesdjgpng_131039311886(self): 
		r = self.client.get('/likitomi/line/pt/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039311889(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_13103931222(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:22.229339")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039312256(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstart_13103931237(self): 
		r = self.client.get('/likitomi/line/pt/start/', {'pID': '566','eID': '6'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"PT")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Starting AAA010 in pad /partition")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:23.716189")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:23.708729")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilineptstartcssfal_style2css_131039312377(self): 
		r = self.client.get('/likitomi/line/pt/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjqueryjs_131039312378(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptflashjs_131039312379(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartcsssmoothnessjquery_ui_1810customcss_13103931238(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjquery_144minjs_131039312381(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjquery_ui_1811customminjs_131039312382(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjqueryquicksearchjs_131039312383(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartimagesquitpng_131039312386(self): 
		r = self.client.get('/likitomi/line/pt/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartimagesdjgpng_131039312387(self): 
		r = self.client.get('/likitomi/line/pt/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_13103931239(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstart_13103931248(self): 
		r = self.client.get('/likitomi/line/pt/start/', {'pID': '566','eID': '6'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"PT")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Starting AAA010 in pad /partition")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:24.822017")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:24.811326")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilineptstartcssfal_style2css_131039312488(self): 
		r = self.client.get('/likitomi/line/pt/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjqueryjs_131039312489(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptflashjs_13103931249(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartcsssmoothnessjquery_ui_1810customcss_131039312491(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjquery_144minjs_131039312493(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjquery_ui_1811customminjs_131039312494(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartjavascriptjqueryquicksearchjs_131039312495(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartimagesquitpng_131039312497(self): 
		r = self.client.get('/likitomi/line/pt/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstartimagesdjgpng_131039312498(self): 
		r = self.client.get('/likitomi/line/pt/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039312501(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039312645(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:05 p.m.','pID': '566','amount': '1000','at': 'PT','Enter': 'Enter','eID': '6'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039312649(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:26.518379")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039312686(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptend_131039312837(self): 
		r = self.client.get('/likitomi/line/pt/end/', {'pID': '566','eID': '6'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"PT")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished AAA010 in pad /partition")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:28.384627")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:28.381087")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilineptendcssfal_style2css_13103931285(self): 
		r = self.client.get('/likitomi/line/pt/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendjavascriptjqueryjs_131039312853(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendjavascriptflashjs_131039312854(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendcsssmoothnessjquery_ui_1810customcss_131039312855(self): 
		r = self.client.get('/likitomi/line/pt/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendjavascriptjquery_144minjs_131039312856(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendjavascriptjquery_ui_1811customminjs_131039312857(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendjavascriptjqueryquicksearchjs_131039312859(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendimagesquitpng_131039312861(self): 
		r = self.client.get('/likitomi/line/pt/end/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptendimagesdjgpng_131039312862(self): 
		r = self.client.get('/likitomi/line/pt/end/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039312865(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039313054(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:05 p.m.','pID': '566','amount': '1000','at': 'PT','Enter': 'Enter','eID': '6'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039313057(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:30.610544")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039313095(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_13103931342(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039313433(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039313936(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 01:29:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:39.425388")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039314069(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131039314264(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '529','eID': '7'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"529")
		self.assertEqual(unicode(r.context[-1]["at"]), u"WH")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KSP130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KSP130 warehouse")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"In")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"529")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"540")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"KANSAI PAINT")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:42.661837")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"JOMAR 4*4 KGS.")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:42.650496")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinewhstartcssfal_style2css_131039314277(self): 
		r = self.client.get('/likitomi/line/wh/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjqueryjs_131039314278(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptflashjs_131039314279(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartcsssmoothnessjquery_ui_1810customcss_13103931428(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjquery_144minjs_131039314281(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjquery_ui_1811customminjs_131039314282(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjqueryquicksearchjs_131039314284(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartimagesquitpng_131039314287(self): 
		r = self.client.get('/likitomi/line/wh/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartimagesdjgpng_131039314288(self): 
		r = self.client.get('/likitomi/line/wh/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039314291(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_13103931446(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:05 p.m.','pID': '529','amount': '540','at': 'WH','Enter': 'Enter','eID': '7'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039314464(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 02:14:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:44.677097")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039314584(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131039314931(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '543','eID': '7'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"543")
		self.assertEqual(unicode(r.context[-1]["at"]), u"WH")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"LTT370")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished LTT370 warehouse")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"In")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"543")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"892")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"Lion (Thailand) Co., Ltd.")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:49.334192")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"ESSENCE PRE WASH 220 ML.")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:49.323614")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinewhstartcssfal_style2css_131039314941(self): 
		r = self.client.get('/likitomi/line/wh/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjqueryjs_131039314943(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptflashjs_131039314944(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartcsssmoothnessjquery_ui_1810customcss_131039314945(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjquery_144minjs_131039314947(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjquery_ui_1811customminjs_131039314948(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjqueryquicksearchjs_13103931495(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartimagesquitpng_131039314952(self): 
		r = self.client.get('/likitomi/line/wh/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartimagesdjgpng_131039314954(self): 
		r = self.client.get('/likitomi/line/wh/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039314957(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039315173(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131039315352(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '529','eID': '7'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"529")
		self.assertEqual(unicode(r.context[-1]["at"]), u"WH")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"KSP130")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished KSP130 warehouse")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"In")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"529")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"540")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"KANSAI PAINT")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:05:53.534726")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"JOMAR 4*4 KGS.")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:53.525254")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinewhstartcssfal_style2css_131039315359(self): 
		r = self.client.get('/likitomi/line/wh/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjqueryjs_13103931536(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptflashjs_131039315361(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartcsssmoothnessjquery_ui_1810customcss_131039315363(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjquery_144minjs_131039315364(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjquery_ui_1811customminjs_131039315365(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartjavascriptjqueryquicksearchjs_131039315366(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartimagesquitpng_131039315368(self): 
		r = self.client.get('/likitomi/line/wh/start/images/quit.png', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstartimagesdjgpng_131039315369(self): 
		r = self.client.get('/likitomi/line/wh/start/images/djg.png', {})
		self.assertEqual(r.status_code, 404)

	def test_faviconico_131039315373(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_13103931558(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:05 p.m.','pID': '529','amount': '540','at': 'WH','Enter': 'Enter','eID': '7'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039315584(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 02:14:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:55.872673")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039315705(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039315899(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 02:14:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:05:59.037168")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039316021(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_13103931684(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039316854(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039392858(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:18:48.682843")

	def test_faviconico_131039392965(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039393133(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:18:51.353868")

	def test_faviconico_13103939322(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039393658(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039393672(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039394107(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:01.099037")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_13103939424(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrstart_131039394698(self): 
		r = self.client.get('/likitomi/line/cr/start/', {'pID': '525','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CA125")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"EKS230")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"0")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"3")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"563")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"1")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting MPM650 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"525")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"840")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"1740")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:19:06.995804")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:06.984030")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"EKS230")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"525")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"293")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_faviconico_131039394734(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039394922(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:19 p.m.','pID': '525','amount': '840','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039394927(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:09.299128")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039395063(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecrend_131039395178(self): 
		r = self.client.get('/likitomi/line/cr/end/', {'pID': '525','eID': '4'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["bl"]), u"")
		self.assertEqual(unicode(r.context[-1]["cm"]), u"CA125")
		self.assertEqual(unicode(r.context[-1]["cl"]), u"EKS230")
		self.assertEqual(unicode(r.context[-1]["length_mm"]), u"0")
		self.assertEqual(unicode(r.context[-1]["slit"]), u"3")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CR")
		self.assertEqual(unicode(r.context[-1]["blank"]), u"563")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"MPM650")
		self.assertEqual(unicode(r.context[-1]["cut"]), u"1")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished MPM650 in corrugator")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"525")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"840")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["width_mm"]), u"1740")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:19:11.799123")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:11.789326")
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["df"]), u"EKS230")
		self.assertEqual(unicode(r.context[-1]["bm"]), u"")
		self.assertEqual(unicode(r.context[-1]["flute"]), u"C")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"525")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")
		self.assertEqual(unicode(r.context[-1]["scoreline"]), u"293")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["next_process"]), u"")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")

	def test_likitomilinecrendcssfal_style2css_131039395187(self): 
		r = self.client.get('/likitomi/line/cr/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendjavascriptjqueryjs_131039395188(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendjavascriptflashjs_131039395188(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendcsssmoothnessjquery_ui_1810customcss_131039395189(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendjavascriptjquery_144minjs_13103939519(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendjavascriptjquery_ui_1811customminjs_13103939519(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendjavascriptjqueryquicksearchjs_131039395193(self): 
		r = self.client.get('/likitomi/line/cr/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendcsssearch_iconpng_131039395218(self): 
		r = self.client.get('/likitomi/line/cr/end/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131039395219(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_13103939522(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_13103939522(self): 
		r = self.client.get('/likitomi/line/cr/end/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendimagesquitpng_131039395221(self): 
		r = self.client.get('/likitomi/line/cr/end/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecrendimagesdjgpng_131039395221(self): 
		r = self.client.get('/likitomi/line/cr/end/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131039395225(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039395381(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:19 p.m.','pID': '525','amount': '840','at': 'CR','Enter': 'Enter','eID': '4'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039395384(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCR','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCR")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CR Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"4")
		self.assertEqual(unicode(r.context[-1]["x"]), u"")
		self.assertEqual(unicode(r.context[-1]["cr"]), u"WPR040")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CR")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:13.879327")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCR")

	def test_faviconico_131039395521(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039395685(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039395699(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_13103939616(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:21.619120")

	def test_faviconico_131039396264(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvstart_131039396417(self): 
		r = self.client.get('/likitomi/line/cv/start/', {'pID': '539','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"539")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"None")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"LSU880")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"starting LSU880 in convertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"539")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"7550")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:19:24.186945")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:24.180309")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_faviconico_131039396453(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_13103939660(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:19 p.m.','pID': '539','amount': '7550','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039396604(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:26.055468")

	def test_faviconico_131039396704(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinecvend_131039396794(self): 
		r = self.client.get('/likitomi/line/cv/end/', {'pID': '539','eID': '5'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"539")
		self.assertEqual(unicode(r.context[-1]["at"]), u"CV")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"None")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"LSU880")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"0")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished LSU880 in corvertor")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"539")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"7550")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:19:27.950135")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:27.946978")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinecvendcssfal_style2css_131039396802(self): 
		r = self.client.get('/likitomi/line/cv/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendjavascriptjqueryjs_131039396802(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendjavascriptflashjs_131039396803(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendcsssmoothnessjquery_ui_1810customcss_131039396804(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendjavascriptjquery_144minjs_131039396804(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendjavascriptjquery_ui_1811customminjs_131039396805(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendjavascriptjqueryquicksearchjs_131039396806(self): 
		r = self.client.get('/likitomi/line/cv/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendcsssearch_iconpng_131039396837(self): 
		r = self.client.get('/likitomi/line/cv/end/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131039396837(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_131039396838(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_131039396838(self): 
		r = self.client.get('/likitomi/line/cv/end/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendimagesquitpng_131039396839(self): 
		r = self.client.get('/likitomi/line/cv/end/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinecvendimagesdjgpng_13103939684(self): 
		r = self.client.get('/likitomi/line/cv/end/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131039396845(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039396952(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:19 p.m.','pID': '539','amount': '7550','at': 'CV','Enter': 'Enter','eID': '5'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039396957(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATCV','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvTwoCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvThreeCL"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["cvTwoCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATCV")
		self.assertEqual(unicode(r.context[-1]["cvThreeCW"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cv"]), u"TPD140")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for CV Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["cvThreeCS"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"5")
		self.assertEqual(unicode(r.context[-1]["page"]), u"CV")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:29.607051")

	def test_faviconico_131039397059(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039397396(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_13103939741(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039398029(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:40.339606")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039398071(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptstart_131039398405(self): 
		r = self.client.get('/likitomi/line/pt/start/', {'pID': '566','eID': '6'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"PT")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Starting AAA010 in pad /partition")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Load")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:19:44.073209")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:44.060819")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilineptstartcssfal_style2css_131039398414(self): 
		r = self.client.get('/likitomi/line/pt/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartjavascriptjqueryjs_131039398414(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartjavascriptflashjs_131039398415(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartcsssmoothnessjquery_ui_1810customcss_131039398416(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartjavascriptjquery_144minjs_131039398416(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartjavascriptjquery_ui_1811customminjs_131039398417(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartjavascriptjqueryquicksearchjs_131039398418(self): 
		r = self.client.get('/likitomi/line/pt/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartcsssearch_iconpng_131039398452(self): 
		r = self.client.get('/likitomi/line/pt/start/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131039398452(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_131039398453(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_131039398454(self): 
		r = self.client.get('/likitomi/line/pt/start/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartimagesquitpng_131039398454(self): 
		r = self.client.get('/likitomi/line/pt/start/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptstartimagesdjgpng_131039398455(self): 
		r = self.client.get('/likitomi/line/pt/start/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131039398458(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039398561(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:19 p.m.','pID': '566','amount': '1000','at': 'PT','Enter': 'Enter','eID': '6'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039398564(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:45.693393")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039398606(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineptend_131039398685(self): 
		r = self.client.get('/likitomi/line/pt/end/', {'pID': '566','eID': '6'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["color"]), u"Red")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["at"]), u"PT")
		self.assertEqual(unicode(r.context[-1]["partner"]), u"")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"AAA010")
		self.assertEqual(unicode(r.context[-1]["speed"]), u"80")
		self.assertEqual(unicode(r.context[-1]["cv_machine"]), u"2CL")
		self.assertEqual(unicode(r.context[-1]["task"]), u"end")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished AAA010 in pad /partition")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Finish")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"566")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"1000")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:19:46.862301")

#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:46.859701")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilineptendcssfal_style2css_131039398696(self): 
		r = self.client.get('/likitomi/line/pt/end/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendjavascriptjqueryjs_131039398696(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendjavascriptflashjs_131039398697(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendcsssmoothnessjquery_ui_1810customcss_131039398698(self): 
		r = self.client.get('/likitomi/line/pt/end/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendjavascriptjquery_144minjs_131039398698(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendjavascriptjquery_ui_1811customminjs_131039398699(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendjavascriptjqueryquicksearchjs_131039398699(self): 
		r = self.client.get('/likitomi/line/pt/end/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendcsssearch_iconpng_131039398752(self): 
		r = self.client.get('/likitomi/line/pt/end/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131039398755(self): 
		r = self.client.get('/likitomi/line/pt/end/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_131039398755(self): 
		r = self.client.get('/likitomi/line/pt/end/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_131039398756(self): 
		r = self.client.get('/likitomi/line/pt/end/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendimagesquitpng_131039398757(self): 
		r = self.client.get('/likitomi/line/pt/end/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilineptendimagesdjgpng_131039398757(self): 
		r = self.client.get('/likitomi/line/pt/end/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131039398782(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomiproductlist_131039398824(self): 
		r = self.client.get('/likitomi/product/list/', {'task': 'end','start_time': 'July 11, 2011, 9:19 p.m.','pID': '566','amount': '1000','at': 'PT','Enter': 'Enter','eID': '6'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039398826(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATPT','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATPT")
		self.assertEqual(unicode(r.context[-1]["pt"]), u"idle")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for PT Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"6")
		self.assertEqual(unicode(r.context[-1]["page"]), u"PT")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:48.309444")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATPT")

	def test_faviconico_131039398866(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039398925(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039398938(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomihome_131039399769(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 02:14:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:19:57.733480")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039399889(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131039400078(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '543','eID': '7'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"543")
		self.assertEqual(unicode(r.context[-1]["at"]), u"WH")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"LTT370")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished LTT370 warehouse")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"In")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"543")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"892")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"Lion (Thailand) Co., Ltd.")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:20:00.791755")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"ESSENCE PRE WASH 220 ML.")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:20:00.785790")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_likitomilinewhstartcssfal_style2css_131039400085(self): 
		r = self.client.get('/likitomi/line/wh/start/css/fal_style2.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartjavascriptjqueryjs_131039400086(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartjavascriptflashjs_131039400087(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/flash.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartcsssmoothnessjquery_ui_1810customcss_131039400087(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/jquery_ui_1.8.10.custom.css', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartjavascriptjquery_144minjs_131039400088(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_1.4.4.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartjavascriptjquery_ui_1811customminjs_131039400089(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery_ui_1.8.11.custom.min.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartjavascriptjqueryquicksearchjs_131039400089(self): 
		r = self.client.get('/likitomi/line/wh/start/javascript/jquery.quicksearch.js', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartcsssearch_iconpng_131039400117(self): 
		r = self.client.get('/likitomi/line/wh/start/css/search_icon.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartcsssmoothnessimagesui_bg_flat_75_ffffff_40x100png_131039400117(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/images/ui_bg_flat_75_ffffff_40x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartcsssmoothnessimagesui_bg_highlight_soft_75_cccccc_1x100png_131039400118(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/images/ui_bg_highlight_soft_75_cccccc_1x100.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartcsssmoothnessimagesui_bg_glass_65_ffffff_1x400png_131039400119(self): 
		r = self.client.get('/likitomi/line/wh/start/css/smoothness/images/ui_bg_glass_65_ffffff_1x400.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartimagesquitpng_131039400119(self): 
		r = self.client.get('/likitomi/line/wh/start/images/quit.png', {})
		self.assertEqual(r.status_code, 200)

	def test_likitomilinewhstartimagesdjgpng_13103940012(self): 
		r = self.client.get('/likitomi/line/wh/start/images/djg.png', {})
		self.assertEqual(r.status_code, 200)

	def test_faviconico_131039400123(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039400231(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:20 p.m.','pID': '543','amount': '892','at': 'WH','Enter': 'Enter','eID': '7'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039400235(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 10:40:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:20:02.383024")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039400357(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131039400482(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '554','eID': '7'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"554")
		self.assertEqual(unicode(r.context[-1]["at"]), u"WH")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"TOT810")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished TOT810 warehouse")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"In")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"554")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"200")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"TOSTEM THAI")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:20:04.842583")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"1300*2850(SHEET)")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:20:04.831988")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_faviconico_13103940050(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039400602(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:20 p.m.','pID': '554','amount': '200','at': 'WH','Enter': 'Enter','eID': '7'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039400606(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 10:40:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:20:06.098784")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039400727(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilinewhstart_131039400899(self): 
		r = self.client.get('/likitomi/line/wh/start/', {'pID': '550','eID': '7'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["product"]), u"Products object")
		self.assertEqual(unicode(r.context[-1]["pID"]), u"550")
		self.assertEqual(unicode(r.context[-1]["at"]), u"WH")
		self.assertEqual(unicode(r.context[-1]["product_code"]), u"SHI780")
		self.assertEqual(unicode(r.context[-1]["task"]), u"start")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Finished SHI780 warehouse")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"In")
		self.assertEqual(unicode(r.context[-1]["planID"]), u"550")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["productCat"]), u"ProductCatalog object")
		self.assertEqual(unicode(r.context[-1]["amount"]), u"42")
		self.assertEqual(unicode(r.context[-1]["cname"]), u"None")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["employee"]), u"AuthUser object")
		self.assertEqual(unicode(r.context[-1]["current_date_time"]), u"2011-07-11 21:20:09.016644")
		self.assertEqual(unicode(r.context[-1]["product_name"]), u"SPAKCC 947 JBEZ(AU-A18 LM")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:20:09.005753")
		self.assertEqual(unicode(r.context[-1]["plan"]), u"StatusTracking object")

	def test_faviconico_131039400928(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomilineupdatestart_131039401025(self): 
		r = self.client.get('/likitomi/line/update/start/', {'task': 'start','start_time': 'July 11, 2011, 9:20 p.m.','pID': '550','amount': '42','at': 'WH','Enter': 'Enter','eID': '7'})
		self.assertEqual(r.status_code, 302)

	def test_likitomihome_131039401029(self): 
		r = self.client.get('/likitomi/home/', {'user': 'workerATWH','Enter': 'Enter'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["username"]), u"workerATWH")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Homepage for WH Login as  ")
		self.assertEqual(unicode(r.context[-1]["is_enable_rightbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["items"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>]")
		self.assertEqual(unicode(r.context[-1]["wh"]), u"2011-07-11 10:42:00")
		self.assertEqual(unicode(r.context[-1]["item_plan"]), u"[<StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, <StatusTracking: StatusTracking object>, '...(remaining elements truncated)...']")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"True")
		self.assertEqual(unicode(r.context[-1]["eID"]), u"7")
		self.assertEqual(unicode(r.context[-1]["page"]), u"WH")
#		self.assertEqual(unicode(r.context[-1]["today"]), u"2011-07-11 21:20:10.326619")
		self.assertEqual(unicode(r.context[-1]["user"]), u"workerATWH")

	def test_faviconico_131039401148(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

	def test_likitomi_131039401626(self): 
		r = self.client.get('/likitomi/', {})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(unicode(r.context[-1]["item_pic"]), u"thumbs/mail.png")
		self.assertEqual(unicode(r.context[-1]["subcontent_header"]), u"Please scan or enter employee code")
		self.assertEqual(unicode(r.context[-1]["la_user_name"]), u"USERNAME")
		self.assertEqual(unicode(r.context[-1]["is_enable_comment"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_tributton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["flashMessage"]), u"")
		self.assertEqual(unicode(r.context[-1]["section_title"]), u"Welcome")
		self.assertEqual(unicode(r.context[-1]["is_enable_arrow"]), u"False")
		self.assertEqual(unicode(r.context[-1]["item_name"]), u"Item name")
		self.assertEqual(unicode(r.context[-1]["content_header"]), u"Login")
		self.assertEqual(unicode(r.context[-1]["is_enable_login"]), u"True")
		self.assertEqual(unicode(r.context[-1]["is_enable_leftbutton"]), u"False")
		self.assertEqual(unicode(r.context[-1]["is_enable_link"]), u"False")
		self.assertEqual(unicode(r.context[-1]["title"]), u"Welcome to Likitomi Status Tracking System")
		self.assertEqual(unicode(r.context[-1]["page"]), u"login")

	def test_faviconico_131039401639(self): 
		r = self.client.get('/favicon.ico', {})
		self.assertEqual(r.status_code, 404)

