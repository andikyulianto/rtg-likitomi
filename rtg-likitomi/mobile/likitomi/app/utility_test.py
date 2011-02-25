import unittest
#from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from utility import todayDate, currentProcess, currentTimeProcess, positionOfCurrentProcess, returnStartingPoint

class utilityTest(unittest.TestCase):
	def setUp(self):
		self.client = Client()
	def test_general(self):
		response = self.client.get('/likitomi/')
		self.assertEqual(response.status_code,200)
		self.assertEqual(response.context['title'],'Welcome to Likitomi Status Tracking System')
		self.assertEqual(response.context['subcontent_header'],"Please scan or enter employee code")
		self.failUnlessEqual(response.context['subcontent_header'],"Please scan or enter employee code")
