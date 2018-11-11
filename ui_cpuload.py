# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpuload.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CpuLoad(object):
    def setupUi(self, CpuLoad):
        CpuLoad.setObjectName("CpuLoad")
        CpuLoad.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(CpuLoad)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CpuLoad)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cpu1 = QtWidgets.QProgressBar(CpuLoad)
        self.cpu1.setStyleSheet("")
        self.cpu1.setProperty("value", 0)
        self.cpu1.setObjectName("cpu1")
        self.gridLayout.addWidget(self.cpu1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(CpuLoad)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cpu2 = QtWidgets.QProgressBar(CpuLoad)
        self.cpu2.setStyleSheet("")
        self.cpu2.setProperty("value", 0)
        self.cpu2.setObjectName("cpu2")
        self.gridLayout.addWidget(self.cpu2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(CpuLoad)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.cpu3 = QtWidgets.QProgressBar(CpuLoad)
        self.cpu3.setStyleSheet("")
        self.cpu3.setProperty("value", 0)
        self.cpu3.setObjectName("cpu3")
        self.gridLayout.addWidget(self.cpu3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(CpuLoad)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.cpu4 = QtWidgets.QProgressBar(CpuLoad)
        self.cpu4.setStyleSheet("")
        self.cpu4.setProperty("value", 0)
        self.cpu4.setObjectName("cpu4")
        self.gridLayout.addWidget(self.cpu4, 3, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(CpuLoad)
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(CpuLoad)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.retranslateUi(CpuLoad)
        QtCore.QMetaObject.connectSlotsByName(CpuLoad)

    def retranslateUi(self, CpuLoad):
        _translate = QtCore.QCoreApplication.translate
        CpuLoad.setWindowTitle(_translate("CpuLoad", "CPU Load"))
        self.label.setText(_translate("CpuLoad", "CPU 1"))
        self.label_2.setText(_translate("CpuLoad", "CPU 2"))
        self.label_3.setText(_translate("CpuLoad", "CPU 3"))
        self.label_4.setText(_translate("CpuLoad", "CPU 4"))
        self.label_5.setText(_translate("CpuLoad", "CPU Temperature"))

