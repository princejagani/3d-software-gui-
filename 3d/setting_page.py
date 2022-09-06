# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from db_module import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
import history_basic
import json
import install_details.fetch_api_data

class Ui_Form(object):
    def __init__(self,main_widget):
        self.settind_all_widget = QtWidgets.QWidget(main_widget)

    def setupUi(self,main_widget,gridLayout_4,main_grid_Layout,main_2_horizontalLayout,verticalLayout):
        self.settind_all_widget.show()
        self.settind_all_widget.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.settind_all_widget.setObjectName("settind_all_widget")
        self.all_grid_Layout = QtWidgets.QGridLayout(self.settind_all_widget)
        self.all_grid_Layout.setContentsMargins(0, 0, 0, 0)
        self.all_grid_Layout.setObjectName("all_grid_Layout")
        self.setting_model_widget = QtWidgets.QWidget(self.settind_all_widget)
        self.setting_model_widget.setStyleSheet("\n"
"\n"
"background-color:  rgb(11,11,11);")
        self.setting_model_widget.setObjectName("setting_model_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.setting_model_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(5, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.title_label = QtWidgets.QLabel(self.setting_model_widget)
        self.title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_label.setStyleSheet("\n"
"font: 81 15pt \"Poppins ExtraBold\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 3px solid  rgb(72, 72, 72);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem10, 3, 2, 1, 1)
        self.user_groupBox = QtWidgets.QGroupBox(self.setting_model_widget)
        self.user_groupBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.user_groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user_groupBox.setStyleSheet("QGroupBox{\n"
"\n"
"    font: 57 12pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"/*border-radius:12px;*/\n"
"QGroupBox:focus\n"
"{\n"
"border: 5px solid 10px QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.user_groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.user_groupBox.setCheckable(False)
        self.user_groupBox.setObjectName("user_groupBox")
        self.user_details_verticalLayout = QtWidgets.QVBoxLayout(self.user_groupBox)
        self.user_details_verticalLayout.setContentsMargins(0, 0, 0, 9)
        self.user_details_verticalLayout.setObjectName("user_details_verticalLayout")
        self.user_details_widget = QtWidgets.QWidget(self.user_groupBox)
        self.user_details_widget.setStyleSheet("background-color: rgb(11,11,11);")
        self.user_details_widget.setObjectName("user_details_widget")
        self.user_details_widget_gridLayout = QtWidgets.QGridLayout(self.user_details_widget)
        self.user_details_widget_gridLayout.setObjectName("user_details_widget_gridLayout")
        self.demo_address_label = QtWidgets.QLabel(self.user_details_widget)
        self.demo_address_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_address_label.setObjectName("demo_address_label")
        self.user_details_widget_gridLayout.addWidget(self.demo_address_label, 2, 1, 1, 1)
        self.demo_phone_number_label = QtWidgets.QLabel(self.user_details_widget)
        self.demo_phone_number_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_phone_number_label.setObjectName("demo_phone_number_label")
        self.user_details_widget_gridLayout.addWidget(self.demo_phone_number_label, 3, 1, 1, 1)
        self.demo_company_name_label_2 = QtWidgets.QLabel(self.user_details_widget)
        self.demo_company_name_label_2.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_company_name_label_2.setObjectName("demo_company_name_label_2")
        self.user_details_widget_gridLayout.addWidget(self.demo_company_name_label_2, 4, 1, 1, 1)
        self.name_label = QtWidgets.QLabel(self.user_details_widget)
        self.name_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.name_label.setObjectName("name_label")
        self.user_details_widget_gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.demo_mail_label = QtWidgets.QLabel(self.user_details_widget)
        self.demo_mail_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_mail_label.setObjectName("demo_mail_label")
        self.user_details_widget_gridLayout.addWidget(self.demo_mail_label, 5, 1, 1, 1)
        self.address_label = QtWidgets.QLabel(self.user_details_widget)
        self.address_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"background-color: rgb(11,11,11);\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"")
        self.address_label.setObjectName("address_label")
        self.user_details_widget_gridLayout.addWidget(self.address_label, 2, 0, 1, 1)
        self.phone_number_label = QtWidgets.QLabel(self.user_details_widget)
        self.phone_number_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);\n"
"")
        self.phone_number_label.setObjectName("phone_number_label")
        self.user_details_widget_gridLayout.addWidget(self.phone_number_label, 3, 0, 1, 1)
        self.mail_label = QtWidgets.QLabel(self.user_details_widget)
        self.mail_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.mail_label.setObjectName("mail_label")
        self.user_details_widget_gridLayout.addWidget(self.mail_label, 5, 0, 1, 1)
        self.company_name_label = QtWidgets.QLabel(self.user_details_widget)
        self.company_name_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.company_name_label.setObjectName("company_name_label")
        self.user_details_widget_gridLayout.addWidget(self.company_name_label, 4, 0, 1, 1)
        self.demo_name_label = QtWidgets.QLabel(self.user_details_widget)
        self.demo_name_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_name_label.setObjectName("demo_name_label")
        self.user_details_widget_gridLayout.addWidget(self.demo_name_label, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.user_details_widget_gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        self.user_details_verticalLayout.addWidget(self.user_details_widget)
        self.gridLayout.addWidget(self.user_groupBox, 0, 1, 1, 1)
        self.license_groupBox = QtWidgets.QGroupBox(self.setting_model_widget)
        self.license_groupBox.setStyleSheet("/*border-style:solid;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width:2px;\n"
"border-radius:12px;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(11,11,11);*/\n"
"\n"
"QGroupBox{\n"
"\n"
"    font: 57 12pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"/*border-radius:12px;*/\n"
"QGroupBox:focus\n"
"{\n"
"border: 5px solid 10px QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.license_groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.license_groupBox.setObjectName("license_groupBox")
        self.license_details_verticalLayout = QtWidgets.QVBoxLayout(self.license_groupBox)
        self.license_details_verticalLayout.setContentsMargins(0, 0, 0, 9)
        self.license_details_verticalLayout.setObjectName("license_details_verticalLayout")
        self.license_details_widget = QtWidgets.QWidget(self.license_groupBox)
        self.license_details_widget.setStyleSheet("background-color: rgb(11,11,11);")
        self.license_details_widget.setObjectName("license_details_widget")
        self.license_details_widget_gridLayout = QtWidgets.QGridLayout(self.license_details_widget)
        self.license_details_widget_gridLayout.setObjectName("license_details_widget_gridLayout")
        self.demo_mac_label = QtWidgets.QLabel(self.license_details_widget)
        self.demo_mac_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_mac_label.setObjectName("demo_mac_label")
        self.license_details_widget_gridLayout.addWidget(self.demo_mac_label, 4, 1, 1, 1)
        self.demo_expiry_date_label = QtWidgets.QLabel(self.license_details_widget)
        self.demo_expiry_date_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_expiry_date_label.setObjectName("demo_expiry_date_label")
        self.license_details_widget_gridLayout.addWidget(self.demo_expiry_date_label, 3, 1, 1, 1)
        self.demo_license_label = QtWidgets.QLabel(self.license_details_widget)
        self.demo_license_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_license_label.setObjectName("demo_license_label")
        self.license_details_widget_gridLayout.addWidget(self.demo_license_label, 0, 1, 1, 1)
        self.demo_registration_data_label = QtWidgets.QLabel(self.license_details_widget)
        self.demo_registration_data_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_registration_data_label.setObjectName("demo_registration_data_label")
        self.license_details_widget_gridLayout.addWidget(self.demo_registration_data_label, 2, 1, 1, 1)
        self.demo_qty_label = QtWidgets.QLabel(self.license_details_widget)
        self.demo_qty_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(11,11,11);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"text-aling:center;\n"
"\n"
"")
        self.demo_qty_label.setObjectName("demo_qty_label")
        self.license_details_widget_gridLayout.addWidget(self.demo_qty_label, 1, 1, 1, 1)
        self.mac_label = QtWidgets.QLabel(self.license_details_widget)
        self.mac_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.mac_label.setObjectName("mac_label")
        self.license_details_widget_gridLayout.addWidget(self.mac_label, 4, 0, 1, 1)
        self.qty_label = QtWidgets.QLabel(self.license_details_widget)
        self.qty_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.qty_label.setObjectName("qty_label")
        self.license_details_widget_gridLayout.addWidget(self.qty_label, 1, 0, 1, 1)
        self.expiry_date_label = QtWidgets.QLabel(self.license_details_widget)
        self.expiry_date_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.expiry_date_label.setObjectName("expiry_date_label")
        self.license_details_widget_gridLayout.addWidget(self.expiry_date_label, 3, 0, 1, 1)
        self.license_label = QtWidgets.QLabel(self.license_details_widget)
        self.license_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.license_label.setObjectName("license_label")
        self.license_details_widget_gridLayout.addWidget(self.license_label, 0, 0, 1, 1)
        self.registration_date_label = QtWidgets.QLabel(self.license_details_widget)
        self.registration_date_label.setStyleSheet("font: 57 10pt \"Poppins Medium\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"background-color: rgb(11,11,11);")
        self.registration_date_label.setObjectName("registration_date_label")
        self.license_details_widget_gridLayout.addWidget(self.registration_date_label, 2, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.license_details_widget_gridLayout.addItem(spacerItem12, 0, 2, 1, 1)
        self.license_details_verticalLayout.addWidget(self.license_details_widget)
        self.gridLayout.addWidget(self.license_groupBox, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.all_grid_Layout.addWidget(self.setting_model_widget, 0, 0, 1, 1)
        gridLayout_4.addWidget(self.settind_all_widget, 0, 0, 1, 1)
        main_grid_Layout.addLayout(gridLayout_4, 1, 0, 1, 1)
        main_2_horizontalLayout.addWidget(main_widget)
        verticalLayout.addLayout(main_2_horizontalLayout)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        s=open('setting.json')
        data = json.load(s)
        s1=open('setting1.json')
        data1=json.load(s1)
        s2=open('key.json')
        data2=json.load(s2)

        self.name=data['customer_name']
        self.add=data['address1']
        print("cmp",install_details.fetch_api_data.company_name)
        self.company_name=data['company_name']
        self.phone=data['mobile']
        self.emial=data['email']
        self.license='Volume licenses'
        self.qty="100"
        self.reg_date=data1['Startdate']
        self.expire=data1['Enddate']
        self.system=data2['active_user_license']['mac_address']
        _translate = QtCore.QCoreApplication.translate
        self.title_label.setText(_translate("Form", "Settings"))
        self.user_groupBox.setTitle(_translate("Form", "User Details"))
        self.demo_address_label.setText(_translate("Form", self.add))
        self.demo_phone_number_label.setText(_translate("Form", self.phone))
        self.demo_company_name_label_2.setText(_translate("Form", self.company_name))
        self.name_label.setText(_translate("Form", "Name :"))
        self.demo_mail_label.setText(_translate("Form", self.emial))
        self.address_label.setText(_translate("Form", "Address :"))
        self.phone_number_label.setText(_translate("Form", "Phone Number :"))
        self.mail_label.setText(_translate("Form", "Email Address :"))
        self.company_name_label.setText(_translate("Form", "Company Name :"))
        self.demo_name_label.setText(_translate("Form", self.name))
        self.license_groupBox.setTitle(_translate("Form", "License Details"))
        self.demo_mac_label.setText(_translate("Form", self.system))
        self.demo_expiry_date_label.setText(_translate("Form", self.expire))
        self.demo_license_label.setText(_translate("Form", self.license))
        self.demo_registration_data_label.setText(_translate("Form", self.reg_date))
        self.demo_qty_label.setText(_translate("Form", self.qty))
        self.mac_label.setText(_translate("Form", "System MAC :"))
        self.qty_label.setText(_translate("Form", "Qty :"))
        self.expiry_date_label.setText(_translate("Form", "Expiry Date :"))
        self.license_label.setText(_translate("Form", "License Type :"))
        self.registration_date_label.setText(_translate("Form", "Registration Date :"))


