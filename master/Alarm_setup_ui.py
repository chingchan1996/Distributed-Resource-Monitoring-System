# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alarm_setup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Alarm_Setup_Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 250))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 331, 81))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sB_cpu_limit = QtWidgets.QSpinBox(self.groupBox)
        self.sB_cpu_limit.setGeometry(QtCore.QRect(210, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.sB_cpu_limit.setFont(font)
        self.sB_cpu_limit.setPrefix("")
        self.sB_cpu_limit.setMaximum(100)
        self.sB_cpu_limit.setProperty("value", 50)
        self.sB_cpu_limit.setObjectName("sB_cpu_limit")
        self.sB_cpu_count = QtWidgets.QSpinBox(self.groupBox)
        self.sB_cpu_count.setGeometry(QtCore.QRect(210, 50, 111, 22))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.sB_cpu_count.setFont(font)
        self.sB_cpu_count.setPrefix("")
        self.sB_cpu_count.setMaximum(100)
        self.sB_cpu_count.setProperty("value", 50)
        self.sB_cpu_count.setObjectName("sB_cpu_count")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 150, 331, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 131, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sB_mem_limit = QtWidgets.QSpinBox(self.groupBox_2)
        self.sB_mem_limit.setGeometry(QtCore.QRect(210, 20, 111, 22))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.sB_mem_limit.setFont(font)
        self.sB_mem_limit.setPrefix("")
        self.sB_mem_limit.setMaximum(100)
        self.sB_mem_limit.setProperty("value", 50)
        self.sB_mem_limit.setObjectName("sB_mem_limit")
        self.sB_mem_count = QtWidgets.QSpinBox(self.groupBox_2)
        self.sB_mem_count.setGeometry(QtCore.QRect(210, 50, 111, 22))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.sB_mem_count.setFont(font)
        self.sB_mem_count.setPrefix("")
        self.sB_mem_count.setMaximum(100)
        self.sB_mem_count.setProperty("value", 50)
        self.sB_mem_count.setObjectName("sB_mem_count")
        self.btn_setup = QtWidgets.QPushButton(Dialog)
        self.btn_setup.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.btn_setup.setObjectName("btn_setup")
        self.label_hostname = QtWidgets.QLabel(Dialog)
        self.label_hostname.setGeometry(QtCore.QRect(40, 20, 321, 16))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_hostname.setFont(font)
        self.label_hostname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hostname.setObjectName("label_hostname")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "CPU Alarm"))
        self.label_2.setText(_translate("Dialog", "CPU limit"))
        self.label.setText(_translate("Dialog", "CPU limit count"))
        self.groupBox_2.setTitle(_translate("Dialog", "Memory Alarm"))
        self.label_4.setText(_translate("Dialog", "Memory limit"))
        self.label_3.setText(_translate("Dialog", "Memory limit count"))
        self.btn_setup.setText(_translate("Dialog", "Set up"))
        self.label_hostname.setText(_translate("Dialog", "hostname"))

