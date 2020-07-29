#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stopwatch - QML version
Edgar Neukirchner 2020
"""
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, QElapsedTimer, QTime, QTimer, pyqtSignal, pyqtSlot

from style_rc import * # material design

class Stopwatch(QObject):
    newTime = pyqtSignal(str, arguments = ['displayTime'])

    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.delta = QElapsedTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.displayTime)

    @pyqtSlot()
    def displayTime(self):        
        t = QTime(0, 0, 0)
        displayTxt = t.addMSecs(self.delta.elapsed()).toString('hh:mm:ss')
        self.newTime.emit(displayTxt)

    @pyqtSlot()
    def start(self):
        self.delta.start()
        self.timer.start()

    @pyqtSlot()
    def stop(self):
        self.timer.stop()


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    stopwatch = Stopwatch()
    context = engine.rootContext()
    context.setContextProperty("stopwatch", stopwatch)
    engine.load("view.qml")
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())





