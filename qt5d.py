# import sys
# from PyQt5.QtWidgets import QApplication,QWidget

# if __name__ == "__main__":
# 	app = QApplication(sys.argv)

# 	w = QWidget()
# 	w.resize(800,600)
# 	w.move(300,300)
# 	w.setWindowTitle("Simple")
# 	w.show()

# 	sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip, 
#     QPushButton, QApplication)
# from PyQt5.QtGui import QFont    


# class Example(QWidget):
    
#     def __init__(self):
#         super().__init__()
        
#         self.initUI()
        
        
#     def initUI(self):
        
#         QToolTip.setFont(QFont('SansSerif', 10))
        
#         self.setToolTip('This is a <b>QWidget</b> widget')
        
#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)       
        
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Tooltips')    
#         self.show()
        
        
# if __name__ == '__main__':
    
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


# class Example(QWidget):
    
#     def __init__(self):
#         super().__init__()
        
#         self.initUI()
        
        
#     def initUI(self):               
        
#         self.setGeometry(300, 300, 250, 150)        
#         self.setWindowTitle('Message box')    
#         self.show()
        
        
#     def closeEvent(self, event):
        
#         reply = QMessageBox.question(self, 'Message',
#             "Are you sure to quit?", QMessageBox.Yes | 
#             QMessageBox.No, QMessageBox.No)

#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()        
        
        
# if __name__ == '__main__':
    
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
    	
        title = QLabel('Title')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1, 1, 1)


        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.resize(800,600)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

