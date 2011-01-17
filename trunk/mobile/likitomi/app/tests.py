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
from models import Employee

class SimpleTest(unittest.TestCase):
	def setUp(self):
		self.client = Client()
	def test_general(self):
		response = self.client.get('/likitomi/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['title'],'Welcome to Likitomi Status Tracking System')
		self.assertEqual(response.context['subcontent_header'],"Please scan or enter employee code")
		self.failUnlessEqual(response.context['subcontent_header'],"Please scan or enter employee code")
	def test_homeT101(self):
		# test T101
		emp = Employee(eid='T101',firstname='Fon', lastname ='Prasomwong', task='PC')
		emp.save()
		response = self.client.get('/likitomi/home/',{'eID':'T101'})
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['eID'],'T101')
		self.assertEqual(response.context['page'],'PC')
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
		
