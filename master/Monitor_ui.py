# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Monitor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # hardware_tree
        self.hardware_tree = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hardware_tree.sizePolicy().hasHeightForWidth())
        self.hardware_tree.setSizePolicy(sizePolicy)
        self.hardware_tree.setSizeIncrement(QtCore.QSize(0, 0))
        self.hardware_tree.setBaseSize(QtCore.QSize(0, 0))
        self.hardware_tree.setColumnCount(3)
        self.hardware_tree.setObjectName("hardware_tree")
        self.hardware_tree.headerItem().setText(0, "Hostname")
        self.hardware_tree.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.hardware_tree.headerItem().setText(1, "Value")
        self.hardware_tree.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.hardware_tree.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.hardware_tree.header().setCascadingSectionResizes(True)
        self.horizontalLayout_2.addWidget(self.hardware_tree)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # host name label here
        self.label_hostname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_hostname.setFont(font)
        self.label_hostname.setObjectName("label_hostnmae")
        self.horizontalLayout.addWidget(self.label_hostname)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_lastupdate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_lastupdate.setFont(font)
        self.label_lastupdate.setObjectName("label_lastupdate")
        self.horizontalLayout.addWidget(self.label_lastupdate)
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.verticalLayout.addLayout(self.horizontalLayout)
        # OS table here
        self.OS_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OS_table.sizePolicy().hasHeightForWidth())
        self.OS_table.setSizePolicy(sizePolicy)
        self.OS_table.setSizeIncrement(QtCore.QSize(0, 0))
        self.OS_table.setObjectName("OS_table")
        self.OS_table.setColumnCount(4)
        self.OS_table.setRowCount(0)
        self.OS_table.horizontalHeader().setSectionResizeMode(1)
        self.OS_table.setSelectionBehavior(1)
        self.OS_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OS_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OS_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OS_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.OS_table.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.OS_table)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        # process table here
        self.process_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process_table.sizePolicy().hasHeightForWidth())
        self.process_table.setSizePolicy(sizePolicy)
        self.process_table.setSizeIncrement(QtCore.QSize(0, 0))
        self.process_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.process_table.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.process_table.setObjectName("process_table")
        self.process_table.setColumnCount(5)
        self.process_table.setRowCount(0)
        self.process_table.horizontalHeader().setSectionResizeMode(1)
        self.process_table.setSelectionBehavior(1)
        self.process_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.process_table)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(2, 6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1025, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMaster = QtWidgets.QMenu(self.menuBar)
        self.menuMaster.setObjectName("menuMaster")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuSet_Refresh_Rate = QtWidgets.QMenu(self.menuView)
        self.menuSet_Refresh_Rate.setObjectName("menuSet_Refresh_Rate")
        # menu group
        self.menuSet_Regresh_Rate_Grooup = QtWidgets.QActionGroup(self.menuView)
        MainWindow.setMenuBar(self.menuBar)
        # menu of termiate
        self.actionTerminate_Master = QtWidgets.QAction(MainWindow)
        self.actionTerminate_Master.setObjectName("actionTerminate_Master")
        self.actionClose_GUI = QtWidgets.QAction(MainWindow)
        self.actionClose_GUI.setObjectName("actionClose_GUI")
        self.actionRefresh_Hardware_Status = QtWidgets.QAction(MainWindow)
        self.actionRefresh_Hardware_Status.setObjectName("actionRefresh_Hardware_Status")
        self.actionHigh = QtWidgets.QAction(MainWindow, checkable=True)
        self.actionHigh.setObjectName("actionHigh")
        self.actionMedium = QtWidgets.QAction(MainWindow, checkable=True)
        self.actionMedium.setObjectName("actionMedium")
        self.actionLow = QtWidgets.QAction(MainWindow, checkable=True)
        self.actionLow.setObjectName("actionLow")
        self.actionPause = QtWidgets.QAction(MainWindow, checkable=True)
        self.actionPause.setObjectName("actionPause")
        self.menuMaster.addAction(self.actionRefresh_Hardware_Status)
        self.menuMaster.addSeparator()
        self.menuMaster.addAction(self.actionTerminate_Master)
        action = self.menuSet_Regresh_Rate_Grooup.addAction(self.actionHigh)        
        self.menuSet_Refresh_Rate.addAction(action)
        action = self.menuSet_Regresh_Rate_Grooup.addAction(self.actionMedium) 
        self.menuSet_Refresh_Rate.addAction(action)
        action = self.menuSet_Regresh_Rate_Grooup.addAction(self.actionLow) 
        self.menuSet_Refresh_Rate.addAction(action)
        action = self.menuSet_Regresh_Rate_Grooup.addAction(self.actionPause) 
        self.menuSet_Refresh_Rate.addAction(action)
        self.menuView.addAction(self.menuSet_Refresh_Rate.menuAction())
        self.menuBar.addAction(self.menuMaster.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hardware_tree.headerItem().setText(2, _translate("MainWindow", "Refresh rate"))
        self.label_hostname.setText(_translate("MainWindow", "Hostname"))
        self.label_lastupdate.setText(_translate("MainWindow", "Last Update:"))
        self.label_time.setText(_translate("MainWindow", "None"))
        item = self.OS_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sensor"))
        item = self.OS_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        item = self.OS_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Max"))
        item = self.OS_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Min"))
        item = self.process_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pid"))
        item = self.process_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.process_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.process_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CPU usage(%)"))
        item = self.process_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Memory usage(%)"))
        self.menuMaster.setTitle(_translate("MainWindow", "Master"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSet_Refresh_Rate.setTitle(_translate("MainWindow", "Set Refresh Rate"))
        self.actionTerminate_Master.setText(_translate("MainWindow", "Terminate Master"))
        self.actionClose_GUI.setText(_translate("MainWindow", "Close GUI"))
        self.actionRefresh_Hardware_Status.setText(_translate("MainWindow", "Refresh Hardware Status"))
        self.actionHigh.setText(_translate("MainWindow", "High"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionLow.setText(_translate("MainWindow", "Low"))
        self.actionPause.setText(_translate("MainWindow", "Pause"))


