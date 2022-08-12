from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self,Form,wid,lay,main_grid,h_lay,v_lay):
        self.model_all_widget = QtWidgets.QWidget(wid)
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
        lay.addWidget(self.model_all_widget, 0, 0, 1, 1)
        main_grid.addLayout(lay, 1, 0, 1, 1)
        h_lay.addWidget(wid)
        v_lay.addLayout(h_lay)
        self.retranslateUi()
        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Import new Models / Videos..."))
        self.label_2.setText(_translate("Form", "How would you like to import new Models?"))
        self.label_3.setText(_translate("Form", "Internet"))
        self.label_4.setText(_translate("Form", "CD / USB"))

