
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
        self.history_widget = QtWidgets.QWidget(main_widget)
        self.scroll_his_model=QScrollArea()
        self.scroll_his_video=QScrollArea()
        self.vbox1 = QtWidgets.QGridLayout() 
        self.vbox=QtWidgets.QGridLayout()
        self.history_main_title_widget = QtWidgets.QWidget(main_widget)
        self.his_disp_widget= QtWidgets.QWidget(main_widget)
        self.main_widget=main_widget
        self.status=0
        self.form=Form
        self.list_widget=list_widget
        self.verticalLayout=verticalLayout

    def setupUi(self,main_widget,gridLayout_4,main_grid_Layout,main_2_horizontalLayout,verticalLayout,big_widget,web1,min_model):
        # self.history_widget = QtWidgets.QWidget(main_widget)
        self.gridLayout_4=gridLayout_4
        self.big_widget=big_widget
        self.web1=web1
        self.min_model=min_model
        self.disp_layout=QtWidgets.QHBoxLayout()
        self.disp_layout.setContentsMargins(0, 0, 0, 0)
        self.history_widget.setObjectName("history_widget")
        self.history_widget.show()
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.history_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.history_model_widget = QtWidgets.QWidget(self.scroll_his_model)
        self.history_model_widget.setStyleSheet("background-color: rgb(11,11,11);")
        self.history_model_widget.setObjectName("history_model_widget")
        self.history_model_widget.setLayout(self.vbox1)
        self.horizontalLayout.addWidget(self.scroll_his_model)
        self.history_video_widget = QtWidgets.QWidget(self.scroll_his_video)
        self.history_video_widget.setStyleSheet("background-color: rgb(11,11,11);")
        self.history_video_widget.setObjectName("history_video_widget")
        self.history_video_widget.setLayout(self.vbox)
        self.horizontalLayout.addWidget(self.scroll_his_video)
        # self.scroll_his.setMinimumSize(QtCore.QSize(600, 0))
        # self.scroll_his.setMaximumSize(QtCore.QSize(600, 16777215))
        self.scroll_his_model.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_his_model.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_his_model.setWidgetResizable(True)
        self.scroll_his_model.setStyleSheet("background-color: rgb(36, 36, 36);border:0px;")
        self.scroll_his_model.setWidget(self.history_model_widget)
        self.scroll_his_video.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_his_video.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_his_video.setWidgetResizable(True)
        self.scroll_his_video.setStyleSheet("background-color: rgb(36, 36, 36);border:0px;")
        self.scroll_his_video.setWidget(self.history_video_widget) 
        self.his_disp_widget.setStyleSheet("background-color: rgb(11,11,11);")
        # self.horizontalLayout.addWidget(self.his_disp_widget)
        self.his_disp_widget.setObjectName("his_disp_widget")
        # self.his_disp_widget.hide()
        self.web=QWebView(self.his_disp_widget)
        gridLayout_4.addWidget(self.history_widget, 0, 0, 1, 1)
        gridLayout_4.addWidget(self.his_disp_widget,0,0,1,1)
        main_grid_Layout.addLayout(gridLayout_4, 2, 0, 1, 1)
        self.history_main_title_widget.show()
        self.history_main_title_widget.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.history_main_title_widget.setObjectName("history_main_title_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.history_main_title_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.history_label = QtWidgets.QLabel(self.history_main_title_widget)
        self.history_label.setStyleSheet("font: 81 15pt \"Poppins ExtraBold\";\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 3px solid rgb(72, 72, 72);")
        self.history_label.setAlignment(QtCore.Qt.AlignCenter)
        self.history_label.setObjectName("history_label")
        self.horizontalLayout_2.addWidget(self.history_label)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        main_grid_Layout.addWidget(self.history_main_title_widget, 1, 0, 2,2)
        main_2_horizontalLayout.addWidget(main_widget)
        verticalLayout.addLayout(main_2_horizontalLayout)
        self.his_disp_widget.setLayout(self.disp_layout)
        self.disp_layout.addWidget(self.web)
        
        # spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        # main_grid_Layout.addItem(spacerItem4, 1, 0, 1, 1)
#         self.history_label = QtWidgets.QLabel(main_widget)
#         self.history_label.setStyleSheet("color: rgb(255, 255, 255);\n"
# "\n"
# "font: 57 12pt \"Poppins Medium\";\n"
# "\n"
# "")
#         self.history_label.setObjectName("history_label")
#         main_grid_Layout.addWidget(self.history_label, 0, 0, 1, 1)
        main_2_horizontalLayout.addWidget(main_widget)
        verticalLayout.addLayout(main_2_horizontalLayout)
        self.close_btn = QtWidgets.QPushButton(self.web)
        self.close_btn.setStyleSheet("QPushButton{\n"
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
        self.close_btn.setText("")
        self.close_btn.clicked.connect(self.close_web)
        self.close_btn.setIconSize(QtCore.QSize(80, 80))
        self.close_btn.setObjectName("close_btn")
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.icon_model=QtGui.QIcon()
        self.icon_model.addPixmap(QtGui.QPixmap("icon/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(self.icon_model)
        self.close_btn.hide()
        # self.retranslateUi()
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
        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.history_label.setText(_translate("Form", "History"))
    def close_web(self):
        self.his_disp_widget.hide()
        # self.scroll_his_model.show()
        # self.scroll_his_video.show()
        self.history_widget.show()

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
        self.close_btn.setGeometry(QtCore.QRect(1560, 0, 30, 30))
        # self.scroll_his_model.hide()
        # self.scroll_his_video.hide()
        self.history_widget.hide()
        self.his_disp_widget.show()

    def model_render(self,num,id):
        global url
        history_basic.count_history(id,'model')
        # self.scroll_his_model.hide()
        # self.scroll_his_video.hide()
        self.history_widget.hide()
        self.his_disp_widget.show()
        self.url=f"file:///C:/xampp/htdocs/main_data/{num}/index.html"
        self.web.load(QUrl(self.url))
        url=self.url
        self.web.setGeometry(QtCore.QRect(0, 0, 1600, 830))
        # self.web.show()
        self.close_btn.show()
        self.close_btn.raise_()
        self.close_btn.setGeometry(QtCore.QRect(1570, 0, 30, 30))
        self.max_model.raise_()
        self.max_model.show()
        self.icon_model.addPixmap(QtGui.QPixmap("icon/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_model.setIcon(self.icon_model) 
        self.max_model.setGeometry(QtCore.QRect(1570, 760, 30, 30))
        
        # self.history_widget.hide()
    def max_size(self):
            self.form.showFullScreen()
            for i in self.list_widget:
                i.hide()
            self.web1.load(QUrl(url))
            self.big_widget.show()
            self.min_model.show()
            self.min_model.raise_()
            self.min_model.setGeometry(QtCore.QRect(1875, 1030, 40, 40))
            self.min_model.clicked.connect(self.min_size)
            self.main_widget.hide()
            self.icon_model.addPixmap(QtGui.QPixmap("icon/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.min_model.setIcon(self.icon_model)
        
    def min_size(self):
        self.big_widget.hide()
        self.min_model.hide()
        self.form.showMaximized()
        self.his_disp_widget.show()
        self.close_btn.show()
        # self.popular_widget.show()
        self.main_widget.show()
        for i in self.list_widget:
            i.show()
        self.gridLayout_4.addWidget(self.his_disp_widget,0,0,1,1)
        self.max_model.setGeometry(QtCore.QRect(1570, 760, 30, 30))
        self.close_btn.setGeometry(QtCore.QRect(1570, 0, 30, 30))
        self.icon_model.addPixmap(QtGui.QPixmap("icon/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_model.setIcon(self.icon_model)
         
    def fun(self,num,num1,id):
        self.object[num].clicked.connect(lambda:self.video_render(str(num1),id))
   
    def fun1(self,num,num1,id):
        self.object1[num].clicked.connect(lambda:self.model_render(str(num1),id))
    def load_data(self):
        ya=10
        xc=0
        yc=10
        self.history_widget.show()
        self.his_disp_widget.hide()
        sql=f"SELECT * FROM history ORDER BY date_time DESC"
        mycursor.execute(sql)
        myresult2=mycursor.fetchall()
        model=[]
        video=[]
        self.result=[]
        self.result1=[]
        self.object1=[]
        self.object=[]
        myresult=[]
        myresult1=[]
        for i in range(0,len(myresult2)):
            if(myresult2[i][2]=='model'):
                model.append(myresult2[i][1])
            elif(myresult2[i][2]=='video'):
                video.append(myresult2[i][1])
        if(model!=[]):
            for i in model:
                sql=f'SELECT * FROM model_file WHERE id={i}'
                mycursor.execute(sql)
                myresult=mycursor.fetchall()
                self.result.append(myresult[0])
                self.object1.append(QLabel_alterada(self.history_model_widget))
            for j in range(0,len(self.result)):
                for y in range(2):
                    self.object1[j] = QLabel_alterada(self.history_model_widget)
                    self.object1[j].setText(f"{self.result[j][4]}\n{self.result[j][7]}")
                    self.object1[j].setMinimumSize(300,40)
                    self.object1[j].setStyleSheet("color:white;font: 25 9pt \"Poppins Medium\";")
                    self.object1[j].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.object1[j].setScaledContents(True)
                    if(len(self.result)<4):
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
                        if(len(self.result)<4):
                            self.object1[j].setMinimumSize(QtCore.QSize(470, 200)) 
                            self.object1[j].setGeometry(xc,yc,400,200)
                            yc=yc+205  
                        self.object1[j].setPixmap(QtGui.QPixmap(f"C:/xampp/htdocs/main_data/{self.result[j][6]}"))
                        self.object1[j].setMinimumSize(QtCore.QSize(350, 200))
                        self.fun1(j,self.result[j][5],self.result[j][0])
            ya=10
            xc=0
            yc=10
        
        if(video!=[]):
            for k in video:
                sql1=f'SELECT * FROM video WHERE id={k}'
                mycursor.execute(sql1)
                myresult1=mycursor.fetchall()
                self.result1.append(myresult1[0])
                self.object.append(QLabel_alterada(self.history_video_widget))
            for j in range(0,len(self.result1)):
                for y in range(2):
                    self.object[j] = QLabel_alterada(self.history_video_widget)
                    self.object[j].setText(f"{self.result1[j][4]}\n{self.result1[j][7]}")
                    self.object[j].setMinimumSize(300,40)
                    self.object[j].setStyleSheet("color:white;font: 25 9pt \"Poppins Medium\";")
                    self.object[j].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.object[j].setScaledContents(True)
                    if(len(self.result1)<4):
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
                        if(len(self.result1)<4):
                            self.object[j].setMinimumSize(QtCore.QSize(470, 200)) 
                            self.object[j].setGeometry(xc,yc,400,200)
                            yc=yc+205
                        self.object[j].setPixmap(QtGui.QPixmap(f"C:/xampp/htdocs/main_data/{self.result1[j][6]}"))
                        self.object[j].setMinimumSize(QtCore.QSize(350, 200))
                        self.fun(j,self.result1[j][5],self.result1[j][0])
            ya=10
            xc=0
            yc=10