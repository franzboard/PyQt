#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Show CPU temperature of Raspberry Pi and control GPIOs - QML version
Edgar Neukirchner 2020
"""

# BCM numbering
LEDS = [18, 23, 24, 25]
BUTTONS = [22, 27, 17]
SYSFS_TEMP = "/sys/class/thermal/thermal_zone0/temp"

import sys
from os.path import abspath, dirname, join
from PySide2.QtCore import QUrl, QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from gpiozero import LEDBoard, ButtonBoard

from style_rc import * # material design

class Monitor(QObject):
    # constructor
    def __init__(self):
        super().__init__() # Initialize base class first
        self.leds = LEDBoard(*LEDS)
        self.buttons = ButtonBoard(*BUTTONS)
        self.state = [0, 0, 0, 0]

    # slots are controlled by timer in monitor.qml
    # temperature from sysfs
    @Slot(result=str)
    def getTemperature(self):
        with open(SYSFS_TEMP, 'rt') as fh:
            temp = int(fh.readline()) / 1000.0
        return str(round(temp)) + " °C"

    # outputs control LEDs
    @Slot(int, result=int)
    def toggleLed(self, number):
        self.state[number] = 1 - self.state[number]
        if self.state[number] == 1:
            self.leds[number].on()
        else:
            self.leds[number].off()
        return self.state[number]

    # input read buttons
    @Slot(int, result=int)
    def readButton(self, number):
        return self.buttons[number].value

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    monitor = Monitor()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", monitor)

    engine.load(QUrl("monitor.qml"))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())





