from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class Window(QWidget):
	def __init__(self):
		super(Window,self).__init__()

		self.resize(800,600)
		self.setWindowTitle("Windows")
		self.setWindowIcon(QIcon("./wifi.ico"))

app = QApplication(sys.argv)
win = Window()
win.show()
app.exec()