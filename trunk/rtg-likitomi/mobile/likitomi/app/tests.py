"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
import unittest
#from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from general import index
from app.models import Employee, FakeStatusTracking
from utility import todayDate, currentProcess, currentTimeProcess, positionOfCurrentProcess, returnStartingPoint, returnall
from config import getPCItemNum

class SimpleTest(unittest.TestCase):
	fixtures = ['app_testfixture.json', 'FakeStatusTracking']
	def setUp(self):
		self.client = Client()
	def test_general(self):
		"""Tests login page"""
		response = self.client.get('/likitomi/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['title'],'Welcome to Likitomi Status Tracking System')
		self.assertEqual(response.context['subcontent_header'],"Please scan or enter employee code")
		self.failUnlessEqual(response.context['subcontent_header'],"Please scan or enter employee code")
	def test_idle(self):
		""" Test idle state of machine """
		status = FakeStatusTracking(plan_id='1', product_id='MLT790',plan_amount='500',plan_cr_start='2010-11-19 08:00:00',plan_cr_end='2010-11-19 09:05:00',plan_cv_start='2010-11-19 09:31:00',plan_cv_end='2010-11-19 09:45:00',plan_pt_start ='2010-11-19 10:50:00', plan_pt_end='2010-11-19 10:50:00', plan_wh_start='2010-11-19 12:00:00',actual_cr_start='2010-11-19 08:15:00',actual_cr_end='2010-11-19 09:15:00',actual_cv_start='2010-11-19 08:15:00',actual_cv_end='2010-11-19 09:15:00',actual_pt_start='2010-11-19 11:15:00',actual_pt_end='2010-11-19 11:15:00',actual_wh_start='2010-11-19 11:15:00',)
		status.save()
	def test_multiitems(self):
		""" Test adding multi items """
		status = FakeStatusTracking(plan_id='1', product_id='MLT790',plan_amount='500',plan_cr_start='2010-11-19 08:00:00',plan_cr_end='2010-11-19 09:05:00',plan_cv_start='2010-11-19 09:31:00',plan_cv_end='2010-11-19 09:45:00',plan_pt_start ='2010-11-19 10:50:00', plan_pt_end='2010-11-19 10:50:00', plan_wh_start='2010-11-19 12:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='2', product_id='UTH140',plan_amount='200',plan_cr_start='2010-11-19 09:31:00', plan_cr_end='2010-11-19 09:35:00', plan_cv_start = '2010-11-19 09:50:00', plan_cv_end = '2010-11-19 10:30:00', plan_wh_start = '2010-11-19 11:00:00')
		status.save()
	def test_fullData(self):
		""" Test insert Data """
		status = FakeStatusTracking(plan_id='1', product_id='MLT790',plan_amount='500',plan_cr_start='2010-11-19 08:00:00',plan_cr_end='2010-11-19 09:05:00',plan_cv_start='2010-11-19 09:31:00',plan_cv_end='2010-11-19 09:45:00',plan_pt_start ='2010-11-19 10:50:00', plan_pt_end='2010-11-19 10:50:00', plan_wh_start='2010-11-19 12:00:00',actual_cr_end='2010-11-19 09:15:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),1)
		status = FakeStatusTracking(plan_id='2', product_id='UTH140',plan_amount='200',plan_cr_start='2010-11-19 09:31:00', plan_cr_end='2010-11-19 09:35:00', plan_cv_start = '2010-11-19 09:50:00', plan_cv_end = '2010-11-19 10:30:00', plan_wh_start = '2010-11-19 11:00:00', actual_cr_end='2010-11-19 09:45:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),2)
		status = FakeStatusTracking(plan_id='3', product_id='UTH130',plan_amount='300',plan_cr_start='2010-11-19 09:37:00', plan_cr_end='2010-11-19 09:40:00', plan_wh_start = '2010-11-19 10:00:00',actual_cr_end='2010-11-19 09:55:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),3)
		status = FakeStatusTracking(plan_id='4', product_id='UTH120',plan_amount='100',plan_cr_start='2010-11-19 09:44:00', plan_cr_end='2010-11-19 09:50:00', plan_wh_start = '2010-11-19 10:00:00',actual_cr_end='2010-11-19 10:05:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),4)
		status = FakeStatusTracking(plan_id='5', product_id='MOL010',plan_amount='300',plan_cr_start='2010-11-19 09:51:00', plan_cr_end='2010-11-19 10:10:00', plan_wh_start = '2010-11-19 11:00:00',actual_cr_end='2010-11-19 10:15:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),5)
		status = FakeStatusTracking(plan_id='6', product_id='ANU010',plan_amount='1300',plan_cr_start='2010-11-19 09:05:00', plan_cr_end='2010-11-19 09:40:00', plan_cv_start = '2010-11-19 09:40:00', plan_cv_end = '2010-11-19 10:30:00',plan_pt_start='2010-11-19 10:45:00',plan_pt_end='2010-11-19 11:30:00', plan_wh_start = '2010-11-19 12:00:00',actual_cr_end='2010-11-19 10:25:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),6)
		status = FakeStatusTracking(plan_id='7', product_id='AAA010',plan_amount='1300',plan_cr_start='2010-11-18 08:00:00', plan_cr_end='2010-11-18 09:00:00', plan_cv_start = '2010-11-19 09:00:00', plan_cv_end = '2010-11-19 09:25:00',plan_pt_start='2010-11-19 09:30:00',plan_pt_end='2010-11-19 10:00:00', plan_wh_start = '2010-11-19 10:30:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),7)
		status = FakeStatusTracking(plan_id='8', product_id='GNG100',plan_amount='600',plan_cr_start='2010-11-18 10:00:00', plan_cr_end='2010-11-18 10:30:00', plan_cv_start = '2010-11-19 09:33:00', plan_cv_end = '2010-11-19 10:30:00', plan_wh_start = '2010-11-19 13:00:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),8)
		status = FakeStatusTracking(plan_id='9', product_id='ADL090',plan_amount='400',plan_cr_start='2010-11-18 11:00:00', plan_cr_end='2010-11-18 11:40:00', plan_cv_start = '2010-11-19 11:00:00', plan_cv_end = '2010-11-19 12:30:00', plan_wh_start = '2010-11-19 13:00:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),9)
		status = FakeStatusTracking(plan_id='10', product_id='KFC010',plan_amount='400',plan_cr_start='2010-11-18 13:00:00', plan_cr_end='2010-11-18 13:30:00', plan_cv_start = '2010-11-18 14:00:00', plan_cv_end = '2010-11-18 14:30:00',plan_pt_start='2010-11-19 08:00:00',plan_pt_end='2010-11-19 08:50:00', plan_wh_start = '2010-11-19 09:00:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),10)
		status = FakeStatusTracking(plan_id='11', product_id='SHG700',plan_amount='900',plan_cr_start='2010-11-18 15:00:00', plan_cr_end='2010-11-18 15:30:00', plan_cv_start = '2010-11-18 15:45:00', plan_cv_end = '2010-11-18 16:00:00',plan_pt_start='2010-11-19 09:00:00',plan_pt_end='2010-11-19 09:30:00', plan_wh_start = '2010-11-19 10:00:00')
		status.save()
		result = FakeStatusTracking.objects.all()
		#self.assertEqual(len(list(result)),11)
	def test_U1(self):
		SimpleTest.test_idle(self)
		""" Test Utility 1.1 : idle state """
		self.assertEqual(currentProcess("CR"),"idle")
		self.assertEqual(currentProcess("CV"),"idle")
		self.assertEqual(currentProcess("PT"),"idle")
		self.assertEqual(currentProcess("WH"),"idle")
	def test_U2(self):
		SimpleTest.test_multiitems(self)
		""" Test Utility 1.2 : two items on the list"""
		self.assertEqual(currentProcess("CR"),unicode('MLT790'))
		self.assertEqual(currentProcess("CV"),unicode('MLT790'))
		self.assertEqual(currentProcess("PT"),unicode('MLT790'))
		self.assertEqual(currentProcess("WH"),unicode('UTH140'))
	def test_U3(self):				
		SimpleTest.test_fullData(self)
		""" Test Utility 1.3 : 12 items on the list"""
		self.assertEqual(len(list(returnall())),11)
		self.assertEqual(currentProcess("CR"),unicode('idle'))
		self.assertEqual(currentTimeProcess("CV"),unicode('idle'))
#		self.assertEqual(currentProcess("2CL"),'')
#		self.assertEqual(currentProcess("3CS"),)
#		self.assertEqual(currentProcess("3CL"),'idle')
#		self.assertEqual(currentProcess("3CW"),'idle')
#		self.assertEqual(currentProcess("2CS"),'idle')
		
#		self.assertEqual(currentProcess("CV")[0][0],'idle')
#		self.assertEqual(currentProcess("3CS")[0][0],unicode('SHG701'))
#		self.assertEqual(currentProcess("3CL"),'idle')
#		self.assertEqual(currentProcess("2CL"),'idle')
#		self.assertEqual(currentProcess("3CW"),'idle')
#		self.assertEqual(currentProcess("2CS"),'idle')
#		self.assertEqual(currentProcess("PT"),'idle')
#		self.assertEqual(list(currentProcess("WH")),list([]))
		# test T101 login
#		emp = Employee(eid='T101',firstname='Fon', lastname ='Prasomwong', task='PC')
#		emp.save()
#		# Test homepage for PC
#		response = self.client.get('/likitomi/home/',{'eID':'T101'})
#		self.assertEqual(response.status_code,200)
#		self.assertEqual(response.context['eID'],'T101')
#		self.assertEqual(response.context['section_title'],"Homepage for PC Login as Fon Prasomwong")
#		#Test queries and items
#		#full list
#		self.assertEqual(len(response.context['item_plan_cr']),6)
#		self.assertEqual(len(response.context['item_plan_cv']),6)
#		self.assertEqual(len(response.context['item_plan_pt']),5)
#		self.assertEqual(len(response.context['item_plan_wh']),11)
#		#limit displys only 3 items for all
#		self.assertEqual(len(response.context['items_plan_cr']),3)
#		self.assertEqual(len(response.context['items_plan_cv']),3)
#		self.assertEqual(len(response.context['items_plan_pt']),3)
#		self.assertEqual(len(response.context['items_plan_wh']),3)
#		#check current process
#		self.assertEqual(response.context['cr'],'idle')
#		self.assertEqual(response.context['cv'],'idle')
#		self.assertEqual(response.context['cvThreeCL'],'idle')
#		self.assertEqual(response.context['cvThreeCS'], 'idle')
#		self.assertEqual(response.context['cvThreeCW'], 'idle')
#		self.assertEqual(response.context['cvTwoCS'],'idle')
#		self.assertEqual(response.context['cvTwoCL'],'idle')
#		self.assertEqual(response.context['pt'],'idle')
#		self.assertEqual(response.context['wh'],'idle')
#		
#		#test pointer
#		size = len(response.context['item_plan_cr'])
#		self.assertEqual(size,6)
#		pos = positionOfCurrentProcess("CR",currentProcess("CR")[0][0:8])
#		self.assertEqual(pos,-2)
##		startList = returnStartingPoint(pos,size)
##		self.assertEqual(startList,3)
##		endList = startList+getPCItemNum()
##		self.assertEqual(response.context['endList'],5)
##	def test_homeT102(self):
##		#test T102
##		emp = Employee(eid='T102',firstname='CR', lastname ='Prasomwong', task='CR')
##		emp.save()
##		# Test homepage for PC
##		response = self.client.get('/likitomi/home/',{'eID':'T102'})
##		self.assertEqual(response.status_code,200)
##		self.assertEqual(response.context['eID'],'T102')
##		self.assertEqual(response.context['section_title'],"Homepage for CR Login as CR Prasomwong")
##		self.assertEqual(response.context['cr'],'idle')
##	def test_homeT103(self):
##		emp = Employee(eid='T103',firstname='CV', lastname ='Prasomwong', task='CV')
##		emp.save()
##		response = self.client.get('/likitomi/home/', {'eID':'T103'})
##		self.assertEqual(response.status_code,200)
##		self.assertEqual(response.context['eID'],'T103')
##		self.assertEqual(response.context['page'],'CV')
##	def test_homeT104(self):
##		emp = Employee(eid='T104',firstname='PT', lastname ='Prasomwong', task='PT')
##		emp.save()
##		response = self.client.get('/likitomi/home/', {'eID':'T104'})
##		self.assertEqual(response.status_code,200)
##		self.assertEqual(response.context['eID'],'T104')
##		self.assertEqual(response.context['page'],'PT')
##	def test_homeT105(self):
##		emp = Employee(eid='T105',firstname='WH', lastname ='Prasomwong', task='WH')
##		emp.save()
##		response = self.client.get('/likitomi/home', {'eID':'T105'})
##		self.assertEqual(response.status_code,200)
##		self.assertEqual(response.context['eID'], 'T105')
##		self.assertEqual(response.context['page'],'WH')
		
		
