from PyQt5.QtWidgets import QDialog, QProgressBar, QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSlot
import RPi.GPIO as GPIO

class RpiGpio_Dialog(QDialog):
    def __init__(self, pin):
        super(RpiGpio_Dialog, self).__init__()
        self.pin = pin
        self.init_gpio()
        
    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 0); 
        self.pwm.start(0)
        print("RpiGpio initialized!") 
        
    def closeEvent(self, event):
        self.pwm.stop()
        GPIO.cleanup()
        print("RpiGpio clean up!") 
        super(QDialog, self).closeEvent(event)
        
    def make_connection(self, slider_object):
        slider_object.changedValue.connect(self.get_slider_value)

    @pyqtSlot(int)
    def get_slider_value(self, val):
        self.pwm.ChangeDutyCycle(val)
        print(val)





  
