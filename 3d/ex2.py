# # importing libraries
# from PyQt5.QtWidgets import * 
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import * 
# from PyQt5.QtCore import * 
# import sys
  
  
# class Window(QMainWindow):
  
#     def __init__(self):
#         super().__init__()
  
#         # setting title
#         self.setWindowTitle("Python ")
  
#         # setting geometry
#         self.setGeometry(100, 100, 500, 400)
  
#         # calling method
#         self.UiComponents()
  
#         # showing all the widgets
#         self.show()
  
  
  
#     # method for components
#     def UiComponents(self):
  
#         # creating a QListWidget
#         list_widget = QListWidget(self)
  
#         # setting geometry to it
#         list_widget.setGeometry(50, 70, 150, 80)
#         label_4 = QLabel()
#         label_4.setGeometry(QtCore.QRect(30, 20, 441, 251))
#         label_4.setStyleSheet("background-image: url(icon/IMG_3928-1.jpg); background-position: center; ")
#         label_4.setText("")
#         label_4.setPixmap(QtGui.QPixmap("icon/download1.jpg"))
#         label_4.setScaledContents(True)
#         label_4.setObjectName("label_4")
  
#         # list widget items
#         item1 = QListWidgetItem(label_4)
#         item2 = QListWidgetItem("B")
#         item3 = QListWidgetItem("C")
#         item4 = QListWidgetItem("D")
#         item4 = QListWidgetItem("D")
#         item5 = QListWidgetItem("D")
#         item6 = QListWidgetItem("D")
#         item7 = QListWidgetItem("D")
#         item8 = QListWidgetItem("D")
  
#         # adding items to the list widget
#         list_widget.addItem(item1)
#         list_widget.addItem(item2)
#         list_widget.addItem(item3)
#         list_widget.addItem(item4)
#         list_widget.addItem(item5)
#         list_widget.addItem(item6)
#         list_widget.addItem(item7)
#         list_widget.addItem(item8)
  
#         # scroll bar
#         scroll_bar = QScrollBar(self)
  
#         # setting style sheet to the scroll bar
#         scroll_bar.setStyleSheet("background : lightgreen;")
  
#         # adding extra scroll bar to it
#         list_widget.addScrollBarWidget(scroll_bar, Qt.AlignLeft)
  
#         # creating a label
#         label = QLabel("GeesforGeeks", self)
  
#         # setting geometry to the label
#         label.setGeometry(230, 80, 280, 80)
  
#         # making label multi line
#         label.setWordWrap(True)
  
  
  
  
# # create pyqt5 app
# App = QApplication(sys.argv)
  
# # create the instance of our Window
# window = Window()
  
# # start the app
# sys.exit(App.exec())


# from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
#                              QHBoxLayout, QVBoxLayout, QMainWindow)
# from PyQt5.QtCore import Qt, QSize
# from PyQt5 import QtWidgets, uic
# import sys


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
#         self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
#         self.vbox = QHBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

#         for i in range(1,1000):
#             object = QLabel("TextLabel")
#             self.vbox.addWidget(object)

#         self.widget.setLayout(self.vbox)

#         #Scroll Area Properties
#         self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.scroll.setWidgetResizable(True)
#         self.scroll.setWidget(self.widget)

#         self.setCentralWidget(self.scroll)

#         self.setGeometry(600, 100, 1000, 900)
#         self.setWindowTitle('Scroll Area Demonstration')
#         self.show()

#         return

# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


# from PyQt5.QtCore import QDir, Qt, QUrl
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
#         QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
# from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
# from PyQt5.QtGui import QIcon
# import sys

# class VideoWindow(QMainWindow):

#     def __init__(self, parent=None):
#         super(VideoWindow, self).__init__(parent)
#         self.setWindowTitle("PyQt Video Player Widget Example - pythonprogramminglanguage.com") 

#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

#         videoWidget = QVideoWidget()

#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)

#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)

#         self.errorLabel = QLabel()
#         self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
#                 QSizePolicy.Maximum)

#         # Create new action
#         openAction = QAction(QIcon('open.png'), '&Open', self)        
#         openAction.setShortcut('Ctrl+O')
#         openAction.setStatusTip('Open movie')
#         openAction.triggered.connect(self.openFile)

#         # Create exit action
#         exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(self.exitCall)

#         # Create menu bar and add action
#         menuBar = self.menuBar()
#         fileMenu = menuBar.addMenu('&File')
#         #fileMenu.addAction(newAction)
#         fileMenu.addAction(openAction)
#         fileMenu.addAction(exitAction)

#         # Create a widget for window contents
#         wid = QWidget(self)
#         self.setCentralWidget(wid)

#         # Create layouts to place inside widget
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)

