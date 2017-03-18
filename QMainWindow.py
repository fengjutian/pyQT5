import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidge(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(1200,800)
		self.setWindowTitle("myapp")

		menu_control = self.menuBar().addMenu("Control")
		act_quit = menu_control.addAction("quit")
		act_quit.triggered.connect(self.close)


		self.statusBar().showMessage("程序已就绪。。。。。。")
		self.show()

    

myapp = QApplication(sys.argv)
mywidge = MyWidge()
sys.exit(myapp.exec_())
