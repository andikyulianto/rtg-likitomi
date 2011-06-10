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

from weight.models import ClampliftPlan, PaperRoll, PaperHistory
from datetime import datetime
import socket

#### This part has to test manually because reading tag has to be set for testing ###
#class AssignNewTag(unittest.TestCase): # Reading tag is unknown #
#	def setUp(self):
#		self.client = Client()
#		PaperRoll.objects.create(tarid=1, paper_code="HKS231", width=56, wunit="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)

#	def tearDown(self):
#		PaperRoll.objects.filter(tarid=1).delete()
#		PaperRoll.objects.filter(tarid=2).delete()
## Write back tag ID #
#		HOST = '192.41.170.55' # CSIM network
##		HOST = '192.168.101.55' # Likitomi network
##		HOST = '192.168.1.55' # My own local network: Linksys
##		HOST = '192.168.2.88' # In Likitomi factory
#		PORT = 50007
#		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#		soc.settimeout(2)
#		soc.connect((HOST, PORT))
#		soc.send('tag.write_id(new_tag_id=112233445566778899AABBCC, tag_id=30002AAAA000000000000000)\r\n')

#	def testNewTag_min(self):
#		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '112233445566778899AABBCC'})
#		self.assertEqual(response.status_code, 302)
##		self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, 'B')
#		self.assertEqual(roll.position, 2)

#	def testNewTag_max(self):
#		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '112233445566778899AABBCC'})
#		self.assertEqual(response.status_code, 302)
##		self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, 'B')
#		self.assertEqual(roll.position, 2)

#	def testNewTag_min_nolanpos(self):
#		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '112233445566778899AABBCC'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, '')
#		self.assertEqual(roll.position, None)

#	def testNewTag_max_nolanpos(self):
#		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '112233445566778899AABBCC'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, '')
#		self.assertEqual(roll.position, None)

#class ReuseTag(unittest.TestCase): # Reading tag is '0001' #
#	def setUp(self):
#		self.client = Client()
#		PaperRoll.objects.create(tarid=1, paper_code="HKS231", width=56, wunit="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)

#	def tearDown(self):
#		PaperRoll.objects.filter(tarid=1).delete()
#		PaperRoll.objects.filter(tarid=2).delete()
## Write back tag ID #
#		HOST = '192.41.170.55' # CSIM network
##		HOST = '192.168.101.55' # Likitomi network
##		HOST = '192.168.1.55' # My own local network: Linksys
##		HOST = '192.168.2.88' # In Likitomi factory
#		PORT = 50007
#		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#		soc.settimeout(2)
#		soc.connect((HOST, PORT))
#		soc.send('tag.write_id(new_tag_id=30001AAAA000000000000000, tag_id=30002AAAA000000000000000)\r\n')

#	def testReuseTag_min(self):
#		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), False)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, 'B')
#		self.assertEqual(roll.position, 2)

#	def testReuseTag_max(self):
#		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), False)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, 'B')
#		self.assertEqual(roll.position, 2)

#	def testReuseTag_min_nolanpos(self):
#		response = self.client.get('/minclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), False)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, '')
#		self.assertEqual(roll.position, None)

#	def testReuseTag_max_nolanpos(self):
#		response = self.client.get('/maxclamp/assigntag/', {'atagid': '2', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=2).exists(), True)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), False)
#		roll = PaperRoll.objects.get(tarid=2)
#		self.assertEqual(roll.tarid, 2)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, '')
#		self.assertEqual(roll.position, None)

#class UpdateTag(unittest.TestCase): # Reading tag is '0001' #
#	def setUp(self):
#		self.client = Client()
#		PaperRoll.objects.create(tarid=1, paper_code="HKS231", width=56, wunit="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)

#	def tearDown(self):
#		PaperRoll.objects.filter(tarid=1).delete()
#		PaperRoll.objects.filter(tarid=2).delete()

#	def testUpdateTag_min(self):
#		response = self.client.get('/minclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), True)
#		roll = PaperRoll.objects.get(tarid=1)
#		self.assertEqual(roll.tarid, 1)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, 'B')
#		self.assertEqual(roll.position, 2)

#	def testUpdateTag_max(self):
#		response = self.client.get('/maxclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': 'B', 'aposition': '2', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), True)
#		roll = PaperRoll.objects.get(tarid=1)
#		self.assertEqual(roll.tarid, 1)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, 'B')
#		self.assertEqual(roll.position, 2)