#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.errorLabel)

#         # Set widget to contain window contents
#         wid.setLayout(layout)

#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)

#     def openFile(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
#                 QDir.homePath())

#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                     QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)

#     def exitCall(self):
#         sys.exit(app.exec_())

#     def play(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#         else:
#             self.mediaPlayer.play()

#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPlay))

#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)

#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)

#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)

#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     player = VideoWindow()
#     player.resize(640, 480)
#     player.show()
#     sys.exit(app.exec_())
# app.py

from pyexpat import model
from turtle import mode
from zipfile import ZipFile
import json
from db_module import *
import os
import shutil
# filename='D:\\python infinite\\gltf\\3d\\api_data\\demo.zip'
# with ZipFile(filename, 'r') as zipObj:
#    zipObj.extractall()
#    os.remove(filename)

filename='api_data/demo.zip'
shutil.unpack_archive(filename,extract_dir="api_data/")
os.remove(filename)
with open("api_data/demo/readme.json") as jsonFile:
        data = json.load(jsonFile)
        std=data['standard']
        sub=data['subject']
        ch=data['chapter']
        to=data['topic']
        v_folder=data['video_f_name']
        m_folder=data['model_f_name']
        m_th=data['m_thumbnail']
        v_th=data['v_thumbnail']

############################################### variable decleration #################################################################
sql1=''
sql2=''
sql3=''
myresult1=None
myresult2=None
myresult3=None
fav=False
################################################ sql query ###################################################################
sql1=f"SELECT id FROM std WHERE std_name='{std}'"
sql2=f"SELECT id FROM sub WHERE sub_name='{sub}'"
sql3=f"SELECT id FROM chapter WHERE ch_name='{ch}'"
mycursor.execute(sql1)
myresult1 = mycursor.fetchone()
print(myresult1)
mycursor.execute(sql2)  
myresult2 = mycursor.fetchone()
print(myresult2)
mycursor.execute(sql3)
myresult3 = mycursor.fetchone()
print(myresult3)
result=0
result1=0
model_name=[]
model_thumbnail=[]
video_name=[]
video_thumbnail=[]
file_list=''
dest=''
if(myresult1!=None and myresult2!=None and myresult3!=None):
        file_list=os.listdir(f"api_data/demo/{m_folder}")
        for i in range(0,len(file_list)):
                model_name.append(file_list[i])
        file_list=os.listdir(f"api_data/demo/{m_th}")
        for i in range(0,len(file_list)):
                model_thumbnail.append(file_list[i])

        for  i in range(0,len(model_name)):
                if(f"{model_name[i]}"+'.jpg'or'.jpeg'or'.png' in model_thumbnail):
                        
                        f=model_thumbnail.index(f"{model_name[i]}"+'.jpg'or'.jpeg'or'.png')
                        sql_model=f"INSERT INTO `model_file` (std_id,sub_id,ch_id,topic_name,filename,thumbnail_name,model_desc,favorite) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{m_folder}/{model_name[i]}','demo/{m_th}/{model_thumbnail[f]}','{sub}|ch {ch}|std {std}',{fav})"
                        print(sql_model)
                        # sql_video=f"INSERT INTO `video` (std_id,sub_id,ch_id,topic_name,v_name,thumbnail_name,v_desc) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{v_folder}','demo/{v_th}','video')"
                        try:

                                mycursor.execute(sql_model)
                                # mycursor.execute(sql_video)
                                mydb.commit()
                                print("files added")
                                result=True
                        except:
                                result=False
                                print("eorr1")

        file_list=os.listdir(f"api_data/demo/{v_folder}")
        for i in range(0,len(file_list)):
                video_name.append(file_list[i])
        file_list=os.listdir(f"api_data/demo/{v_th}")
        for i in range(0,len(file_list)):
                video_thumbnail.append(file_list[i])
        for  i in range(0,len(video_name)):
                nm,ex=video_name[i].split('.')
                if(f"{nm}"+'.jpg'or'.jpeg'or'.png' in video_thumbnail):
                        f=video_thumbnail.index(f"{nm}"+'.jpg'or'.jpeg'or'.png')
                        # sql_model=f"INSERT INTO `model_file` (std_id,sub_id,ch_id,topic_name,filename,thumbnail_name,model_desc) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{m_folder}/{model_name[i]}','demo/{m_th}/{model_thumbnail[f]}','model')"
                        sql_video=f"INSERT INTO `video` (std_id,sub_id,ch_id,topic_name,v_name,thumbnail_name,v_desc,favorite) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{v_folder}/{video_name[i]}','demo/{v_th}/{video_thumbnail[f]}','{sub}|ch {ch}|std {std}',{fav})"
                        try:

                                # mycursor.execute(sql_model)
                                mycursor.execute(sql_video)
                                mydb.commit()
                                print("files added")
                                result1=True
                        except:
                                result1=False
                                print("eorr1")
        if(result==True and result1==True):
                import shutil
                source = "api_data/demo"
                destination = "C:/xampp/htdocs/main_data/demo"
                dest = shutil.move(source, destination)
                print("folder moved")



 

