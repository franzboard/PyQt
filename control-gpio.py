#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber 
and to a slot of RpiGpio.

This shows how Qt interacts with
Raspberry Pi GPIO pins

Author: Edgar Neukirchner
Last edited: October 2017
"""

import sys
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
                                QVBoxLayout, QApplication)
import RPi.GPIO as GPIO

class ControlPanel(QWidget):
    """ Graphical User Interface """

    valueChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        sld.valueChanged.connect(self.on_changed_value)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Pi Control')
        self.show()
        
    def on_changed_value(self, value):
        self.valueChanged.emit(value)


class RpiGpio(QObject): 
    """ Control Raspberry Pi Hardware """  
    def __init__(self, pin):
        self.pin = pin
        QObject.__init__(self)
        self.init_gpio()
        
    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50); 
        self.pwm.start(50)
        print("RpiGpio initialized!")  
         
    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
        print("RpiGpio clean up!") 
            
    @pyqtSlot(int)
    def set_value(self, value):
        print(self.pin, " ->" , value)
        self.pwm.ChangeDutyCycle(value)
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    panel = ControlPanel()
    rpiPin = RpiGpio(18)
    panel.valueChanged.connect(rpiPin.set_value)
    ret = app.exec_()
    rpiPin.cleanup()
    sys.exit(ret)

