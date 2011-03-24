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
from models import Employee, FakeStatusTracking

class SimpleTest(unittest.TestCase):
	def setUp(self):
		self.client = Client()
	def test_general(self):
		response = self.client.get('/likitomi/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['title'],'Welcome to Likitomi Status Tracking System')
		self.assertEqual(response.context['subcontent_header'],"Please scan or enter employee code")
		self.failUnlessEqual(response.context['subcontent_header'],"Please scan or enter employee code")
	#def test_plan(self):
		
		
	def test_homeT101(self):
		
		status = FakeStatusTracking(plan_id='1', product_id='MLT790',plan_amount='500',plan_cr_start='2010-11-19 08:00:00',plan_cr_end='2010-11-19 09:05:00',plan_cv_start='2010-11-19 09:31:00',plan_cv_end='2010-11-19 09:45:00',plan_pt_start ='2010-11-19 10:50:00', plan_pt_end='2010-11-19 10:50:00', plan_wh_start='2010-11-19 12:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='2', product_id='UTH140',plan_amount='200',plan_cr_start='2010-11-19 09:31:00', plan_cr_end='2010-11-19 09:35:00', plan_cv_start = '2010-11-19 09:50:00', plan_cv_end = '2010-11-19 10:30:00', plan_wh_start = '2010-11-19 11:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='3', product_id='UTH130',plan_amount='300',plan_cr_start='2010-11-19 09:37:00', plan_cr_end='2010-11-19 09:40:00', plan_wh_start = '2010-11-19 10:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='4', product_id='UTH120',plan_amount='100',plan_cr_start='2010-11-19 09:44:00', plan_cr_end='2010-11-19 09:50:00', plan_wh_start = '2010-11-19 10:00:00')
		status = FakeStatusTracking(plan_id='5', product_id='MOL010',plan_amount='300',plan_cr_start='2010-11-19 09:51:00', plan_cr_end='2010-11-19 10:10:00', plan_wh_start = '2010-11-19 11:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='6', product_id='ANU010',plan_amount='1300',plan_cr_start='2010-11-19 09:05:00', plan_cr_end='2010-11-19 09:40:00', plan_cv_start = '2010-11-19 09:40:00', plan_cv_end = '2010-11-19 10:30:00',plan_pt_start='2010-11-19 10:45:00',plan_pt_end='2010-11-19 11:30:00', plan_wh_start = '2010-11-19 12:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='7', product_id='AAA010',plan_amount='1300',plan_cr_start='2010-11-18 08:00:00', plan_cr_end='2010-11-18 09:00:00', plan_cv_start = '2010-11-19 09:00:00', plan_cv_end = '2010-11-19 09:25:00',plan_pt_start='2010-11-19 09:30:00',plan_pt_end='2010-11-19 10:00:00', plan_wh_start = '2010-11-19 10:30:00')
		status.save()
		status = FakeStatusTracking(plan_id='8', product_id='GNG100',plan_amount='600',plan_cr_start='2010-11-18 10:00:00', plan_cr_end='2010-11-18 10:30:00', plan_cv_start = '2010-11-19 09:33:00', plan_cv_end = '2010-11-19 10:30:00', plan_wh_start = '2010-11-19 13:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='9', product_id='ADL090',plan_amount='400',plan_cr_start='2010-11-18 11:00:00', plan_cr_end='2010-11-18 11:40:00', plan_cv_start = '2010-11-19 11:00:00', plan_cv_end = '2010-11-19 12:30:00', plan_wh_start = '2010-11-19 13:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='10', product_id='KFC010',plan_amount='400',plan_cr_start='2010-11-18 13:00:00', plan_cr_end='2010-11-18 13:30:00', plan_cv_start = '2010-11-18 14:00:00', plan_cv_end = '2010-11-18 14:30:00',plan_pt_start='2010-11-19 08:00:00',plan_pt_end='2010-11-19 08:50:00', plan_wh_start = '2010-11-19 09:00:00')
		status.save()
		status = FakeStatusTracking(plan_id='11', product_id='SHG700',plan_amount='900',plan_cr_start='2010-11-18 15:00:00', plan_cr_end='2010-11-18 15:30:00', plan_cv_start = '2010-11-18 15:45:00', plan_cv_end = '2010-11-18 16:00:00',plan_pt_start='2010-11-19 09:00:00',plan_pt_end='2010-11-19 09:30:00', plan_wh_start = '2010-11-19 10:00:00')
		status.save()
		
		# test T101 login
		emp = Employee(eid='T101',firstname='Fon', lastname ='Prasomwong', task='PC')
		emp.save()
		# Test homepage for PC
		response = self.client.get('/likitomi/home/',{'eID':'T101'})
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['eID'],'T101')
		self.assertEqual(response.context['section_title'],"Homepage for PC Login as Fon Prasomwong")
		#Test queries and items
		self.assertEqual(len(response.context['item_plan_cr']),6)
		self.assertEqual(len(response.context['items_plan_cr']),3)
		self.assertEqual(len(response.context['items_plan_cv']),3)
		self.assertEqual(len(response.context['items_plan_pt']),3)
		self.assertEqual(len(response.context['items_plan_wh']),3)
#	def test_homeT102(self):
#		#test T102
#		emp = Employee(eid='T102',firstname='CR', lastname ='Prasomwong', task='CR')
#		emp.save()
#		response = self.client.get('/likitomi/home/',{'eID':'T102'})
#		self.assertEqual(response.status_code,200)
#		self.assertEqual(response.context['eID'],'T102')
#		self.assertEqual(response.context['page'],'CR')
#	def test_homeT103(self):
#		emp = Employee(eid='T103',firstname='CV', lastname ='Prasomwong', task='CV')
#		emp.save()
#		response = self.client.get('/likitomi/home/', {'eID':'T103'})
#		self.assertEqual(response.status_code,200)
#		self.assertEqual(response.context['eID'],'T103')
#		self.assertEqual(response.context['page'],'CV')
#	def test_homeT104(self):
#		emp = Employee(eid='T104',firstname='PT', lastname ='Prasomwong', task='PT')
#		emp.save()
#		response = self.client.get('/likitomi/home/', {'eID':'T104'})
#		self.assertEqual(response.status_code,200)
#		self.assertEqual(response.context['eID'],'T104')
#		self.assertEqual(response.context['page'],'PT')
#	def test_homeT105(self):
#		emp = Employee(eid='T105',firstname='WH', lastname ='Prasomwong', task='WH')
#		emp.save()
#		response = self.client.get('/likitomi/home', {'eID':'T105'})
#		self.assertEqual(response.status_code,200)
#		self.assertEqual(response.context['eID'], 'T105')
#		self.assertEqual(response.context['page'],'WH')
		