else:
        if(myresult1==None):
                sql4=f"INSERT INTO `std`(std_name) VALUES('{std}')"
                try:
                        mycursor.execute(sql4)
                        mydb.commit()
                        print('done')
                except:
                        print("error")
        if(myresult2==None):
                sql5=f"INSERT INTO `sub`(sub_name) VALUES('{sub}')"
                try:
                        mycursor.execute(sql5)
                        mydb.commit()
                        print('done')
                except:
                        print("error")
        if(myresult3==None):
                sql6=f"INSERT INTO `chapter`(ch_name) VALUES('{ch}')"
                try:
                        mycursor.execute(sql6)
                        mydb.commit()
                        print('done')
                except:
                        print("error")
        sql1=f"SELECT id FROM std WHERE std_name='{std}'"
        sql2=f"SELECT id FROM sub WHERE sub_name='{sub}'"
        sql3=f"SELECT id FROM chapter WHERE ch_name='{ch}'"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchone()
        print(myresult1)
        mycursor.execute(sql2)  
        myresult2 = mycursor.fetchone()
        print(myresult2)
        mycursor.execute(sql3)
        myresult3 = mycursor.fetchone()
        print(myresult3)
        if(myresult1!=None and myresult2!=None and myresult3!=None):
                file_list=os.listdir(f"api_data/demo/{m_folder}")
                for i in range(0,len(file_list)):
                        model_name.append(file_list[i])
                file_list=os.listdir(f"api_data/demo/{m_th}")
                for i in range(0,len(file_list)):
                        model_thumbnail.append(file_list[i])

                for  i in range(0,len(model_name)):
                        if(f"{model_name[i]}"+'.jpg'or'.jpeg'or'.png' in model_thumbnail):
                                
                                f=model_thumbnail.index(f"{model_name[i]}"+'.jpg' or '.jpeg' or '.png')
                                sql_model=f"INSERT INTO `model_file` (std_id,sub_id,ch_id,topic_name,filename,thumbnail_name,model_desc,favorite) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{m_folder}/{model_name[i]}','demo/{m_th}/{model_thumbnail[f]}','{sub}|ch {ch}|std {std}',{fav})"
                                # sql_video=f"INSERT INTO `video` (std_id,sub_id,ch_id,topic_name,v_name,thumbnail_name,v_desc) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{v_folder}','demo/{v_th}','video')"
                                try:

                                        mycursor.execute(sql_model)
                                        # mycursor.execute(sql_video)
                                        mydb.commit()
                                        print("files added")
                                        result=True
                                except:
                                        result=False
                                        print("eorr1")

                file_list=os.listdir(f"api_data/demo/{v_folder}")
                for i in range(0,len(file_list)):
                        video_name.append(file_list[i])
                file_list=os.listdir(f"api_data/demo/{v_th}")
                for i in range(0,len(file_list)):
                        video_thumbnail.append(file_list[i])
                for  i in range(0,len(video_name)):
                        nm,ex=video_name[i].split('.')
                        if(f"{nm}"+'.jpg'or'.jpeg'or'.png' in video_thumbnail):
                                f=video_thumbnail.index(f"{nm}"+'.jpg'or'.jpeg'or'.png')
                                # sql_model=f"INSERT INTO `model_file` (std_id,sub_id,ch_id,topic_name,filename,thumbnail_name,model_desc) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{m_folder}/{model_name[i]}','demo/{m_th}/{model_thumbnail[f]}','model')"
                                sql_video=f"INSERT INTO `video` (std_id,sub_id,ch_id,topic_name,v_name,thumbnail_name,v_desc,favorite) VALUES('{myresult1[0]}','{myresult2[0]}','{myresult3[0]}','{to}','demo/{v_folder}/{video_name[i]}','demo/{v_th}/{video_thumbnail[f]}','{sub}|ch {ch}|std {std}',{fav})"
                                try:

                                        # mycursor.execute(sql_model)
                                        mycursor.execute(sql_video)
                                        mydb.commit()
                                        print("files added")
                                        result1=True
                                except:
                                        result1=False
                                        print("eorr1")
                if(result==True and result1==True):
                        import shutil
                        source = "api_data/demo"
                        destination = "C:/xampp/htdocs/main_data/demo"
                        dest = shutil.move(source, destination)
                        print("folder moved")
                        


