"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

from django.utils import unittest # Changed in Django 1.3
#import unittest # Historically used
from django.test.client import Client
#from django.test.utils import setup_test_environment, teardown_test_environment

import serial
import socket
from datetime import datetime
from time import sleep
from weight.models import TblClamplift, PaperRolldetails, PaperMovement

### This part involves writing tag so unpredictable errors or failures may occur ###
class Scale(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperRolldetails.objects.create(paper_roll_detail_id=1, paper_code="HKS231", size=56, uom="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)
		try:
# Write tag ID to unknown #
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=30001AAAA000000000000000)\r\n')
			response = soc.recv(128)
			if response.find('ok') != -1:
				pass
			else:
				print '\nWriteTagError'
			soc.close()
		except socket.timeout:
			print '\nRFIDConnectionError'

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=1).delete()
		try:
# Write back tag ID #
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=112233445566778899AABBCC, tag_id=30001AAAA000000000000000)\r\n')
			response = soc.recv(128)
			if response.find('ok') != -1:
				pass
			else:
				print '\nWriteBackError'
			soc.close()
		except socket.timeout:
			print '\nRFIDConnectionError'
		sleep(2)

	def testScale(self):
		response = self.client.get('/scale/')
		self.assertEqual(response.status_code, 200)
		realtag = response.context['realtag']
		weight = response.context['weight']
		temp_weight = PaperRolldetails.objects.get(paper_roll_detail_id=realtag).temp_weight
		self.assertEqual(weight, temp_weight)
#		print str(weight)+" = "+str(temp_weight)

class AssignNewTag(unittest.TestCase): # Reading tag is unknown #
	def setUp(self):
		self.client = Client()
		PaperRolldetails.objects.create(paper_roll_detail_id=1, paper_code="HKS231", size=56, uom="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)
		try:
# Write tag ID to unknown #
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=112233445566778899AABBCC)\r\n')
			response = soc.recv(128)
			if response.find('ok') != -1:
				pass
			else:
				print '\nWriteTagError'
			soc.close()
		except socket.timeout:
			print '\nRFIDConnectionError'

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=1).delete()
		PaperRolldetails.objects.filter(paper_roll_detail_id=2).delete()
		try:
# Write back tag ID #
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=112233445566778899AABBCC, tag_id=30002AAAA000000000000000)\r\n')
			response = soc.recv(128)
			if response.find('ok') != -1:
				pass
			else:
				print '\nWriteBackError'
			soc.close()
		except socket.timeout:
			print '\nRFIDConnectionError'
		sleep(2)

	def testNewTag_min(self):
		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '112233445566778899AABBCC'})
		self.assertEqual(response.status_code, 302)
#		self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testNewTag_max(self):
		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '112233445566778899AABBCC'})
		self.assertEqual(response.status_code, 302)
#		self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testNewTag_min_nolanpos(self):
		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '112233445566778899AABBCC'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, '')
		self.assertEqual(roll.position, None)

	def testNewTag_max_nolanpos(self):
		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '112233445566778899AABBCC'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, '')
		self.assertEqual(roll.position, None)

class ReuseTag(unittest.TestCase): # Reading tag is '0001' #
	def setUp(self):
		self.client = Client()
		PaperRolldetails.objects.create(paper_roll_detail_id=1, paper_code="HKS231", size=56, uom="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)
		try:
# Write tag ID to '0001' #
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=30001AAAA000000000000000)\r\n')
			response = soc.recv(128)
			if response.find('ok') != -1:
				pass
			else:
				print '\nWriteTagError'
			soc.close()
		except socket.timeout:
			print '\nRFIDConnectionError'

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=1).delete()
		PaperRolldetails.objects.filter(paper_roll_detail_id=2).delete()
		try:
