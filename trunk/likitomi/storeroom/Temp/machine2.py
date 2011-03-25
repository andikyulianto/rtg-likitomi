class Machine2:
    ''' machine objects'''
    def __init__(self,planId='1', planStart='08.00', planEnd='09.30'):
        self.machineName = 'CR'
        self.planId = planId
        self.planStart = planStart
        self.planEnd = planEnd
    def printIt(self,prefix=''):
        ''' Print the data nicely.'''
        print prefix,'Machine :',self.machineName,'plan',self.planId,'will start at',self.planStart,'plan to end at',self.planEnd
        
        #setter
    def setPlanId(self,planId="1"):
        self.planId = planId
    def setPlanStart(self,planStart="08.30"):
        self.planStart = planStart
    def setPlanEnd(self,planEnd="09.30"):
        self.planEnd = planEnd
    def setMachineName(self,machineName="CR"):
        self.machineName = machineName
class CR(Machine2):
    ''' holding task for CR machine '''
    def __init__(self):
        ''' Initialize with an start and stop time '''
        Machine.__init__(self, '1', '08.30', '10.00')
        self.setMachineName('CR')
class ThreeCL(Machine2):
    def __init__(self):
        Machine.__init__(self, '1', '08.35', '10.05')
        self.setMachineName =('ThreeCL')
    def setPlanStart(self,planStart='08.35'):
        if planStart !='08.30' and planStart != '08.35':
            raise delayException
            Machine.setPlanStart(self,planStart)
class TwoCL(Machine2):
    def __init__(self):
        ''' Initialize with start and stop time. '''
        Machine.__init__(self, '2', '08.40', '10.20')
        self.setMachineName('TwoCL')
    def printIT(self,prefix=''):
        '''Print even more nicely.'''
        print prefix,'Plan :',self.planId,'Machine :',self.machineName,'Start:',self.planStart,'End: ',self.planEnd
class delayException(Exception):
    pass
def test():
    '''Test function'''
    print 'Module Machine test'
    #Generic no arguments
    print 'Testing Machine Class'
    m = Machine()
    
    m.printIt("\t")
    
    m = Machine('2','10.10','10.30')
    
    #test CR
    print 'Testing CR class'
    cr = CR()
    cr.printIt("\t")
    
    cr.setMachineName('CR changes to CV')
    cr.printIt("\t")
    
    #test TwoCL
    print 'Testing TwoCL'
    d = TwoCL()
    d.printIT('\t')
    
    #test ThreeCL
    print 'Test ThreeCL'
    l = ThreeCL()
    l.printIt('\t')
    
    print 'Calling ThreeCL.setPlanStart()'
    try:
        l.setPlanStart('10.12')
    except delayException:
        print '\t','The actual plan is'
#Run est if this module is run a program.
if __name__ == '__main__':
    test()