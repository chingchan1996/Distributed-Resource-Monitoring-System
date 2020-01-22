class AlarmData(object):
    """description of class"""
    def __init__(self, _name, _cpu_limit, _mem_limit, _cpu_count_limit, _mem_count_limit ):
        self.__name = _name 
        self.__cpu_limit = _cpu_limit
        self.__mem_limit = _mem_limit
        self.__cpu_count_limit = _cpu_count_limit
        self.__mem_count_limit = _mem_count_limit

        self.__cpu_count = 0
        self.__mem_count = 0

        self.__isNeedAlarm_cpu = self.__isNeedAlarm_mem = False
  
    # end of the declaration of Constructor

    def setCPULimit(self, _limit ):
        self.__cpu_limit = float( _limit )
    # end of setCPUCount()

    def setMemLimit(self, _limit ):
        try:
            self.__mem_limit = float( _limit )
        except ValueError as e:
            print( e.args[0] )
    # end of setMemCount()
    
    def setCPUCountLimit(self, _count ):
        try:
            self.__cpu_count_limit = int( _count )
        except ValueError as e:
            print( e.args[0] )
    # end of setCPUCountLimit()

    def setCPUMemLimit(self, _count ):
        try:
            self.__cpu_mem_limit = int( _count )
        except ValueError as e:
            print( e.args[0] )
    # end of setCPUMemLimit()

    def getName(self):
        return self.__name
    # end of getName()

    def getCPUCount(self):
        return self.__cpu_count
    # end of getCPUCount()

    def getMemCount(self):
        return self.__mem_count
    # end of getMemCount()

    def getCPULimit(self):
        return self.__cpu_limit
    # end of getCPULimit()

    def getMemLimit(self):
        return self.__mem_limit
    # end of getMemLimit()

    def getCPUCountLimit(self):
        return self.__cpu_count_limit
    # end of getCPUCountLimit()

    def getMemCountLimit(self):
        return self.__mem_count_limit
    # end of getMemCountLimit()

    def markCPU(self, _reset=False):
        self.__cpu_count = self.__cpu_count + 1 if not _reset else 0
    # end of markCPU()

    def markMem(self, _reset=False):
        self.__mem_count = self.__mem_count + 1 if not _reset else 0
    # end of markMem()

    def isNeedAlarm(self):
        if self.__cpu_count >= self.__cpu_count_limit:
            self.__isNeedAlarm_cpu = True
        if self.__mem_count >= self.__mem_count_limit:
            self.__isNeedAlarm_mem = True

        if self.__isNeedAlarm_cpu == True and self.__isNeedAlarm_mem == True:
            return True, 'CPU & Mem', 'CPU:' + str( self.__cpu_limit ) + ' Memory:' + str( self.__mem_limit )
        elif self.__isNeedAlarm_cpu == True and self.__isNeedAlarm_mem == False:
            return True, 'CPU', 'CPU Threshold:' + str( self.__cpu_limit )
        elif self.__isNeedAlarm_cpu == False and self.__isNeedAlarm_mem == True:
            return True, 'Mem', 'Memory Threshold:' + str( self.__mem_limit )
        else:
            return False, None, None
    # end of isNeedAlarm()

    def alarmed(self):
        self.__isNeedAlarm_cpu = self.__isNeedAlarm_mem = False 
    # end of alarmed()

    def toString(self):
        return 'CPU Limit:' + str( self.__cpu_limit ) + 'CPU Count Limit:' + str( self.__cpu_count_limit ) + 'Mem Limit:' + str( self.__mem_limit ) + 'Mem Count Limit:' + str( self.__mem_count_limit )
    # end of toString()
           
