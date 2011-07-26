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


