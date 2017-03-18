from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):
	def __init__(self):
		super(Window,self).__init__()

		#设置大小
		self.resize(1200,800)
		#居中显示
		self.center()
		#设置名称
		self.setWindowTitle("Windows")
		#设置图标
		self.setWindowIcon(QIcon("./network.png"))
		# self.setToolTip("弹窗")
		# QToolTip.setFont(QFont("微软雅黑",12))
	def center(self):
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())