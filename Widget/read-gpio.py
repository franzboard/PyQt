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
import RPi.GPIO as GPIO
import time
import sys
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from PyQt5.QtWidgets import QWidget, QLCDNumber, QVBoxLayout, QApplication
        
class RpiGpioIn(QObject): 
    """ Read Raspberry Pi Hardware """  
    changed = pyqtSignal(int)
    
    def __init__(self, pin):
        self.pin = pin
        QObject.__init__(self)
        self.init_gpio()
        
    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.gpio_change)
        print("RpiGpio initialized!")  
         
    def cleanup(self):
        GPIO.remove_event_detect(self.pin)
        GPIO.cleanup()
        print("RpiGpio clean up!") 
        
    def gpio_change(self, pin):
        value = 1 - GPIO.input(pin)
        print(value)
        self.changed.emit(value)
        
    
class Display(QWidget):
    """ Displays input pin state """
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.display(0)
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        self.setLayout(vbox)        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Gpio Input')
        self.show()
        
    @pyqtSlot(int)
    def get_value(self, val):
        self.lcd.display(val)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    display = Display()
    rpiPin = RpiGpioIn(22)
    rpiPin.changed.connect(display.get_value)
    ret = app.exec_()
    rpiPin.cleanup()
    sys.exit(ret)

















