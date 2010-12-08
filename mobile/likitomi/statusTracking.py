
from app.models import FakeStatusTracking

class Plan:
    def __init__(self,planId=''):
        self.planID = planId
        self.machineName =''
        self.planStart =''
        self.planEnd =''
        self.planAmount = ''
    def setMachineName(self,newMachineName):
        self.machineName = newMachineName
    def getMachineName(self):
        return self.machineName
    def getPlanStart(self):
        planObj = FakeStatusTracking.objects.get(plan_id=self.planID)
        print planObj
    def getPlanId(self):
        return self.planID
    def printPlan(self):
        #print 'plan:',planID,'machine:',machineName,'start: ',planStart,'end: ',planEnd,'amount: ',planAmount
        print 'plan:',self.PlanID
class Machine:
    ''' machine objects'''
    def __init__(self,planId='', planStart='', planEnd='',planAmount =''):
        self.machineName = ''
        self.planId = planId
        self.planStart = planStart
        self.planEnd = planEnd
        self.actualStart = ''
        self.actualEnd = ''
        self.actualAmount =''
    def printIt(self,prefix=''):
        ''' Print the data nicely.'''
        print prefix,'Machine :',self.machineName,'plan',self.planId,'will start at',self.planStart,'plan to end at',self.planEnd
        
        #setter
    def setPlanId(self,planID=""):
        self.planId = planID
    def setPlanStart(self,planStart=""):
        self.planStart = planStart
    def setPlanEnd(self,planEnd=""):
        self.planEnd = planEnd
    def setMachineName(self,machineName=""):
        self.machineName = machineName
        
        
## Testing ##
import unittest

class PlanTest(unittest.TestCase):
    def setUp(self):
        self.plan = Plan()
        self.plan.__init__('1')
        self.plan.setMachineName("CR")

    def runTest(self):
        """ Test plan object """
        self.assertEquals(self.plan.getPlanId(), '1')
        self.assertEquals(self.plan.getMachineName(),"CR")
def suite():
    suite = unittest.TestSuite()
    suite.addTest(PlanTest())
    return suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)