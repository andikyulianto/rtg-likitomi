"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

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

    def test_showplan(self):
        response = self.client.get('/showplan/', {'opdate':'2010-3-30'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['opdate'], '2010-3-30')
        self.assertTemplateUsed(response, 'showplan.html')

    def test_wholeplan(self):
        response = self.client.get('/wholeplan/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wholeplan.html')

    def test_showreq(self):
        response = self.client.get('/showreq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showreq.html')

    def test_reqhead(self):
        response = self.client.get('/reqhead/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reqhead.html')

    def test_required(self):
        response = self.client.get('/required/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'required.html')

    def test_showdet(self):
        response = self.client.get('/showdet/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'showdet.html')

    def test_dethead(self):
        response = self.client.get('/dethead/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dethead.html')

    def test_detail(self):
        response = self.client.get('/detail/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')

    def test_stock(self):
        response = self.client.get('/stock/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock.html')

    def test_inventory(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory.html')



__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

