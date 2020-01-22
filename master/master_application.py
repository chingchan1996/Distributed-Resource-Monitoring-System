import logging
import logging.config
import pickle
from pathlib import Path
import threading
import sys
import signal
from functools import partial
# custom
from Database import Database
from Coder import Encoder, Decoder 
from Message import Message
from MessageCenter import MessageCenter
from Machine import Machine
from Analyzer import Analyzer
from MyGUIHandler import MyGUIHandler

# initial logger
root = logging.getLogger('MonitorApplication')

def dbInitial(__debug):
    db = Database() 
    db.initializeDatabase(__debug) 
    return db
# end of initialDB()

def dumpLocalMachine( _machine, _dir ):
   with open( _dir, 'wb') as handle:
        pickle.dump( _machine, handle, protocol=pickle.HIGHEST_PROTOCOL )
# end of dumpLocalMachine()

def loadLocalMachine( _my_file ):
    with open(_my_file, 'rb') as handle:
        machine = pickle.load(handle)
    return machine
# end of loadLocalMachine()

def settingUpLocalMachine( _dir ):
    while True:
        root.debug( "Setting up..." )
        name = input( "Enter the machine name: " ) 
        ip = input( "Enter the machine IP address: " )
        port = input( "Enter the connection port: " )

        print( "\nName:" +name+", IP:"+ip+", Port:"+port + "\n" )
        cmd = input( "Confirm ? y/n  " )
        if cmd == "y":
             break

    localMachine = Machine( name, ip, port )
    dumpLocalMachine( localMachine, _dir )
    return localMachine
# end of settingUpLocalMachine()

def machineInitial( __debug ):
    my_path = "./machineFile.plk" 
    my_file = Path(my_path)

    if my_file.is_file():
        localmachine = loadLocalMachine( my_path ) 
        if __debug in ['True', 'true']:
            print( "\nLocal machine details: " )
            print( localmachine.toString() + "\n" )
            cmd = input( "Confirm ?  y/n  ") 
            if cmd == "y":
                pass
            else:
                localmachine = settingUpLocalMachine( my_path ) 
    else:
        localmachine = settingUpLocalMachine( my_path )

    return localmachine
# end of initialDB()


def initialStage():

    # logInitailize()
    root.setLevel(logging.DEBUG)
    fh = logging.FileHandler('master.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    root.addHandler(fh)
    
    # logging.config.fileConfig('logging.conf')
    
    # reading config for debug
    __debug = 'True'
    try:
        with open("debugsetting.cfg", 'r') as cfgfile:
            __debug = cfgfile.read().split(":")[1]
    except FileNotFoundError:
        with open("debugsetting.cfg", 'w+') as cfgfile:
            cfgfile.write('debug:True')
            __debug = 'True'

    if __debug in ['True', 'true']:
        std = logging.StreamHandler(sys.stdout)
        root.addHandler(std)
    
    
    root.debug( "Initializing ..." ) 

    # Initialize local machine
    root.debug( "Local machine check..." )
    localmachine = machineInitial( __debug )
    root.debug( "Local machine is confirmed.")

    # Initialize Database 
    root.debug( "Database check..." )
    db = dbInitial(__debug)
    root.debug( "Database is confirmed." )

    # initialize MessageCenter 
    root.debug( "Message center check..." )
    table = db.getMachineTable_ip()
    table[ localmachine.getIP() ] = localmachine.getName()
    msgCenter = MessageCenter( localmachine, table )
    msgCenter.start()
    root.debug( "Message Center is confirmed." )


    # Initialize Encoder
    root.debug( "Encoder check..." )
    table = db.getMachineTable_name()
    table[localmachine.getName()] = localmachine
    ec = Encoder( localmachine, table ) 
    root.debug( "Encoder is confirmed." )

    # initialize Decoder
    root.debug( "Decoder check..." )
    dc = Decoder( localmachine, table )
    root.debug( "Dncoder is confirmed." )

    # Connection test
    root.debug( "Connection test" )
    slaveList = db.getMachineList()

    for slName in slaveList:
        newMsg = ec.encodeMsg_out( "Sys", ["test", "test"], slName.getName() ) 
        if isinstance( newMsg, Message ):
            msgCenter.sendNewMessage( newMsg ) 
        else :
            root.debug( slName + ", cannot find the corresponed IP.")

    root.debug( "Connections are confirmed.")



    # initialize GUI
    myGUI = MyGUIHandler( ec, msgCenter, db, localmachine )

    ay = Analyzer( db, myGUI )

    return localmachine, db, msgCenter, ec, dc, ay, myGUI 


def messageHandler( _type, _obj, _db, _ay ):

    if _type == "status_os/p" or _type == "status_all":
        for o in _obj:
            _db.updateStatusRecord( o )
            _ay.analyzeData( o )
        return 'normal'
    elif _type == "status_h" or _type == "status_os" or _type == "status_p":
        _db.updateStatusRecord( _obj )
        _ay.analyzeData( obj )
        return 'normal'
    elif type == "sys":
        content = obj.getContent()

        if isinstance( content, str ):
            content = content
        else:
            content_2 = content[1]
            content = content[0]

        if content == 'terminate':
            return 'terminate'
        elif content == 'alarmData change':
            # content_2 should be 'name'
            _ay.refreshAlarmData( content_2 )
            return 'new alarm data accept'
        else:
            pass
        
# end of messageHandler()

def signal_handler(self, signum, frame):
    self.restart()
# end of signal_handler

if __name__ == "__main__":
    localmachine, db, msgCenter, ec, dc, ay, myGUI = initialStage()
    root.debug( "Initialization successed")
    signal.signal(signal.SIGINT, partial( signal_handler, myGUI ) )
    p = False 

    keepRunning = True
    while keepRunning:

        while not msgCenter.isQueueEmpty():
            p = not p 
            newMsg = msgCenter.getNewMessage()
            db.updateMessageRecord( newMsg )
            root.debug( newMsg.getSender() )
            type, obj = dc.decodeMessage( newMsg ) 
            status = messageHandler( type, obj, db, ay )
            if status == 'normal':
                pass
            elif status == 'terminate':
                keepRunning = False
                for name in db.getMachineNameList():
                    msg = ec.encodeMsg_out( 'sys', "stop transmit", name )
                    msgCenter.sendNewMessage( msg )
                # end of for-loop
                break
            else:
                pass

            if not myGUI.isAlive():
                pass
                # perform certain actions
        # end of inner while-loop
    # end of outer while-loop
            

        if p:
            root.debug( "OS_History Max")
            root.debug( db.getOSHistoryData( _name='slave1', _type='max' ) )
            # root.debug( db.getOSHistoryData( _name='slave2', _type='max' ) )
            root.debug( "END\n\n" )

            root.debug( "OS_History min")
            root.debug( db.getOSHistoryData( _name='slave1', _type='min' ) )
            # root.debug( db.getOSHistoryData( _name='slave2', _type='min' ) )
            root.debug( "END\n\n" )

            
            '''root.debug( "Type1")
            root.debug( db.getType1Data())
            root.debug( "END\n\n" )'''

            root.debug( "Type2")
            root.debug( db.getType2Data() )
            root.debug( "END\n\n" )
            
            '''root.debug( "Type3")
            root.debug( db.getType3Data() )
            root.debug( "END\n\n" )'''
            p = not p
