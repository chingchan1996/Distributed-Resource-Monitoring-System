from PyQt5 import QtCore, QtWidgets, QtGui
from Monitor_ui import Ui_MainWindow
from Fre_dialog_ui import Frequence_Dialog
from Database import Database
from Alarm_dialog import AlarmGuiThread
from Alarm_setup_ui import Alarm_Setup_Ui_Dialog
import sys
import threading
import time
import random
from AlarmData import AlarmData

class MyForm (QtWidgets.QMainWindow):
    def __init__(self, _ec=None, _mc=None, _db=None, _lm=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # communication components set up
        self.__ec = _ec 
        self.__messagecenter = _mc
        self.__db = Database()
        self.__localMachine = _lm
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.refresh_table)       

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionPause.setChecked(True) # Default view menu selection
        # hardware_tree set up
        self.ui.hardware_tree.setHeaderLabels(["HostName","Value"])
        self.load_hardware_status()
        self.ui.hardware_tree.expandAll()
        self.ui.hardware_tree.resizeColumnToContents(0)
        self.ui.hardware_tree.setContextMenuPolicy(3)
        self.ui.hardware_tree.customContextMenuRequested.connect(self.slave_cmd_menu)
        self.ui.hardware_tree.itemClicked.connect(self.tree_click_handler)
        # menu bar set up
        self.ui.menuMaster.triggered.connect(self.master_menubar_handler)
        self.ui.menuView.triggered.connect(self.view_menubar_handler)
        # process table menu set up
        self.ui.process_table.setContextMenuPolicy(3)
        self.ui.process_table.customContextMenuRequested.connect(self.process_cmd_menu)

        self.ui.menuMaster.setDefaultAction(self.ui.actionPause)
        # RefreshTableThread(1, self.ui).start()
        
        # to initialize the update frq
        self.initialSlavesUpdateFreq()

    # end of the declaration of Contructor

    def initialSlavesUpdateFreq(self):
        for name in self.__db.getMachineNameList():
            self.sendFrqChange( _time=5, _host_name=name )
    # end initialSlavesUploadFreq

    # click the top level of tree and laod the Os table and process table.
    def tree_click_handler(self, item, col):
        if not item.parent():
            # print(item.text(0))
            self.ui.label_hostname.setText(item.text(0))
            # start to laod OS table and Process table here.
            self.load_OS_table(item.text(0))
            self.load_process_table(item.text(0))


    # get the hardware msg from getter.
    def load_hardware_status(self):
        # get the hardware msg from getter.
        self.ui.hardware_tree.clear()
        machineList = self.__db.getMachineNameList()

        for name in machineList:
            parent = QtWidgets.QTreeWidgetItem(self.ui.hardware_tree)
            parent.setText(0, name )
            parent.setText(2, "2")
            try:
                HWData = self.__db.getType1Data(1, name)[0]
                ls = ["Physical CPU","Logical CPU","Min CPU frequency","Max CPU frequency","Memory size","Boost time"]
                for x in ls:
                    child = QtWidgets.QTreeWidgetItem(parent)
                    child.setText(0, x)
                    if x == "Physical CPU":
                        child.setText(1, str( HWData['phy_cpu'] ) )
                    elif x == "Logical CPU":
                        child.setText(1, str( HWData['log_cpu'] ) )
                    elif x == "Min CPU frequency":
                        child.setText(1, str( HWData['min_cpu_freq'] ) )
                    elif x == "Max CPU frequency":
                        child.setText(1, str( HWData['max_cpu_freq'] ) )
                    elif x == "Memory size":
                        byte_size = HWData['mem_size']
                        mega_size = byte_size / pow(2, 20)
                        child.setText(1, str( mega_size )+" MB" )
                    elif x == "Boost time":
                        child.setText(1, str( HWData['boot_time'] ) )
            except IndexError as e:
                pass
        '''
        # Just for test
        machineList = ['s1','s2','s3']

        for name in machineList:
            parent = QtWidgets.QTreeWidgetItem(self.ui.hardware_tree)
            parent.setText(0, name )
            parent.setText(2,"0") # 
            ls = ["Physical CPU","Logical CPU","Min CPU frequency","Max CPU frequency","Memory size","Boost time"]
            for x in ls:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setText(0, x)
                child.setText(1, "text~~")
        '''

    # change last update time evey while loading table.
    def load_update_time(self, _t):
        self.ui.label_time.setText(_t)

    # laod the OS status here.
    def load_OS_table(self, _hostname):

        senser = []
        value = []
        Max = []
        Min = []
        try:
            # get the threshold data
            alarmdata = self.__db.getAlarmData(_hostname)
            cpu_limit = float(alarmdata.getCPULimit())
            mem_limit = float(alarmdata.getMemLimit())

            max_stats = self.__db.getOSHistoryData( _hostname, 'max' )
            min_stats = self.__db.getOSHistoryData( _hostname, 'min' )
            cur_stats = self.__db.getType2Data(_name = _hostname)[0]
            senser = ['cpu_usr', 'cpu_sys', 'cpu_idle', 'mem_per']
            time = cur_stats['time']

            value = [cur_stats['cpu_usr'], cur_stats['cpu_sys'], cur_stats['cpu_idle'], cur_stats['mem_percent']]
            Max = [max_stats['cpu_usr'], max_stats['cpu_sys'], max_stats['cpu_idle'], max_stats['mem_per']]
            Min = [min_stats['cpu_usr'], min_stats['cpu_sys'], min_stats['cpu_idle'], min_stats['mem_per']]
            
            self.load_update_time( cur_stats['time'] )
            self.ui.OS_table.setRowCount(4)
            for row in range(4): # {0:'cpu_usr', 1:'cpu_sys', 2:'cpu_idle', 3:'mem_per'}
                item_senser = QtWidgets.QTableWidgetItem(senser[row])
                item_value = QtWidgets.QTableWidgetItem(value[row])
                item_max = QtWidgets.QTableWidgetItem(Max[row])
                item_min = QtWidgets.QTableWidgetItem(Min[row])
                # setItem(row num, column num, table_Item)
                self.ui.OS_table.setItem( row, 0, item_senser )
                self.ui.OS_table.setItem( row, 1, item_value )
                self.ui.OS_table.setItem( row, 2, item_max )
                self.ui.OS_table.setItem( row, 3, item_min )

            cpu_usr = self.ui.OS_table.item(0,1)
            cpu_sys = self.ui.OS_table.item(1,1)
            mem_per = self.ui.OS_table.item(3,1)
            if float(cpu_usr.text()) + float(cpu_sys.text()) >= cpu_limit:
                cpu_usr.setBackground(QtGui.QColor(255, 128, 128))
                cpu_sys.setBackground(QtGui.QColor(255, 128, 128))
            if float(mem_per.text()) >= mem_limit:
                mem_per.setBackground(QtGui.QColor(255, 128, 128))

        except IndexError as e:
            pass

    # load process status here.
    def load_process_table(self, _hostname):

        pid = []
        name = []
        username = []
        cpu_usg = []
        mem_usg = []
        i = 0
        try:
            for p in self.__db.getType3Data(_name = _hostname)[0]:
                pid.append(p['pid'])
                name.append(p['name'])
                username.append(p['username'])
                cpu_usg.append(p['cpu_percent'])
                mem_usg.append(p['memory_percent'])
                i = i + 1

            self.ui.process_table.setRowCount(i)
            for row in range(i):
                item_pid = QtWidgets.QTableWidgetItem(str(pid[row]))
                item_name = QtWidgets.QTableWidgetItem(str(name[row]))
                item_username = QtWidgets.QTableWidgetItem(str(username[row]))
                item_cpu_usg = QtWidgets.QTableWidgetItem(str(cpu_usg[row]))
                item_mem_usg = QtWidgets.QTableWidgetItem(str(mem_usg[row]))
                # setItem(row num, column num, table_Item)
                self.ui.process_table.setItem( row, 0, item_pid )
                self.ui.process_table.setItem( row, 1, item_name )
                self.ui.process_table.setItem( row, 2, item_username )
                self.ui.process_table.setItem( row, 3, item_cpu_usg )
                self.ui.process_table.setItem( row, 4, item_mem_usg )
        except IndexError as e:
            pass
        '''
        # Jsust fot test
        pid = ['0001', '0012']
        name = ['python3', 'Adobe CS6']
        username = ['Tom', 'Jack']
        cpu_usg = ['10%', '25%']
        mem_usg = ['0.5%','1.2%']
        self.ui.process_table.setRowCount(2)
        for row in range(2):
            item_pid = QtWidgets.QTableWidgetItem(pid[row])
            item_name = QtWidgets.QTableWidgetItem(name[row])
            item_username = QtWidgets.QTableWidgetItem(username[row])
            item_cpu_usg = QtWidgets.QTableWidgetItem(cpu_usg[row])
            item_mem_usg = QtWidgets.QTableWidgetItem(mem_usg[row])
            # setItem(row num, column num, table_Item)
            self.ui.process_table.setItem( row, 0, item_pid )
            self.ui.process_table.setItem( row, 1, item_name )
            self.ui.process_table.setItem( row, 2, item_username )
            self.ui.process_table.setItem( row, 3, item_cpu_usg )
            self.ui.process_table.setItem( row, 4, item_mem_usg )
        '''
    def slave_cmd_menu(self, pos):
        index = self.ui.hardware_tree.indexAt(pos)        
        item = self.ui.hardware_tree.itemAt(pos)
        # only parent can be right clicked
        if index.parent().isValid() or item == None:
            return
        host_name = item.text(0)

        menu = QtWidgets.QMenu()
        alarm = menu.addAction('Set alarm of "' + host_name + '"' )
        freq = menu.addAction('Set update frequency' )
        start = menu.addAction('Send start transmit message to "' + host_name +'"')
        stop = menu.addAction('Send stop transmit message to "' + host_name +'"' )
        menu.addSeparator()
        term = menu.addAction('Send terminate message to "' + host_name +'"')
        action = menu.exec_(self.ui.hardware_tree.mapToGlobal(pos))
        if action == freq:
            widget = FrequenceDialog()
            widget.setWindowTitle('Set frequency')
            widget.exec_()
            if widget.fre != None:
                self.sendFrqChange(widget.fre, host_name)
                # change the refresh rate
                item.setText(2, widget.fre)
        elif action == start:
            msg = self.__ec.encodeMsg_out( "sys", "start transmit", host_name )
            self.__messagecenter.sendNewMessage( msg )
        elif action == stop:
            msg = self.__ec.encodeMsg_out( "sys", "stop transmit", host_name )
            self.__messagecenter.sendNewMessage( msg )
        elif action == term:
            msg = self.__ec.encodeMsg_out( "sys", "terminate", host_name )
            self.__messagecenter.sendNewMessage( msg )
        elif action == alarm:
            alarmbuf = self.__db.getAlarmData(host_name)
            widget = AlarmSetupDialog(host_name, [alarmbuf.getCPULimit(),alarmbuf.getCPUCountLimit(),alarmbuf.getMemLimit(),alarmbuf.getMemCountLimit()])
            widget.setWindowTitle('Set alarm')
            widget.exec_()
            if widget.update_data != None:
                alarmbuf = AlarmData(host_name, widget.update_data[0], widget.update_data[2], widget.update_data[1], widget.update_data[3])
                self.__db.updateAlarmData(alarmbuf)


    def process_cmd_menu(self, pos):
        try:
            index = self.ui.process_table.itemAt(pos).row()
        except AttributeError:
            return
        pid = self.ui.process_table.item(index,0).text()

        menu = QtWidgets.QMenu()
        kill = menu.addAction('Kill process')
        action = menu.exec_(self.ui.process_table.mapToGlobal(pos))
        if action == kill:
            # print('kill cmd in row{}, pid{}'.format(index, pid))
            msg = self.__ec.encodeMsg_out( "sys", "kill process " + pid, self.ui.label_hostname.text() )
            self.__messagecenter.sendNewMessage( msg )

    def master_menubar_handler(self, action):
        if action == self.ui.actionRefresh_Hardware_Status:
            self.load_hardware_status()
        elif action == self.ui.actionTerminate_Master:
            msg = self.__ec.encodeMsg_out( "sys", "terminate", self.__localMachine.getName() )
            self.__messagecenter.sendNewMessage( msg )
        
    def view_menubar_handler(self, action):
        self.timer.start()
        if action == self.ui.actionHigh:
            self.timer.setInterval(1000)
        elif action == self.ui.actionMedium:
            self.timer.setInterval(10000)
        elif action == self.ui.actionLow:
            self.timer.setInterval(30000)
        elif action == self.ui.actionPause:
            self.timer.stop()

    def sendFrqChange(self, _time='10', _host_name="slave1"):
        cmd = "clock change " + str(_time)
        msg = self.__ec.encodeMsg_out( "sys", cmd, _host_name )
        self.__messagecenter.sendNewMessage( msg )

    def refresh_table(self):
        '''
        self.ui.label_time.setText(time.asctime())
        pid = ['0001', '0012']
        name = ['python3', 'Adobe CS6']
        username = ['Tom', 'Jack']
        cpu_usg = [str(random.randint(10,100)), '25']
        mem_usg = [str(random.randint(10,100)),'1.2']
        # self.ui.process_table.setRowCount(2)
        for row in range(2):
            item_pid = QtWidgets.QTableWidgetItem(pid[row])
            item_name = QtWidgets.QTableWidgetItem(name[row])
            item_username = QtWidgets.QTableWidgetItem(username[row])
            item_cpu_usg = QtWidgets.QTableWidgetItem(cpu_usg[row])
            item_mem_usg = QtWidgets.QTableWidgetItem(mem_usg[row])
            # setItem(row num, column num, table_Item)
            self.ui.process_table.setItem( row, 0, item_pid )
            self.ui.process_table.setItem( row, 1, item_name )
            self.ui.process_table.setItem( row, 2, item_username )
            self.ui.process_table.setItem( row, 3, item_cpu_usg )
            self.ui.process_table.setItem( row, 4, item_mem_usg )
        '''
        self.load_OS_table( self.ui.label_hostname.text() )
        self.load_process_table( self.ui.label_hostname.text() )  

