# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 1000, 800)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a push button
        button = QPushButton("CLICK", self)
  
        # setting geometry of button
        button.setGeometry(10, 15, 100, 40)
  
        # adding action to a button
        button.clicked.connect(self.clickme)
  
        # setting background image
        button.setStyleSheet("background-image : url(icon/20200103_232614.jpg);")
  
        # resizing button according to size of image
        button.resize(724, 430)
  
    # action method
    def clickme(self):
  
        # printing pressed
        print("pressed")
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())