#	def testUpdateTag_min_nolanpos(self):
#		response = self.client.get('/minclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), True)
#		roll = PaperRoll.objects.get(tarid=1)
#		self.assertEqual(roll.tarid, 1)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, '')
#		self.assertEqual(roll.position, None)

#	def testUpdateTag_max_nolanpos(self):
#		response = self.client.get('/maxclamp/assigntag/', {'atagid': '1', 'apcode': 'CA125', 'asize': '36', 'aweight': '800', 'alane': '', 'aposition': '', 'atag2write': '30001AAAA000000000000000'})
#		self.assertEqual(response.status_code, 302)
#		self.assertEqual(PaperRoll.objects.filter(tarid=1).exists(), True)
#		roll = PaperRoll.objects.get(tarid=1)
#		self.assertEqual(roll.tarid, 1)
#		self.assertEqual(roll.paper_code, 'CA125')
#		self.assertEqual(roll.width, 36)
#		self.assertEqual(roll.wunit, 'inch')
#		self.assertEqual(roll.initial_weight, 800)
#		self.assertEqual(roll.lane, '')
#		self.assertEqual(roll.position, None)
#### End manual test ###

class UpdateWeight(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperHistory.objects.create(roll_id=1, before_wt=1200, last_wt=600, timestamp=datetime.now())

	def tearDown(self):
		PaperHistory.objects.filter(roll_id=1).delete()

	def testUpdateWeight_min(self):
		response = self.client.get('/minclamp/update/', {'realtag': '0001', 'temp_weight': 300, 'actual_wt': 600})
		self.assertEqual(response.status_code, 302)
		phist = PaperHistory.objects.get(roll_id=1, before_wt=600, last_wt=300)
		self.assertEqual(phist.roll_id, 1)
		self.assertEqual(phist.before_wt, 600)
		self.assertEqual(phist.last_wt, 300)

	def testUpdateWeight_max(self):
		response = self.client.get('/maxclamp/update/', {'realtag': '0001', 'temp_weight': 300, 'actual_wt': 600})
		self.assertEqual(response.status_code, 302)
		phist = PaperHistory.objects.get(roll_id=1, before_wt=600, last_wt=300)
		self.assertEqual(phist.roll_id, 1)
		self.assertEqual(phist.before_wt, 600)
		self.assertEqual(phist.last_wt, 300)

class UndoWeight(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperHistory.objects.create(roll_id=1, before_wt=1200, last_wt=900, timestamp='2011-06-07 15:41:19')
		PaperHistory.objects.create(roll_id=1, before_wt=900, last_wt=600, timestamp='2011-06-08 15:41:19')
		PaperHistory.objects.create(roll_id=1, before_wt=600, last_wt=300, timestamp='2011-06-08 16:41:19')

	def tearDown(self):
		PaperRoll.objects.filter(tarid=1).delete()

	def testUndoWeight_min(self):
		t = PaperHistory.objects.filter(roll_id=1).order_by('-timestamp')[0].timestamp
		response = self.client.get('/minclamp/undo/', {'realtag': '0001'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperHistory.objects.filter(roll_id=1, timestamp=t).exists(), False)

	def testUndoWeight_max(self):
		t = PaperHistory.objects.filter(roll_id=1).order_by('-timestamp')[0].timestamp
		response = self.client.get('/maxclamp/undo/', {'realtag': '0001'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(PaperHistory.objects.filter(roll_id=1, timestamp=t).exists(), False)

class ChangeLocation(unittest.TestCase):
	def setUp(self):
		self.client = Client()
		PaperRoll.objects.create(tarid=1, paper_code="HKS231", width=56, wunit="inch", initial_weight=1200, temp_weight=600, lane="A", position=1)

	def tearDown(self):
		PaperRoll.objects.filter(tarid=1).delete()

	def testChangeLocation_min(self):
		response = self.client.get('/minclamp/changeloc/', {'realtag': '0001', 'lane': 'B', 'pos': '2'})
		self.assertEqual(response.status_code, 302)
		roll = PaperRoll.objects.get(tarid=1)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

	def testChangeLocation_max(self):
		response = self.client.get('/maxclamp/changeloc/', {'realtag': '0001', 'lane': 'B', 'pos': '2'})
		self.assertEqual(response.status_code, 302)
		roll = PaperRoll.objects.get(tarid=1)
		self.assertEqual(roll.lane, 'B')
		self.assertEqual(roll.position, 2)

class ShowPlan(unittest.TestCase):
	def setUp(self):
		self.client = Client()

	def testShowPlan(self):
		response = self.client.get('/showplan/', {'opdate': '2010-03-30'})

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