class GuiThread(threading.Thread):
    def __init__(self, _ec, _mc, _db, _localMachine ):
        threading.Thread.__init__(self, daemon=True)
        self.__ec = _ec # encoder
        self.__messageCenter = _mc # messageCenter
        self.__db = _db # database
        self.__localMachine = _localMachine # localMachine master

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        form = MyForm( self.__ec, self.__messageCenter, self.__db, self.__localMachine )
        form.setWindowTitle('Distributed Resource Monitoring System powered by CYCU ICE')
        form.show()
        sys.exit(app.exec_())

class FrequenceDialog(QtWidgets.QDialog, Frequence_Dialog):
    def __init__(self, parent=None):
        super(FrequenceDialog, self).__init__(parent)
        self.fre = None
        self.setupUi(self)
        self.btn_submit.clicked.connect(self.submit)

    def submit(self):
        self.fre = self.text_freq.text()
        self.accept()

class AlarmSetupDialog(QtWidgets.QDialog, Alarm_Setup_Ui_Dialog):
    def __init__(self, hostname, data, parent=None):
        super(AlarmSetupDialog, self).__init__(parent)
        self.setupUi(self)
        self.old_data = data
        self.update_data = None
        self.label_hostname.setText(hostname)
        self.btn_setup.clicked.connect(self.submit)
        self.load_alarm_data()

    def submit(self):
        cpu_limit = self.sB_cpu_limit.value()
        cpu_cnt = self.sB_cpu_count.value()
        mem_limit = self.sB_mem_limit.value()
        mem_cnt = self.sB_mem_count.value()
        self.update_data = [cpu_limit, cpu_cnt, mem_limit, mem_cnt]
        self.accept()

    def load_alarm_data(self):
        self.sB_cpu_limit.setValue(self.old_data[0])
        self.sB_cpu_count.setValue(self.old_data[1])
        self.sB_mem_limit.setValue(self.old_data[2])
        self.sB_mem_count.setValue(self.old_data[3])

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        form = MyForm()
        form.setWindowTitle('Distributed Resource Monitoring System powered by CYCU ICE')
        form.show()
        sys.exit(app.exec_())

