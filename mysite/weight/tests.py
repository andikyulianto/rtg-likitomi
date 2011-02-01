"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

    def test_index(self):
        response = self.client.get('/index/')
        # self.failUnlessEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.template.name, 'index.html')
        self.assertTemplateUsed(response, 'index.html')
        # self.assertContains(response, 'Likitomi', count=2, status_code=200)
        # self.assertNotContains(response, 'Likitomi', status_code=200)

    def test_scale(self):
        response = self.client.get('/scale/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scale.html')

    def test_clamplift(self):
        response = self.client.get('/clamplift/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clamplift.html')

    def test_clamplift_update(self):
        response = self.client.get('/clamplift/update/')
        self.assertRedirects(response, '/clamplift/', status_code=302, target_status_code=200)

    def test_clamplift_undo(self):
        response = self.client.get('/clamplift/undo/')
        self.assertRedirects(response, '/clamplift/', status_code=302, target_status_code=200)

    def test_clamplift_changeloc(self):
        response = self.client.get('/clamplift/changeloc/')
        self.assertRedirects(response, '/clamplift/', status_code=302, target_status_code=200)

    def test_minclamp(self):
        response = self.client.get('/minclamp/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minclamp.html')

    def test_minclamp_update(self):
        response = self.client.get('/minclamp/update/')
        self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)

    def test_minclamp_undo(self):
        response = self.client.get('/minclamp/undo/')
        self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)

    def test_minclamp_changeloc(self):
        response = self.client.get('/minclamp/changeloc/')
        self.assertRedirects(response, '/minclamp/', status_code=302, target_status_code=200)

    def test_now(self):
        response = self.client.get('/now/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'now.html')

    def test_plan(self):
        response = self.client.get('/plan/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'plan.html')
        today = datetime.datetime.now().strftime("%Y-%m-%d")
#        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.assertContains(response, today, status_code=200)
#        self.assertContains(response, now, status_code=200)
        self.assertContains(response, 'TIME', status_code=200)
        self.assertContains(response, 'SHEET CODE', status_code=200)
        self.assertContains(response, 'SIZE', status_code=200)
        self.assertContains(response, 'DF', status_code=200)
        self.assertContains(response, 'BL', status_code=200)
        self.assertContains(response, 'BM', status_code=200)
        self.assertContains(response, 'CL', status_code=200)
        self.assertContains(response, 'CM', status_code=200)

#### Show Plan ####

    def test_showplan_2010_3_30(self):
        response = self.client.get('/showplan/', {'opdate':'2010-3-30'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2010-3-30')
        self.assertTemplateUsed(response, 'showplan.html')

    def test_showplan_2008_7_2(self):
        response = self.client.get('/showplan/', {'opdate':'2008-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-2')
        self.assertTemplateUsed(response, 'showplan.html')

    def test_showplan_2008_7_1(self):
        response = self.client.get('/showplan/', {'opdate':'2008-7-1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-1')
        self.assertTemplateUsed(response, 'showplan.html')

    def test_showplan_2007_7_2(self):
        response = self.client.get('/showplan/', {'opdate':'2007-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2007-7-2')
        self.assertTemplateUsed(response, 'showplan.html')

########

    def test_wholeplan(self):
        response = self.client.get('/wholeplan/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wholeplan.html')

    def test_showreq(self):
        response = self.client.get('/showreq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showreq.html')

#### ReqHead ####

    def test_reqhead_2010_3_30(self):
        response = self.client.get('/reqhead/', {'opdate':'2010-3-30'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2010-3-30')
        self.assertTemplateUsed(response, 'reqhead.html')

    def test_reqhead_2008_7_2(self):
        response = self.client.get('/reqhead/', {'opdate':'2008-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-2')
        self.assertTemplateUsed(response, 'reqhead.html')

    def test_reqhead_2008_7_1(self):
        response = self.client.get('/reqhead/', {'opdate':'2008-7-1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-1')
        self.assertTemplateUsed(response, 'reqhead.html')

    def test_reqhead_2007_7_2(self):
        response = self.client.get('/reqhead/', {'opdate':'2007-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2007-7-2')
        self.assertTemplateUsed(response, 'reqhead.html')

#### Required ####

    def test_required_2010_3_30(self):
        response = self.client.get('/required/', {'opdate':'2010-3-30'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2010-3-30')
        self.assertTemplateUsed(response, 'required.html')

    def test_required_2008_7_2(self):
        response = self.client.get('/required/', {'opdate':'2008-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-2')
        self.assertTemplateUsed(response, 'required.html')

    def test_required_2008_7_1(self):
        response = self.client.get('/required/', {'opdate':'2008-7-1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-1')
        self.assertTemplateUsed(response, 'required.html')

    def test_required_2007_7_2(self):
        response = self.client.get('/required/', {'opdate':'2007-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2007-7-2')
        self.assertTemplateUsed(response, 'required.html')

########

    def test_showdet(self):
        response = self.client.get('/showdet/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showdet.html')

#### DetHead ####

    def test_dethead_2010_3_30(self):
        response = self.client.get('/dethead/', {'opdate':'2010-3-30'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2010-3-30')
        self.assertTemplateUsed(response, 'dethead.html')

    def test_dethead_2008_7_2(self):
        response = self.client.get('/dethead/', {'opdate':'2008-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-2')
        self.assertTemplateUsed(response, 'dethead.html')

    def test_dethead_2008_7_1(self):
        response = self.client.get('/dethead/', {'opdate':'2008-7-1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-1')
        self.assertTemplateUsed(response, 'dethead.html')

    def test_dethead_2007_7_2(self):
        response = self.client.get('/dethead/', {'opdate':'2007-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2007-7-2')
        self.assertTemplateUsed(response, 'dethead.html')

#### Detail ####

    def test_detail_2010_3_30(self):
        response = self.client.get('/detail/', {'opdate':'2010-3-30'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2010-3-30')
        self.assertTemplateUsed(response, 'detail.html')

    def test_detail_2008_7_2(self):
        response = self.client.get('/detail/', {'opdate':'2008-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-2')
        self.assertTemplateUsed(response, 'detail.html')

    def test_detail_2008_7_1(self):
        response = self.client.get('/detail/', {'opdate':'2008-7-1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2008-7-1')
        self.assertTemplateUsed(response, 'detail.html')

    def test_detail_2007_7_2(self):
        response = self.client.get('/detail/', {'opdate':'2007-7-2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2007-7-2')
        self.assertTemplateUsed(response, 'detail.html')

########

    def test_stock(self):
        response = self.client.get('/stock/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock.html')

#### Inventory #### 2010-3-30

    def test_inventory_CA125_56_286(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':56, 'loss':286})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '286')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_56_413(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':56, 'loss':413})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '413')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKS231_56_529(self):
        response = self.client.get('/inventory/', {'pcode':'HKS231', 'width':56, 'loss':529})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS231')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '529')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_56_424(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':56, 'loss':424})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '424')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_HCM97_54_293(self):
        response = self.client.get('/inventory/', {'pcode':'HCM97', 'width':54, 'loss':293})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM97')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '293')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM97_54_422(self):
        response = self.client.get('/inventory/', {'pcode':'HCM97', 'width':54, 'loss':422})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM97')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '422')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKS161_54_421(self):
        response = self.client.get('/inventory/', {'pcode':'HKS161', 'width':54, 'loss':421})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS161')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '421')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM147_54_419(self):
        response = self.client.get('/inventory/', {'pcode':'HCM147', 'width':54, 'loss':419})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM147')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '419')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM112_54_434(self):
        response = self.client.get('/inventory/', {'pcode':'HCM112', 'width':54, 'loss':434})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM112')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '434')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_HKI158_36_65(self):
        response = self.client.get('/inventory/', {'pcode':'HKI158', 'width':36, 'loss':65})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKI158')
        self.assertEqual(response.context['width'], '36')
        self.assertEqual(response.context['loss'], '65')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKI128_36_53(self):
        response = self.client.get('/inventory/', {'pcode':'HKI128', 'width':36, 'loss':53})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKI128')
        self.assertEqual(response.context['width'], '36')
        self.assertEqual(response.context['loss'], '53')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM112_36_68(self):
        response = self.client.get('/inventory/', {'pcode':'HCM112', 'width':36, 'loss':68})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM112')
        self.assertEqual(response.context['width'], '36')
        self.assertEqual(response.context['loss'], '68')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_PKL205_42_333(self):
        response = self.client.get('/inventory/', {'pcode':'PKL205', 'width':42, 'loss':333})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'PKL205')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '333')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM147_42_333(self):
        response = self.client.get('/inventory/', {'pcode':'HCM147', 'width':42, 'loss':333})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM147')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '333')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_TKA230_70_149(self):
        response = self.client.get('/inventory/', {'pcode':'TKA230', 'width':70, 'loss':149})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'TKA230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '149')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_120(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':120})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '120')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_EKB230_64_3347(self):
        response = self.client.get('/inventory/', {'pcode':'EKB230', 'width':64, 'loss':3347})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'EKB230')
        self.assertEqual(response.context['width'], '64')
        self.assertEqual(response.context['loss'], '3347')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM190_64_2765(self):
        response = self.client.get('/inventory/', {'pcode':'HCM190', 'width':64, 'loss':2765})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM190')
        self.assertEqual(response.context['width'], '64')
        self.assertEqual(response.context['loss'], '2765')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM190_64_4093(self):
        response = self.client.get('/inventory/', {'pcode':'HCM190', 'width':64, 'loss':4093})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM190')
        self.assertEqual(response.context['width'], '64')
        self.assertEqual(response.context['loss'], '4093')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_HKS161_56_132(self):
        response = self.client.get('/inventory/', {'pcode':'HKS161', 'width':56, 'loss':132})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS161')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '132')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM147_56_132(self):
        response = self.client.get('/inventory/', {'pcode':'HKS147', 'width':56, 'loss':132})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS147')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '132')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA112_56_136(self):
        response = self.client.get('/inventory/', {'pcode':'ECA112', 'width':56, 'loss':136})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA112')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '136')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_EII150_54_208(self):
        response = self.client.get('/inventory/', {'pcode':'EII150', 'width':54, 'loss':208})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'EII150')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '208')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_54_256(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':54, 'loss':256})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '256')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_EII185_54_639(self):
        response = self.client.get('/inventory/', {'pcode':'EII185', 'width':54, 'loss':639})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'EII185')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '639')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_54_639(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':54, 'loss':639})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '54')
        self.assertEqual(response.context['loss'], '639')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_HKB230_44_3267(self):
        response = self.client.get('/inventory/', {'pcode':'HKB230', 'width':44, 'loss':3267})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKB230')
        self.assertEqual(response.context['width'], '44')
        self.assertEqual(response.context['loss'], '3267')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA150_44_2273(self):
        response = self.client.get('/inventory/', {'pcode':'ECA150', 'width':44, 'loss':2273})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA150')
        self.assertEqual(response.context['width'], '44')
        self.assertEqual(response.context['loss'], '2273')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM147_44_3091(self):
        response = self.client.get('/inventory/', {'pcode':'HCM147', 'width':44, 'loss':3091})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM147')
        self.assertEqual(response.context['width'], '44')
        self.assertEqual(response.context['loss'], '3091')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_EKC125_44_34(self):
        response = self.client.get('/inventory/', {'pcode':'EKC125', 'width':44, 'loss':34})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'EKC125')
        self.assertEqual(response.context['width'], '44')
        self.assertEqual(response.context['loss'], '34')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_44_51(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':44, 'loss':51})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '44')
        self.assertEqual(response.context['loss'], '51')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_EII150_42_474(self):
        response = self.client.get('/inventory/', {'pcode':'EII150', 'width':42, 'loss':474})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'EII150')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '474')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_42_585(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':42, 'loss':585})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '585')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_ECA112_70_56(self):
        response = self.client.get('/inventory/', {'pcode':'ECA112', 'width':70, 'loss':56})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA112')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '56')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA112_70_81(self):
        response = self.client.get('/inventory/', {'pcode':'ECA112', 'width':70, 'loss':81})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA112')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '81')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_EII150_70_75(self):
        response = self.client.get('/inventory/', {'pcode':'EII150', 'width':70, 'loss':75})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'EII150')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '75')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA150_70_81(self):
        response = self.client.get('/inventory/', {'pcode':'ECA150', 'width':70, 'loss':81})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA150')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '81')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA112_70_83(self):
        response = self.client.get('/inventory/', {'pcode':'ECA112', 'width':70, 'loss':83})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA112')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '83')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_CA125_70_525(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':525})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '525')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_757(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':757})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '757')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKB230_70_967(self):
        response = self.client.get('/inventory/', {'pcode':'HKB230', 'width':70, 'loss':967})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKB230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '967')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA230_70_967(self):
        response = self.client.get('/inventory/', {'pcode':'ECA230', 'width':70, 'loss':967})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '967')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_778(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':778})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '778')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_CA125_70_273(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':273})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '273')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_393(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':393})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '393')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKB230_70_502(self):
        response = self.client.get('/inventory/', {'pcode':'HKB230', 'width':70, 'loss':502})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKB230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '502')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA230_70_502(self):
        response = self.client.get('/inventory/', {'pcode':'ECA230', 'width':70, 'loss':502})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '502')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_404(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':404})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '404')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_CA125_70_555(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':555})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '555')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_799(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':799})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '799')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKB230_70_1021(self):
        response = self.client.get('/inventory/', {'pcode':'HKB230', 'width':70, 'loss':1021})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKB230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '1021')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_ECA230_70_1021(self):
        response = self.client.get('/inventory/', {'pcode':'ECA230', 'width':70, 'loss':1021})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'ECA230')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '1021')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_70_821(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':70, 'loss':821})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '70')
        self.assertEqual(response.context['loss'], '821')
        self.assertTemplateUsed(response, 'inventory.html')

#### Inventory #### 2008-7-2

    def test_inventory_CA125_56_385(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':56, 'loss':385})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '385')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_56_554(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':56, 'loss':554})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '554')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_TKA185_56_569(self):
        response = self.client.get('/inventory/', {'pcode':'TKA185', 'width':56, 'loss':569})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'TKA185')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '569')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HAC185_56_569(self):
        response = self.client.get('/inventory/', {'pcode':'HAC185', 'width':56, 'loss':569})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HAC185')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '569')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_56_569(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':56, 'loss':569})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '56')
        self.assertEqual(response.context['loss'], '569')
        self.assertTemplateUsed(response, 'inventory.html')

