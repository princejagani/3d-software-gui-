
from PyQt5 import QtCore, QtGui, QtWidgets
from db_module import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
import history_basic

class QLabel_alterada(QLabel):
    clicked=pyqtSignal()

    def mousePressEvent(self, ev):
        self.clicked.emit()

class Ui_Form(object):
    def __init__(self,main_widget,Form,list_widget,verticalLayout):
        self.favorite_widget = QtWidgets.QWidget(main_widget)
        self.scroll_fav_model=QScrollArea()
        self.scroll_fav_video=QScrollArea()
        self.vbox1 = QtWidgets.QGridLayout() 
        self.vbox=QtWidgets.QGridLayout()
        self.fav_disp_widget= QtWidgets.QWidget(main_widget)
        self.list_widget=list_widget
        self.form=Form
        self.box=QtWidgets.QGridLayout()
        self.error_widget=QtWidgets.QWidget(main_widget)
        self.verticalLayout=verticalLayout
        self.main_widget=main_widget
        self.status_fav=0
    def setupUi(self,main_widget,gridLayout_4,main_grid_Layout,main_2_horizontalLayout,verticalLayout,big_widget,web1,min_model):
        self.favorite_widget.hide()
        self.big_widget=big_widget
        self.web1=web1
        self.min_model=min_model
        self.gridLayout_4=gridLayout_4
        self.web=QWebView(self.fav_disp_widget)
        self.disp_layout=QtWidgets.QHBoxLayout()
        self.fav_disp_widget.setLayout(self.disp_layout)
        self.disp_layout.setContentsMargins(0, 0, 0, 0)
        self.disp_layout.addWidget(self.web)
        self.favorite_widget.setObjectName("favorite_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.favorite_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fav_model_widget = QtWidgets.QWidget(self.favorite_widget)
        self.fav_model_widget.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.fav_model_widget.setObjectName("fav_model_widget")
        self.horizontalLayout.addWidget(self.scroll_fav_model)
        self.fav_video_widget = QtWidgets.QWidget(self.favorite_widget)
        self.fav_video_widget.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.fav_video_widget.setObjectName("fav_video_widget")
        self.horizontalLayout.addWidget(self.scroll_fav_video)
        gridLayout_4.addWidget(self.favorite_widget, 0, 0, 1, 1)
        main_grid_Layout.addLayout(gridLayout_4, 3, 1, 1, 1)
        # self.mange_widget = QtWidgets.QWidget(main_widget)
        # self.mange_widget.setStyleSheet("background-color: rgb(11, 11, 11);")
        # self.mange_widget.setObjectName("mange_widget")
        # gridLayout_4.addWidget(self.mange_widget, 1, 1, 1, 1)
        # spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        # main_grid_Layout.addItem(spacerItem4, 1, 0, 1, 1)
        self.favarite_label = QtWidgets.QLabel(main_widget)
        self.fav_video_widget.setLayout(self.vbox)
        self.fav_model_widget.setLayout(self.vbox1)
        self.scroll_fav_model.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_fav_model.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_fav_model.setWidgetResizable(True)
        self.scroll_fav_model.setStyleSheet("background-color: rgb(36, 36, 36);border:0px;")
        self.scroll_fav_model.setWidget(self.fav_model_widget)
        self.scroll_fav_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_fav_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_fav_video.setWidgetResizable(True)
        self.scroll_fav_video.setStyleSheet("background-color: rgb(36, 36, 36);border:0px;")
        self.scroll_fav_video.setWidget(self.fav_video_widget)
        
        self.fav_disp_widget.setStyleSheet("background-color: rgb(11,11,11);")
        # self.horizontalLayout.addWidget(self.his_disp_widget)
        self.fav_disp_widget.setObjectName("his_disp_widget")
        gridLayout_4.addWidget(self.fav_disp_widget,0,0,1,1)
#         self.favarite_label.setStyleSheet("color: rgb(255, 255, 255);\n"
# "\n"
# "font: 57 12pt \"Poppins Medium\";")
#         self.favarite_label.setObjectName("favarite_label")
#         main_grid_Layout.addWidget(self.favarite_label, 0, 0, 1, 1)
        main_2_horizontalLayout.addWidget(main_widget)
        verticalLayout.addLayout(main_2_horizontalLayout)
        self.close_btn = QtWidgets.QPushButton(self.web)
        self.close_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb();\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:14px;\n"
"border-color: rgb(62, 62, 62);\n"
"padding:6px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(11, 11, 11);\n"
"}")
        self.close_btn.setText("")
        self.close_btn.clicked.connect(self.close_web)
        self.close_btn.setIconSize(QtCore.QSize(80, 80))
        self.close_btn.setObjectName("close_btn")
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_model=QtGui.QIcon()
        self.icon_model.addPixmap(QtGui.QPixmap("icon/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(self.icon_model)
        self.close_btn.hide()
        
        self.load_data()
        self.max_model = QtWidgets.QPushButton(self.web)
        self.max_model.hide()
        self.max_model.setStyleSheet("QPushButton{\n"
"background-color: rgb(11, 11, 11);\n"
"color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:0px;\n"
"border-radius:14px;\n"
"border-color: rgb(62, 62, 62);\n"
"padding:6px\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(11, 11, 11);\n"
"}")
        self.max_model.setText("")
        
        self.max_model.setIconSize(QtCore.QSize(60, 60))
        self.max_model.setObjectName("max_model")
        self.max_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max_model.clicked.connect(self.max_size)
        self.error_widget.setObjectName("error_widget")
        
        self.error_widget.setLayout(self.box)
        self.error_widget.hide()
        gridLayout_4.addWidget(self.error_widget,0,0,1,1)
        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.favarite_label.setText(_translate("Form", "Favarite"))

    def close_web(self):
        self.fav_disp_widget.hide()
        # self.scroll_his_model.show()
        # self.scroll_his_video.show()
        self.favorite_widget.show()

    def video_render(self,num,id):
        history_basic.count_history(id,'video')
       
        f = open('index1.html','w')
        html_template =f"""<html>

<head>
     <link rel="stylesheet" type="text/css" href="demo.css">

</head>

<body>
    <video controls id="myvideo">
  <source src="C:/xampp/htdocs/main_data/{str(num)}" type="video/webm">
   <source src="small.ogg" type="video/ogg">

</video>


</body>

</html>"""
        f.write(html_template)
        f.close()
        self.url=f"file:///D:/python%20infinite/gltf/3d/index1.html"
        self.web.load(QUrl(self.url))
        self.web.setGeometry(QtCore.QRect(0, 0, 1600, 830))
        self.close_btn.show()
        self.close_btn.raise_()
        self.close_btn.setGeometry(QtCore.QRect(1560, 0, 30, 30))
        # self.scroll_his_model.hide()
        # self.scroll_his_video.hide()
        self.favorite_widget.hide()
        self.fav_disp_widget.show()

    def model_render(self,num,id):
        global url
        history_basic.count_history(id,'model')
        # self.scroll_his_model.hide()
        # self.scroll_his_video.hide()
        self.favorite_widget.hide()
        self.fav_disp_widget.show()
        # self.fav_disp_widget.setMinimumSize(1100,900)
        self.url=f"file:///C:/xampp/htdocs/main_data/{num}/index.html"
        self.web.load(QUrl(self.url))
        url=self.url
        self.web.setGeometry(QtCore.QRect(0, 0, 1600, 830))
        # self.web.show()
        self.close_btn.raise_()
        self.close_btn.show()
        self.max_model.raise_()
        self.max_model.show()
        self.max_model.setGeometry(QtCore.QRect(1580, 840, 30, 30))
        self.close_btn.setGeometry(QtCore.QRect(1585, 0, 30, 30))
        
        self.icon_model.addPixmap(QtGui.QPixmap("icon/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_model.setIcon(self.icon_model) 
        # self.history_widget.hide()

    def max_size(self):
            self.form.showFullScreen()
            for i in self.list_widget:
                i.hide()
            self.main_widget.hide()
            print(self.status_fav)
            self.web1.load(QUrl(url))
            self.big_widget.show()
            self.min_model.show()
            self.min_model.raise_()
            self.min_model.setGeometry(QtCore.QRect(1875, 1030, 40, 40))
            self.min_model.clicked.connect(self.min_size)
            self.icon_model.addPixmap(QtGui.QPixmap("icon/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.min_model.setIcon(self.icon_model)
        
    def min_size(self):
        self.form.showMaximized()
        self.fav_disp_widget.show()
        self.close_btn.show()
        # self.popular_widget.show()
        self.main_widget.show()
        for i in self.list_widget:
            i.show()
        print(self.status_fav)
        self.big_widget.hide()
        self.min_model.hide()
        self.max_model.setGeometry(QtCore.QRect(1580, 840, 30, 30))
        self.close_btn.setGeometry(QtCore.QRect(1585, 0, 30, 30))
        self.icon_model.addPixmap(QtGui.QPixmap("icon/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_model.setIcon(self.icon_model)
        self.status_fav=0

    def fun(self,num,num1,id):
        self.object[num].clicked.connect(lambda:self.video_render(str(num1),id))
   
    def fun1(self,num,num1,id):
        self.object1[num].clicked.connect(lambda:self.model_render(str(num1),id))

    def load_data(self):
        self.norc_text=QtWidgets.QLabel(self.fav_model_widget)
        self.norc1_text=QtWidgets.QLabel(self.fav_disp_widget)
        self.norc2_text=QtWidgets.QLabel(self.fav_video_widget)
        for i in reversed(range(self.vbox.count())):     
                 self.vbox.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.vbox1.count())):     
                 self.vbox1.itemAt(i).widget().setParent(None)  
        for i in reversed(range(self.box.count())):     
                 self.box.itemAt(i).widget().setParent(None)
        xc=0
        yc=10
        xa=0
        ya=10
        self.fav_disp_widget.hide()
        self.favorite_widget.show()
        self.object1=[]
        self.object=[]
        sql=f'SELECT * FROM model_file WHERE favorite=1'
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        if(myresult!=[]):
            self.favorite_widget.show()
            for i in range(0,len(myresult)):
                 self.object1.append(QLabel_alterada(self.fav_model_widget))
            for j in range(0,len(myresult)):
                for y in range(2):
                    self.object1[j] = QLabel_alterada(self.fav_model_widget)
                    self.object1[j].setText(f"{myresult[j][4]}\n{myresult[j][7]}")
                    self.object1[j].setMinimumSize(300,40)
                    self.object1[j].setStyleSheet("color:white;font: 25 9pt \"Poppins Medium\";")
                    self.object1[j].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.object1[j].setScaledContents(True)
                    if(len(myresult)<4):
                        self.object1[j].show()
                        if(y==1):
                            # self.object[j].move(450,0)
                            self.object1[j].setGeometry(480,ya,400,200)
                            ya=ya+205
                    else:
                        self.vbox1.addWidget(self.object1[j],j,y)
                    # self.object1[i].clicked.connect(self.home1)
                    self.object1[j].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    if(y==0):
                        if(len(myresult)<4):
                            self.object1[j].setMinimumSize(QtCore.QSize(470, 200)) 
                            self.object1[j].setGeometry(xc,yc,400,200)
                            yc=yc+205
                        self.object1[j].setPixmap(QtGui.QPixmap(f"C:/xampp/htdocs/main_data/{myresult[j][6]}"))
                        self.object1[j].setMinimumSize(QtCore.QSize(350, 200))
                        self.fun1(j,myresult[j][5],myresult[j][0])
                       
            ya=10
            xc=0
            yc=10
        else:
            self.label_model =QtWidgets.QLabel(self.fav_model_widget)
            self.label_model.setText(f"No Records")
            self.label_model.show()
            self.vbox1.addWidget(self.label_model)
        sql1=f'SELECT * FROM video WHERE favorite=1'
        mycursor.execute(sql1)
        myresult1=mycursor.fetchall()
        
        if(myresult1!=[]):
            for i in range(0,len(myresult1)):
                 self.object.append(QLabel_alterada(self.fav_video_widget))
            for j in range(0,len(myresult1)):
                for y in range(2):
                    
                    self.object[j] = QLabel_alterada(self.fav_video_widget)
                    self.object[j].setText(f"{myresult1[j][4]}\n{myresult1[j][7]}")
                    self.object[j].setMinimumSize(300,40)
                    self.object[j].setStyleSheet("color:white;font: 25 9pt \"Poppins Medium\";")
                    self.object[j].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.object[j].setScaledContents(True)
                    if(len(myresult1)<4):
                        self.object[j].show()
                        if(y==1):
                            # self.object[j].move(450,0)
                            self.object[j].setGeometry(480,ya,400,200)
                            ya=ya+205
                    else:
                        self.vbox.addWidget(self.object[j],j,y)
                    # self.object1[i].clicked.connect(self.home1)
                    self.object[j].setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    
                    if(y==0):
                        if(len(myresult1)<4):
                            self.object[j].setMinimumSize(QtCore.QSize(470, 200)) 
                            self.object[j].setGeometry(xc,yc,400,200)
                            yc=yc+205
                        self.object[j].setPixmap(QtGui.QPixmap(f"C:/xampp/htdocs/main_data/{myresult1[j][6]}"))
                        self.object[j].setMinimumSize(QtCore.QSize(350, 200))
                        self.fun(j,myresult1[j][5],myresult1[j][0])
                        
            xc=0
            yc=10
            ya=10


# import xyz_rc
        if(myresult==[] and myresult1==[]):
            self.favorite_widget.hide()
            self.fav_disp_widget.hide()
            # self.close_btn.hide()
            self.error_widget.show()
            self.norc1_text.setText("No record founded !")
            self.norc1_text.setStyleSheet("color:white;font: 81 15pt \"Poppins ExtraBold\";")
            self.norc1_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop|QtCore.Qt.AlignCenter)
            self.norc1_text.show()
            self.box.addWidget(self.norc1_text)
        elif(myresult==[]):
            self.error_widget.hide()
            self.fav_disp_widget.hide()
            # self.close_btn.hide()
            # self.error_widget.show()
            self.norc_text.setText("No model founded !")
            self.norc_text.setStyleSheet("color:white;font: 81 15pt \"Poppins ExtraBold\";")
            self.norc_text.show()
            self.vbox1.addWidget(self.norc_text)
        elif(myresult1==[]):
            self.error_widget.hide()
            self.fav_disp_widget.hide()
            # self.close_btn.hide()
            # self.error_widget.show()
            self.norc2_text.setText("No video founded !")
            self.norc2_text.setStyleSheet("color:white;font: 81 15pt \"Poppins ExtraBold\";")
            self.norc2_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop|QtCore.Qt.AlignCenter)
            self.norc2_text.show()
            self.vbox.addWidget(self.norc2_text)
