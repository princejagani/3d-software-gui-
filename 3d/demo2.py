# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(982, 1009)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_1_horizontalLayout = QtWidgets.QHBoxLayout()
        self.main_1_horizontalLayout.setObjectName("main_1_horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.main_1_horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.main_1_horizontalLayout)
        self.main_2_horizontalLayout = QtWidgets.QHBoxLayout()
        self.main_2_horizontalLayout.setSpacing(0)
        self.main_2_horizontalLayout.setObjectName("main_2_horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(173, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.main_2_horizontalLayout.addItem(spacerItem1)
        self.left_widget = QtWidgets.QWidget(Form)
        self.left_widget.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.left_widget.setObjectName("left_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_2_horizontalLayout.addWidget(self.left_widget)
        self.main_widget = QtWidgets.QWidget(Form)
        self.main_widget.setStyleSheet("background-color:  rgb(11,11,11);")
        self.main_widget.setObjectName("main_widget")
        self.main_grid_Layout = QtWidgets.QGridLayout(self.main_widget)
        self.main_grid_Layout.setContentsMargins(9, 9, 9, 9)
        self.main_grid_Layout.setObjectName("main_grid_Layout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_grid_Layout.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mange_widget = QtWidgets.QWidget(self.main_widget)
        self.mange_widget.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.mange_widget.setObjectName("mange_widget")
        self.gridLayout_4.addWidget(self.mange_widget, 1, 1, 1, 1)
        self.model_all_widget = QtWidgets.QWidget(self.main_widget)
        self.model_all_widget.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.model_all_widget.setObjectName("model_all_widget")
        self.all_grid_Layout = QtWidgets.QGridLayout(self.model_all_widget)
        self.all_grid_Layout.setContentsMargins(0, 0, 0, 0)
        self.all_grid_Layout.setObjectName("all_grid_Layout")
        self.model_widget = QtWidgets.QWidget(self.model_all_widget)
        self.model_widget.setStyleSheet("\n"
"\n"
"background-color:  rgb(11,11,11);")
        self.model_widget.setObjectName("model_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.model_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.model_widget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 3px solid  rgb(72, 72, 72);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.model_widget)
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.cd_btn = QtWidgets.QPushButton(self.model_widget)
        self.cd_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cd_btn.setStyleSheet("QPushButton{\n"
"\n"
"background-color:  rgb(11,11,11);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:4.5px;\n"
"border-radius:12px;\n"
"border-color: rgb(182, 182, 182);\n"
"padding:6px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(106, 106, 106);\n"
"}\n"
"\n"
"")
        self.cd_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/cd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cd_btn.setIcon(icon)
        self.cd_btn.setIconSize(QtCore.QSize(150, 150))
        self.cd_btn.setObjectName("cd_btn")
        self.gridLayout.addWidget(self.cd_btn, 0, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 2, 1, 1)
        self.internet_btn = QtWidgets.QPushButton(self.model_widget)
        self.internet_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.internet_btn.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"background-color:  rgb(11,11,11);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:4.5px;\n"
"border-radius:12px;\n"
"border-color: rgb(182, 182, 182);\n"
"padding:6px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(106, 106, 106);\n"
"}\n"
"\n"
"\n"
"/*\n"
"QPushButton{\n"
"background-color:rgb(11, 11, 11);\n"
"color: rgb(255, 255, 255);\n"
"border-style:solid ;\n"
"border-width:5px;\n"
"border-radius:0px;\n"
"border-color:rgb(11, 11, 11);\n"
"\n"
"}\n"
"QpushButton:focus{\n"
"\n"
"    border-color: rgb(106, 106, 106);\n"
"}\n"
"*/")
        self.internet_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/internet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.internet_btn.setIcon(icon1)
        self.internet_btn.setIconSize(QtCore.QSize(150, 150))
        self.internet_btn.setObjectName("internet_btn")
        self.gridLayout.addWidget(self.internet_btn, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.model_widget)
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.model_widget)
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.all_grid_Layout.addWidget(self.model_widget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.model_all_widget, 0, 0, 1, 1)
        self.main_grid_Layout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.main_2_horizontalLayout.addWidget(self.main_widget)
        self.verticalLayout.addLayout(self.main_2_horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Import new Models / Videos..."))
        self.label_2.setText(_translate("Form", "How would you like to import new Models?"))
        self.label_3.setText(_translate("Form", "Internet"))
        self.label_4.setText(_translate("Form", "CD / USB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
