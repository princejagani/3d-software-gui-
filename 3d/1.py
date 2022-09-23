from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import sys
 
def display():
    global count
    count += 1
    if count > 5:
        print("Finished")
        timer.stop()
        return
    print("Hello World")
 
count = 0
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400,400,300,300)
win.setWindowTitle("CodersLegacy")
  
timer = QtCore.QTimer()
timer.timeout.connect(display)
timer.start(1000)
 
 
win.show()
sys.exit(app.exec_())