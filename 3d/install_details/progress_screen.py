# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import company_details
import time
from PyQt5.QtCore import Qt
class Ui_Form(object):
    def __init__(self):
        self.main_widget = QtWidgets.QWidget(Form)
        self.all_widget = QtWidgets.QWidget(self.main_widget)
        self.start_progressBar = QtWidgets.QProgressBar(self.all_widget)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        
    def company_page(self):
        self.all_widget.hide()
        self.load_company=company_details.Ui_Form(self.main_widget,self.gridLayout_2,self.gridLayout)
        self.load_company.setupUi()
        
    def progress(self):
        
        for i in range(101):
            print(i)
            time.sleep(0.01)
            self.start_progressBar.setValue(i)
            if(self.start_progressBar.value()==100):
                self.company_page()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1037, 565)
        Form.setWindowFlag(Qt.FramelessWindowHint)
        # Form.setMinimumSize(QtCore.QSize(839, 925))
        Form.setMinimumSize(QtCore.QSize(1037, 565))
        Form.setMaximumSize(QtCore.QSize(1037, 565))
        # Form.setMaximumSize(QtCore.QSize(839, 1665))
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        # self.main_widget = QtWidgets.QWidget(Form)
        self.main_widget.setObjectName("main_widget")
        # self.gridLayout_2 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_2.setContentsMargins(0, 7, 0, 7)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # self.all_widget = QtWidgets.QWidget(self.main_widget)
        self.all_widget.setObjectName("all_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.all_widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.all_widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/3d-01.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

#         self.version_label = QtWidgets.QLabel(Form)
#         self.version_label.setGeometry(360, 290, 300, 20)
#         self.version_label.setStyleSheet("\n"
# "background-image: url(:/newPrefix/icon/text.png);\n"
# "color: rgb(255, 255, 255);\n"
# "font: 57 13pt \"Poppins SemiBold\";")
#         self.version_label.setObjectName("version_label")
        # self.start_progressBar = QtWidgets.QProgressBar(self.all_widget)
        self.start_progressBar.setGeometry(420, 290, 300, 20)
        self.start_progressBar.show()
        self.start_progressBar.setStyleSheet("\n"
"\n"
"QProgressBar\n"
"{\n"
"\n"
"background-image: url(:/newPrefix/icon/text.png);\n"
"    background-color: rgb(53, 53, 53);\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-align:center;\n"
"border-radius :10px;\n"
"\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color:rgb(248,180,100);\n"
"border-radius :10px;\n"
"}  ")
        # self.start_progressBar.setProperty("value", 0)
        # self.start_progressBar.setMaximum(100)
        self.start_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.start_progressBar.setObjectName("start_progressBar")
        self.start_progressBar.setProperty("value", 0)
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.all_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
       
    def retranslateUi(self, Form):
        
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.version_label.setText(_translate("Form", "V .1.0"))
import xyz_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

    