# Write back tag ID #
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=112233445566778899AABBCC, tag_id=30002AAAA000000000000000)\r\n')
			response = soc.recv(128)
			if response.find('ok') != -1:
				pass
			else:
				print '\nWriteBackError'
			soc.close()
		except socket.timeout:
			print '\nRFIDConnectionError'
		sleep(2)

	def testReuseTag_min(self):
		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), False)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testReuseTag_max(self):
		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), False)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testReuseTag_min_nolanpos(self):
		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), False)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, '')
		self.assertEqual(roll.position, None)

	def testReuseTag_max_nolanpos(self):
		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=2).exists(), True)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), False)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=2)
		self.assertEqual(roll.paper_roll_detail_id, 2)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, '')
		self.assertEqual(roll.position, None)

class UpdateTag(unittest.TestCase): # Reading tag is '0001' #
	def setUp(self):
		self.client = Client()
		PaperRolldetails.objects.create(paper_roll_detail_id=1, paper_code="HKS231", size=56, uom="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=1).delete()
		PaperRolldetails.objects.filter(paper_roll_detail_id=2).delete()

	def testUpdateTag_min(self):
		response = self.client.get('/minclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=1)
		self.assertEqual(roll.paper_roll_detail_id, 1)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testUpdateTag_max(self):
		response = self.client.get('/maxclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=1)
		self.assertEqual(roll.paper_roll_detail_id, 1)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testUpdateTag_min_nolanpos(self):
		response = self.client.get('/minclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=1)
		self.assertEqual(roll.paper_roll_detail_id, 1)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, '')
		self.assertEqual(roll.position, None)

	def testUpdateTag_max_nolanpos(self):
		response = self.client.get('/maxclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperRolldetails.objects.filter(paper_roll_detail_id=1).exists(), True)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=1)
		self.assertEqual(roll.paper_roll_detail_id, 1)
		self.assertEqual(roll.paper_code, 'CA125')
		self.assertEqual(roll.size, 36)
		self.assertEqual(roll.uom, 'inch')
		self.assertEqual(roll.initial_weight, 800)
		self.assertEqual(roll.lane, '')
		self.assertEqual(roll.position, None)
### End tag-involved part ###

class UpdateWeight(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperMovement.objects.create(roll_id=1, before_wt=1200, actual_wt=600, created_on=datetime.now())

	def tearDown(self):
		PaperMovement.objects.filter(roll_id=1).delete()

	def testUpdateWeight_min(self):
		response = self.client.get('/minclamp/update/', {'realtag': '0001', 'temp_weight': 300, 'actual_wt': 600})
		self.assertEqual(response.status_code, 302)
		phist = PaperMovement.objects.get(roll_id=1, before_wt=600, actual_wt=300)
		self.assertEqual(phist.roll_id, 1)
		self.assertEqual(phist.before_wt, 600)
		self.assertEqual(phist.actual_wt, 300)

	def testUpdateWeight_max(self):
		response = self.client.get('/maxclamp/update/', {'realtag': '0001', 'temp_weight': 300, 'actual_wt': 600})
		self.assertEqual(response.status_code, 302)
		phist = PaperMovement.objects.get(roll_id=1, before_wt=600, actual_wt=300)
		self.assertEqual(phist.roll_id, 1)
		self.assertEqual(phist.before_wt, 600)
		self.assertEqual(phist.actual_wt, 300)

class UndoWeight(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperMovement.objects.create(roll_id=1, before_wt=1200, actual_wt=900, created_on='2011-06-07 15:41:19')
		PaperMovement.objects.create(roll_id=1, before_wt=900, actual_wt=600, created_on='2011-06-08 15:41:19')
		PaperMovement.objects.create(roll_id=1, before_wt=600, actual_wt=300, created_on='2011-06-08 16:41:19')

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=1).delete()

	def testUndoWeight_min(self):
		t = PaperMovement.objects.filter(roll_id=1).order_by('-created_on')[0].created_on
		response = self.client.get('/minclamp/undo/', {'realtag': '0001'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperMovement.objects.filter(roll_id=1, created_on=t).exists(), False)

	def testUndoWeight_max(self):
		t = PaperMovement.objects.filter(roll_id=1).order_by('-created_on')[0].created_on
		response = self.client.get('/maxclamp/undo/', {'realtag': '0001'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperMovement.objects.filter(roll_id=1, created_on=t).exists(), False)

class ChangeLocation(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperRolldetails.objects.create(paper_roll_detail_id=1, paper_code="HKS231", size=56, uom="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=1).delete()

	def testChangeLocation_min(self):
		response = self.client.get('/minclamp/changeloc/', {'realtag': '0001', 'lane': 'B', 'pos': '2'})
		self.assertEqual(response.status_code, 302)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=1)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testChangeLocation_max(self):
		response = self.client.get('/maxclamp/changeloc/', {'realtag': '0001', 'lane': 'B', 'pos': '2'})
		self.assertEqual(response.status_code, 302)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=1)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

class ShowPlan(unittest.TestCase):
	def setUp(self):
		self.client = Client()

	def testShowPlan(self):
		response = self.client.get('/showplan/', {'opdate': '2010-03-30'})
		self.assertEqual(response.status_code, 200)
#		self.assertTemplateUsed(response, 'showplan.html')
		self.assertEqual(response.context['opdate'],'2010-03-30')

	def testRequiredPlan(self):
		response = self.client.get('/required/', {'opdate': '2010-03-30'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['opdate'],'2010-03-30')

	def testDetailPlan(self):
		response = self.client.get('/detail/', {'opdate': '2010-03-30'})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['opdate'],'2010-03-30')

class Inventory(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperRolldetails.objects.create(paper_roll_detail_id=67, paper_code="CA125", size=56, uom="inch", initial_weight=1200, temp_weight=600, lane="A", position=3)

	def tearDown(self):
		PaperRolldetails.objects.filter(paper_roll_detail_id=67).delete()

	def testNormalInventory(self):
		response = self.client.get('/inventory/', {'pcode': 'HKS231', 'width': '56', 'loss': '529', 'lossarr': '529,529', 'spcode': 'HCM97', 'swidth': '54', 'cpcode': 'CA125', 'cwidth': '56', 'lane': 'A', 'position': '3', 'atlane': '1', 'atposition': '13', 'clamping': 'no', 'changed': 'no', 'realtag': '0067', 'loc': '',})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['pcode'],'HKS231')
		self.assertEqual(response.context['width'],'56')
		self.assertEqual(response.context['loss'],'529')
		self.assertEqual(response.context['lossarr'],'529,529')
		self.assertEqual(response.context['spcode'],'HCM97')
		self.assertEqual(response.context['swidth'],'54')
		self.assertEqual(response.context['cpcode'],'CA125')
		self.assertEqual(response.context['cwidth'],'56')
		self.assertEqual(response.context['lane'],'A')
		self.assertEqual(response.context['position'],'3')
		self.assertEqual(response.context['atlane'],'1')
		self.assertEqual(response.context['atposition'],'13')
		self.assertEqual(response.context['clamping'],'no')
		self.assertEqual(response.context['changed'],'no')
		self.assertEqual(response.context['realtag'],'0067')
		self.assertEqual(response.context['loc'],'')

	def testClamping(self):
		response = self.client.get('/inventory/', {'pcode': 'HKS231', 'width': '56', 'loss': '529', 'lossarr': '529,529', 'spcode': 'HCM97', 'swidth': '54', 'cpcode': 'CA125', 'cwidth': '56', 'lane': 'A', 'position': '3', 'atlane': '1', 'atposition': '13', 'clamping': 'yes', 'changed': 'no', 'realtag': '0067', 'loc': '',})
		self.assertEqual(response.status_code, 200)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=67)
		self.assertEqual(roll.lane, '1')
		self.assertEqual(roll.position, 13)
		self.assertEqual(response.context['pcode'],'HKS231')
		self.assertEqual(response.context['width'],'56')
		self.assertEqual(response.context['loss'],'529')
		self.assertEqual(response.context['lossarr'],'529,529')
		self.assertEqual(response.context['spcode'],'HCM97')
		self.assertEqual(response.context['swidth'],'54')
		self.assertEqual(response.context['cpcode'],'CA125')
		self.assertEqual(response.context['cwidth'],'56')
		self.assertEqual(response.context['lane'],'A')
		self.assertEqual(response.context['position'],'3')
		self.assertEqual(response.context['atlane'],'1')
		self.assertEqual(response.context['atposition'],'13')
		self.assertEqual(response.context['clamping'],'yes')
		self.assertEqual(response.context['changed'],'no')
		self.assertEqual(response.context['realtag'],'0067')
		self.assertEqual(response.context['loc'],'')

	def testLocUp(self):
		response = self.client.get('/inventory/', {'pcode': 'HKS231', 'width': '56', 'loss': '529', 'lossarr': '529,529', 'spcode': 'HCM97', 'swidth': '54', 'cpcode': 'CA125', 'cwidth': '56', 'lane': 'A', 'position': '3', 'atlane': '1', 'atposition': '13', 'clamping': 'no', 'changed': 'no', 'realtag': '0067', 'loc': 'up',})
		self.assertEqual(response.status_code, 200)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=67)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 13)
		self.assertEqual(response.context['pcode'],'HKS231')
		self.assertEqual(response.context['width'],'56')
		self.assertEqual(response.context['loss'],'529')
		self.assertEqual(response.context['lossarr'],'529,529')
		self.assertEqual(response.context['spcode'],'HCM97')
		self.assertEqual(response.context['swidth'],'54')
		self.assertEqual(response.context['cpcode'],'CA125')
		self.assertEqual(response.context['cwidth'],'56')
		self.assertEqual(response.context['lane'],'A')
		self.assertEqual(response.context['position'],'3')
		self.assertEqual(response.context['atlane'],'1')
		self.assertEqual(response.context['atposition'],'13')
		self.assertEqual(response.context['clamping'],'no')
		self.assertEqual(response.context['changed'],'no')
		self.assertEqual(response.context['realtag'],'0067')
		self.assertEqual(response.context['loc'],'up')

	def testLocDown(self):
		response = self.client.get('/inventory/', {'pcode': 'HKS231', 'width': '56', 'loss': '529', 'lossarr': '529,529', 'spcode': 'HCM97', 'swidth': '54', 'cpcode': 'CA125', 'cwidth': '56', 'lane': 'A', 'position': '3', 'atlane': '1', 'atposition': '13', 'clamping': 'no', 'changed': 'no', 'realtag': '0067', 'loc': 'down',})
		self.assertEqual(response.status_code, 200)
		roll = PaperRolldetails.objects.get(paper_roll_detail_id=67)
		self.assertEqual(roll.lane, 'A')
		self.assertEqual(roll.position, 13)
		self.assertEqual(response.context['pcode'],'HKS231')
		self.assertEqual(response.context['width'],'56')
		self.assertEqual(response.context['loss'],'529')
		self.assertEqual(response.context['lossarr'],'529,529')
		self.assertEqual(response.context['spcode'],'HCM97')
		self.assertEqual(response.context['swidth'],'54')
		self.assertEqual(response.context['cpcode'],'CA125')
		self.assertEqual(response.context['cwidth'],'56')
		self.assertEqual(response.context['lane'],'A')
		self.assertEqual(response.context['position'],'3')
		self.assertEqual(response.context['atlane'],'1')
		self.assertEqual(response.context['atposition'],'13')
		self.assertEqual(response.context['clamping'],'no')
		self.assertEqual(response.context['changed'],'no')
		self.assertEqual(response.context['realtag'],'0067')
		self.assertEqual(response.context['loc'],'down')



#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.failUnlessEqual(1 + 1, 2)

#__test__ = {"doctest": """
#Another way to test that 1 + 1 is equal to 2.

#>>> 1 + 1 == 2

#True
#"""}

