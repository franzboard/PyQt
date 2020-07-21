#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Show CPU load and temperature of Raspberry PI
Edgar Neukirchner 2018
"""
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer

import sys
import psutil
from ui_cpuload import Ui_CpuLoad

SYSFS_TEMP = "/sys/class/thermal/thermal_zone0/temp"

class CpuLoad(QWidget, Ui_CpuLoad):
    def __init__(self):
        super(CpuLoad, self).__init__()
        self.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.update_values)
        timer.start(1000)

    def update_values(self):
        # load in percent
        loads = psutil.cpu_percent(interval = 0.1, percpu = True)
        n = len(loads) # number of CPUs depends on Pi model

        self.cpu1.setValue(round(loads[0]))
        if (n > 1):
            self.cpu2.setValue(round(loads[1]))
        if (n > 2):
            self.cpu3.setValue(round(loads[2]))
        if (n > 3):
            self.cpu4.setValue(round(loads[3]))

        # temperature from sysfs
        with open(SYSFS_TEMP, 'rt') as fh:
            temp = int(fh.readline()) / 1000.0
        self.lcdNumber.display(round(temp))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    panel = CpuLoad()
    panel.show()
    ret = app.exec_()
    sys.exit(ret)

