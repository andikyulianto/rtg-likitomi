import unittest
class ArithTest (unittest.TestCase):
    def runTest(self):
        """ Test addition and succeed11. """
        self.failUnless(1+1==2, 'one plus one fails!')
        self.failIf(1+1 != 2, 'one plus one fails again!')
        self.failUnlessEqual(1+1, 2, 'more trouble with one plus one')
def suite():
    suite = unittest.TextTestRunner()
    suite.addTest(ArithTest())
    return suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)