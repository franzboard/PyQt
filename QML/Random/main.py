#!/usr/bin/env python3
import sys
import random
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class NumberGenerator(QObject):
    def __init__(self):
        QObject.__init__(self)

    nextNumber = pyqtSignal(int, arguments=['giveNumber'])

    @pyqtSlot()
    def giveNumber(self):
        self.nextNumber.emit(random.randint(0, 99))

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    numbergenerator = NumberGenerator()
    engine.rootContext().setContextProperty("numbergenerator", numbergenerator)
    engine.load("main.qml")
    if not engine.rootObjects():
        sys.exit(-1)    
    sys.exit(app.exec_())
