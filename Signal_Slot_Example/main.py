from SliderDialog.Slider import Slider_Dialog
from ProgressDialog.Progress import ProgressBar_Dialog
from RpiGpioDialog.RpiGpio import RpiGpio_Dialog
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sd = Slider_Dialog()
    pb = ProgressBar_Dialog()
    gpio = RpiGpio_Dialog()
    # Making the connection
    pb.make_connection(sd)
    gpio.make_connection(sd)
    sys.exit(app.exec_())
