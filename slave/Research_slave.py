from Slave import Slave
import time 
import logging
import sys

# initial logger
root = logging.getLogger('MonitorApplication')

if __name__ == '__main__':
    # initial logger
    root.setLevel(logging.DEBUG)
    fh = logging.FileHandler('slave.log')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    root.addHandler(fh)
    
    # reading config for debug
    _debug = 'True'
    try:
        with open("debugsetting.cfg", 'r') as cfgfile:
            _debug = cfgfile.read().split(":")[1]
    except FileNotFoundError:
        with open("debugsetting.cfg", 'w+') as cfgfile:
            cfgfile.write('debug:True')
            _debug = 'True'

    if _debug in ['True', 'true']:
        std = logging.StreamHandler(sys.stdout)
        root.addHandler(std)
    root.debug('logger stand by...')

    slave = Slave()
    slave.start()

    msgCenter = slave.getMsgCenter()
    ec = slave.getEncoder()
    lm = slave.getLocalMachine()
    while True and _debug in ['True', 'true']:
        cmd = input( "start to start, 1 - 5 to change request, stop to stop, t to terminate\n" )
        msg = None 
        if cmd == "start":
            msg = ec.encodeMsg_out( "sys", "start transmit", lm.getName() )
        elif cmd == "stop":
            msg = ec.encodeMsg_out( "sys", "stop transmit", lm.getName() )
        elif cmd == "t":
            msg = ec.encodeMsg_out( "sys", "terminate", lm.getName() )
        elif cmd == "1":
            msg = ec.encodeMsg_out( "sys", "request type1", lm.getName() )
        elif cmd == "2":
            msg = ec.encodeMsg_out( "sys", "request type2", lm.getName() )
        elif cmd == "3":
            msg = ec.encodeMsg_out( "sys", "request type3", lm.getName() )
        elif cmd == "4":
            msg = ec.encodeMsg_out( "sys", "request type4", lm.getName() )
        elif cmd == "5":
            msg = ec.encodeMsg_out( "sys", "request type5", lm.getName() )
        elif cmd == "c2":
            msg = ec.encodeMsg_out( "sys", "clock change 2", lm.getName() )
        elif cmd == "c10":
            msg = ec.encodeMsg_out( "sys", "clock change 10", lm.getName() )
        elif cmd == "c30":
            msg = ec.encodeMsg_out( "sys", "clock change 30", lm.getName() )
        elif cmd == "c60":
            msg = ec.encodeMsg_out( "sys", "clock change 60", lm.getName() )
        elif cmd == "c120":
            msg = ec.encodeMsg_out( "sys", "clock change 120", lm.getName() )
        elif cmd == "k":
            msg = ec.encodeMsg_out( "sys", "kill process pid", lm.getName() )

        if msg != None:
            msgCenter.sendNewMessage( msg )
        else:
            pass

        if not slave.is_alive():
            break
        else:
            pass
