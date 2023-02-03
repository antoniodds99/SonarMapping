# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lbConnectionStatus = QtWidgets.QLabel(self.centralwidget)
        self.lbConnectionStatus.setText("")
        self.lbConnectionStatus.setObjectName("lbConnectionStatus")
        self.verticalLayout_2.addWidget(self.lbConnectionStatus)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnConnection = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnection.setEnabled(True)
        self.btnConnection.setObjectName("btnConnection")
        self.horizontalLayout.addWidget(self.btnConnection)
        self.btnMapping = QtWidgets.QPushButton(self.centralwidget)
        self.btnMapping.setEnabled(False)
        self.btnMapping.setObjectName("btnMapping")
        self.horizontalLayout.addWidget(self.btnMapping)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Select serial port"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select serial port"))
        self.comboBox.setItemText(1, _translate("MainWindow", "rfcomm0"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ttyUSB0"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ttyUSB1"))
        self.comboBox.setItemText(4, _translate("MainWindow", "ttyUSB2"))
        self.label.setText(_translate("MainWindow", "Connessione :"))
        self.btnConnection.setText(_translate("MainWindow", "Connection"))
        self.btnMapping.setText(_translate("MainWindow", "Start mapping"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
