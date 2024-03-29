# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index_4.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import finsh_page
import user_details
class Ui_Form(object):
    def __init__(self,main_widget,gridLayout_2,gridLayout):
        self.main_widget=main_widget
        self.gridLayout_2=gridLayout_2
        self.gridLayout=gridLayout
        self.data=''
    def user_page(self):
        self.all_widget.hide()
        self.load_user=user_details.Ui_Form(self.main_widget,self.gridLayout_2,self.gridLayout,self.data)
        self.load_user.setupUi()
    def finish_page(self):
        self.all_widget.hide()
        self.load_finish=finsh_page.Ui_Form(self.main_widget,self.gridLayout_2,self.gridLayout)
        self.load_finish.setupUi()
    def setupUi(self):
        self.all_widget = QtWidgets.QWidget(self.main_widget)
        self.all_widget.setObjectName("all_widget")
        self.all_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.all_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_gridLayout = QtWidgets.QGridLayout()
        self.top_gridLayout.setObjectName("top_gridLayout")
        self.label_3 = QtWidgets.QLabel(self.all_widget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("icon/Untitled_page-0003.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.top_gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.top_gridLayout)
        self.bottom_gridLayout = QtWidgets.QGridLayout()
        self.bottom_gridLayout.setSpacing(0)
        self.bottom_gridLayout.setObjectName("bottom_gridLayout")
        self.next_btn = QtWidgets.QPushButton(self.all_widget)
        self.next_btn.clicked.connect(self.finish_page)
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_btn.setStyleSheet("QPushButton{\n"
"\n"
"background-color:  rgb(248,180,100);\n"
"color: rgb(255, 255, 255);\n"
"    \n"
"    font: 63 12pt \"Poppins SemiBold\";\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:17px;\n"
"border-color: rgb(62, 62, 62);\n"
"padding:6px\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"\n"
"    background-color: rgb(248, 207, 135);\n"
"}\n"
"")
        self.next_btn.setObjectName("next_btn")
        self.bottom_gridLayout.addWidget(self.next_btn, 4, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem1, 3, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.all_widget)
        self.label_2.setStyleSheet("\n"
"color: rgb(166, 166, 166);\n"
"font: 57 10pt \"Poppins Medium\";\n"
"\n"
"\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.bottom_gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem4, 3, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem5, 1, 4, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(self.all_widget)
        self.name_lineEdit.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"\n"
"\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:7px;\n"
"\n"
"border-color: rgb(62, 62, 62);\n"
"font: 57 10pt \"Poppins Medium\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:focus{\n"
"/*\n"
"background-color:  rgb(248,180,100);\n"
"*/\n"
"\n"
"    background-color: rgb(248, 221, 158);\n"
"}")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.bottom_gridLayout.addWidget(self.name_lineEdit, 0, 4, 1, 1)
        self.previous_btn = QtWidgets.QPushButton(self.all_widget)
        self.previous_btn.clicked.connect(self.user_page)
        self.previous_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previous_btn.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);\n"
"\n"
"font: 57 11pt \"Poppins Medium\";\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-radius:17px;\n"
"border-color: rgb(62, 62, 62);\n"
"padding:6px\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"\n"
"    background-color: rgb(248, 207, 135);\n"
"}\n"
"")
        self.previous_btn.setObjectName("previous_btn")
        self.bottom_gridLayout.addWidget(self.previous_btn, 4, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.bottom_gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.all_widget)
        self.checkBox.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(166, 166, 166);")
        self.checkBox.setObjectName("checkBox")
        self.bottom_gridLayout.addWidget(self.checkBox, 2, 2, 1, 3)
        self.verticalLayout.addLayout(self.bottom_gridLayout)
        self.gridLayout_2.addWidget(self.all_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.next_btn.setText(_translate("Form", "Next"))
        self.label_2.setText(_translate("Form", "Installation Path :"))
        self.previous_btn.setText(_translate("Form", "Previous"))
        self.checkBox.setText(_translate("Form", "Create Desktop Shortcut"))
import xyz_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
