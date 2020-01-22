from Database import Database
from SystemDeliveryObjects import Status_Software
from AlarmData import AlarmData
from Alarm_dialog_ui import Alarm_Ui_Dialog
from Alarm_dialog import AlarmGuiThread

class Analyzer(object):
    """description of class"""
    def __init__(self, _db, _myGUI ):
        self.__db = _db
        self.__update = False
        self.__historyData_max = {}
        self.__historyData_min = {}
        self.__machineNameList = self.__db.getMachineNameList()
        
        self.__alarm = {}

        self.__alarmGUI = None 
        self.__myGUI = _myGUI 

        for name in self.__machineNameList:
            self.__historyData_max[name] = self.__db.getOSHistoryData( _name=name, _type='max' )
            self.__historyData_min[name] = self.__db.getOSHistoryData( _name=name, _type='min' )

            alarmDataBuffer = self.__db.getAlarmData( name )
            if alarmDataBuffer == None:
                self.__alarm[name] = AlarmData( name, 0.1, 20, 10, 10 )
                self.__db.insertAlarmData( self.__alarm[name] )
            else:
                self.__alarm[name] = alarmDataBuffer
        # end of for-loop

        
    # end of the declaration of constructor

    def analyzeData(self, _obj ):
        self.max_min_Analyze( _obj )

        if not self.__myGUI.isAlive():
            self.alarm_Analyze( _obj )
        else:
            pass
    # end of analyzeData()

    def max_min_Analyze(self, _obj):
        if isinstance( _obj, Status_Software ):
            name = _obj.getOwnerName() 
            if self.__historyData_max[name] != None:
                cpuTotal_record = float( self.__historyData_max[name]['cpu_sys'] ) + float( self.__historyData_max[name]['cpu_usr'] )
                cpuTotel_current = float( _obj.getCPU_sys() ) + float( _obj.getCPU_usr() )

                if cpuTotel_current > cpuTotal_record:
                    self.__update = True
                    self.__db.updateOSHistory( name, 'cpu', [ _obj.getCPU_usr(), _obj.getCPU_sys(),_obj.getCPU_idle()], 'max' )
                else:
                    pass

                if float( _obj.getMem_percent() ) > float( self.__historyData_max[name]['mem_per'] ):
                    self.__update = True
                    self.__db.updateOSHistory( name, 'mem_per', _obj.getMem_percent(), 'max' )
                else:
                    pass

            else:
                self.__db.insertOSHistory( _obj, 'max' )
                self.__update = True

            if self.__update:
                self.__historyData_max[name] = self.__db.getOSHistoryData( name, 'max' )
                self.__update = False
            else:
                pass

            if self.__historyData_min[name] != None:
                cpuTotal_record = float( self.__historyData_min[name]['cpu_sys'] ) + float( self.__historyData_min[name]['cpu_usr'] )
                cpuTotel_current = float( _obj.getCPU_sys() ) + float( _obj.getCPU_usr() )

                if cpuTotel_current < cpuTotal_record:
                    self.__update = True
                    self.__db.updateOSHistory( name, 'cpu', [ _obj.getCPU_usr(), _obj.getCPU_sys(),_obj.getCPU_idle()], 'min' )
                else:
                    pass

                if float( _obj.getMem_percent() ) < float( self.__historyData_max[name]['mem_per'] ):
                    self.__update = True
                    self.__db.updateOSHistory( name, 'mem_per', _obj.getMem_percent(), 'min' )
                else:
                    pass

            else:
                self.__db.insertOSHistory( _obj, 'min' )
                self.__update = True

            if self.__update:
                self.__historyData_min[name] = self.__db.getOSHistoryData( name, 'min' )
                self.__update = False
            else:
                pass
        else:
            pass
    # end of max_min_analyze()

    def alarm_Analyze(self, _obj):
        if isinstance( _obj, Status_Software ):
            cpuTotal = float( _obj.getCPU_sys() ) + float( _obj.getCPU_usr() )
            memTotal = float( _obj.getMem_percent() )
            name = _obj.getOwnerName()
            if cpuTotal > self.__alarm[name].getCPULimit():
                self.__alarm[name].markCPU()
                print( "cpu count " + name  + ":" + str( self.__alarm[name].getCPUCount() ) )
            else:
                pass

            if memTotal > self.__alarm[name].getMemLimit():
                self.__alarm[name].markMem()
                print( "mem count " + name + ":" + str( self.__alarm[name].getMemCount() ) )
            else:
                pass

            needAlarm, type, threshold= self.__alarm[name].isNeedAlarm()
            if needAlarm:
                
                if self.__alarmGUI == None or not self.__alarmGUI.is_alive():

                    if type == 'CPU':
                        currentUsage = str( cpuTotal )
                    elif type == 'Mem':
                        currentUsage = str( memTotal )
                    else:
                        currentUsage = 'CPU:' + str( cpuTotal ) + 'Memory:' + str( memTotal )

                    self.__alarmGUI = AlarmGuiThread( name, type, threshold, currentUsage, _obj.getChron() )
                    self.__alarmGUI.start()

                    self.__alarm[name].alarmed()
                    self.__alarm[name].markCPU( _reset=True )
                    self.__alarm[name].markMem( _reset=True )
                else:
                    pass
            else:
                pass
        else:
            pass
    # end of alarm_Analyze

    def setAlarmCPULimit(self, _name, _percent):
        self.__alarm[_name]['cpu_limit'] = float( _percent)
    # end of setAlarmCPULimit()

    def setAlarmMemLimit(self, _name, _percent):
        self.__alarm[_name]['mem_limit'] = float( _percent )
    # end of setAlarmMemLimit()

    def updateAlarmData(self, name, _newData ):
        self.__alarm[name] = AlarmData( _newData[0], _newData[1], _newData[2], _newData[3], _newData[4] )
        self.__db.updateAlarmData( _newData )
    # end of updateAlarmData()

    def refreshAlarmData(self, _name):
        self.__alarm[_name] = self.__db.getAlarmData( _name )
        print( self.__alarm[_name].toString() )
    # end of refreshAlarmData()