#### Inventory #### 2008-7-1

    def test_inventory_CA125_40_79(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':79})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '79')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_40_114(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':114})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '114')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HAC155_40_98(self):
        response = self.client.get('/inventory/', {'pcode':'HAC155', 'width':40, 'loss':98})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HAC155')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '98')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HCM147_40_93(self):
        response = self.client.get('/inventory/', {'pcode':'HCM147', 'width':40, 'loss':93})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HCM147')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '93')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_40_117(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':117})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '117')
        self.assertTemplateUsed(response, 'inventory.html')

#### Inventory #### 2007-7-2

    def test_inventory_PKL175_48_502(self):
        response = self.client.get('/inventory/', {'pcode':'PKL175', 'width':48, 'loss':502})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'PKL175')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '502')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_48_516(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':48, 'loss':516})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '516')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_PKL250_48_716(self):
        response = self.client.get('/inventory/', {'pcode':'PKL250', 'width':48, 'loss':716})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'PKL250')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '716')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_48_530(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':48, 'loss':530})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '530')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_CA125_48_142(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':48, 'loss':142})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '142')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_48_204(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':48, 'loss':204})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '204')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKS121_48_137(self):
        response = self.client.get('/inventory/', {'pcode':'HKS121', 'width':48, 'loss':137})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS121')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '137')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_HKB120_48_136(self):
        response = self.client.get('/inventory/', {'pcode':'HKB120', 'width':48, 'loss':136})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKB120')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '136')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_48_210(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':48, 'loss':210})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '48')
        self.assertEqual(response.context['loss'], '210')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_PKL175_46_395(self):
        response = self.client.get('/inventory/', {'pcode':'PKL175', 'width':46, 'loss':395})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'PKL175')
        self.assertEqual(response.context['width'], '46')
        self.assertEqual(response.context['loss'], '395')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_46_406(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':46, 'loss':406})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '46')
        self.assertEqual(response.context['loss'], '406')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_PKL250_46_564(self):
        response = self.client.get('/inventory/', {'pcode':'PKL250', 'width':46, 'loss':564})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'PKL250')
        self.assertEqual(response.context['width'], '46')
        self.assertEqual(response.context['loss'], '564')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_46_417(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':46, 'loss':417})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '46')
        self.assertEqual(response.context['loss'], '417')
        self.assertTemplateUsed(response, 'inventory.html')

########

    def test_inventory_CA125_40_299(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':299})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '299')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_40_430(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':430})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '430')

    def test_inventory_PKL205_40_490(self):
        response = self.client.get('/inventory/', {'pcode':'PKL205', 'width':40, 'loss':490})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'PKL205')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '490')
        self.assertTemplateUsed(response, 'inventory.html')

    def test_inventory_CA125_40_442(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':442})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '442')

########

    def test_inventory_HKI188_58_1117(self):
        response = self.client.get('/inventory/', {'pcode':'HKI188', 'width':58, 'loss':1117})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKI188')
        self.assertEqual(response.context['width'], '58')
        self.assertEqual(response.context['loss'], '1117')

    def test_inventory_HKI128_58_760(self):
        response = self.client.get('/inventory/', {'pcode':'HKI128', 'width':58, 'loss':760})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKI128')
        self.assertEqual(response.context['width'], '58')
        self.assertEqual(response.context['loss'], '760')

    def test_inventory_CA125_58_1099(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':58, 'loss':1099})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '58')
        self.assertEqual(response.context['loss'], '1099')

########

    def test_inventory_HKS231_58_82(self):
        response = self.client.get('/inventory/', {'pcode':'HKS231', 'width':58, 'loss':82})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS231')
        self.assertEqual(response.context['width'], '58')
        self.assertEqual(response.context['loss'], '82')

    def test_inventory_HKS161_58_57(self):
        response = self.client.get('/inventory/', {'pcode':'HKS161', 'width':58, 'loss':57})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS161')
        self.assertEqual(response.context['width'], '58')
        self.assertEqual(response.context['loss'], '57')

    def test_inventory_CA125_58_66(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':58, 'loss':66})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '58')
        self.assertEqual(response.context['loss'], '66')

########

    def test_inventory_HLW174_52_16(self):
        response = self.client.get('/inventory/', {'pcode':'HLW174', 'width':52, 'loss':16})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HLW174')
        self.assertEqual(response.context['width'], '52')
        self.assertEqual(response.context['loss'], '16')

    def test_inventory_CA125_52_17(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':52, 'loss':17})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '52')
        self.assertEqual(response.context['loss'], '17')

########

    def test_inventory_HKS231_50_271(self):
        response = self.client.get('/inventory/', {'pcode':'HKS231', 'width':50, 'loss':271})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS231')
        self.assertEqual(response.context['width'], '50')
        self.assertEqual(response.context['loss'], '271')

    def test_inventory_HKS161_50_189(self):
        response = self.client.get('/inventory/', {'pcode':'HKS161', 'width':50, 'loss':189})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS161')
        self.assertEqual(response.context['width'], '50')
        self.assertEqual(response.context['loss'], '189')

    def test_inventory_CA125_50_217(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':50, 'loss':217})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '50')
        self.assertEqual(response.context['loss'], '217')

########

    def test_inventory_HKS231_50_153(self):
        response = self.client.get('/inventory/', {'pcode':'HKS231', 'width':50, 'loss':153})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS231')
        self.assertEqual(response.context['width'], '50')
        self.assertEqual(response.context['loss'], '153')

    def test_inventory_HKS161_50_107(self):
        response = self.client.get('/inventory/', {'pcode':'HKS161', 'width':50, 'loss':107})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS161')
        self.assertEqual(response.context['width'], '50')
        self.assertEqual(response.context['loss'], '107')

    def test_inventory_CA125_50_123(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':50, 'loss':123})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '50')
        self.assertEqual(response.context['loss'], '123')

########

    def test_inventory_HKS231_42_106(self):
        response = self.client.get('/inventory/', {'pcode':'HKS231', 'width':42, 'loss':106})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS231')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '106')

    def test_inventory_HKS161_42_74(self):
        response = self.client.get('/inventory/', {'pcode':'HKS161', 'width':42, 'loss':74})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKS161')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '74')

    def test_inventory_CA125_42_85(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':42, 'loss':85})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '42')
        self.assertEqual(response.context['loss'], '85')

########

    def test_inventory_HKI188_40_750(self):
        response = self.client.get('/inventory/', {'pcode':'HKI188', 'width':40, 'loss':750})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'HKI188')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '750')

    def test_inventory_CA125_40_738(self):
        response = self.client.get('/inventory/', {'pcode':'CA125', 'width':40, 'loss':738})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['pcode'], 'CA125')
        self.assertEqual(response.context['width'], '40')
        self.assertEqual(response.context['loss'], '738')

########

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

