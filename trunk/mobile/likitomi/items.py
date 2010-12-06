from django.http import HttpResponse
from django.template import Template, Context
from datetime import date
#from app.models import Employee, FakeStatusTracking
#from app.models import FakeStatusTracking
class Items:
    """ This module collect the items in the production line"""

    def __init__(self, plan_id, starter):
        self.plan_id = plan_id
        self.machine_name_start = ""
        self.machine_name_end = ""
        self.actualTime_start = ""
        self.actualTime_end = ""
        self.start_by = starter
        self.end_by = starter
    def startTask(self, machine_name):
        self.machine_name_start = machine_name
        self.actualTime_start = now()
    def endTask(self, machine_name, amount):
        self.machine_name_end = machine_name
        self.actualTime_end = now()
        self.actualAmount = amount
    def setEndBy(self, worker):
        self.end_by = worker
    def getProductDetail(self):
        print self.plan_id
    def getProductName(self):
        print self.plan_id
    def getStartBy(self):
        return self.start_by
    def getEndBy(self):
        return self.end_by
class CR(Items):
    ''' Hold the Corugator section task '''
    def __init__(self):
        ''' Initialize with plan '''
        Items.__init__(self, '1', "Fon")
        self
