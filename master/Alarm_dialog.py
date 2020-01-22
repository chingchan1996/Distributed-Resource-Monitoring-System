from Alarm_dialog_ui import Alarm_Ui_Dialog
from PyQt5 import QtCore, QtWidgets, QtGui
import threading
import sys

class AlarmDialog(QtWidgets.QMainWindow):
    def __init__(self, hostname, problem, threshold, current, time):
        QtWidgets.QWidget.__init__(self)
        self.ui = Alarm_Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.tx_hostname.setText(hostname)
        self.ui.tx_problem.setText(problem)
        self.ui.tx_threshold.setText(threshold)
        self.ui.tx_currentstatus.setText(current)
        self.ui.tx_timestamp.setText(time)

class AlarmGuiThread(threading.Thread):
    def __init__(self, hostname, problem, threshold, current, time):
        threading.Thread.__init__(self)
        self.hostname = hostname
        self.problem = problem
        self.threshold = threshold
        self.current_status = current
        self.time = time

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        form = AlarmDialog(self.hostname, self.problem, self.threshold, self.current_status, self.time)
        form.setWindowTitle('Alarm window')
        form.show()
        app.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = AlarmDialog("Slave3", "CPU overloading", "CPU usage > 95%", "50%", "2017/11/25 12:00")
    form.setWindowTitle('Alarm')
    form.show()
    sys.exit(app.exec_())