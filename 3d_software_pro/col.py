# from click import command
# from direct.showbase.ShowBase import ShowBase
# from panda3d.core import WindowProperties
# from tkinter import *
# root=Tk()
# def demo():
#    tkinter_window = Tkinter_window()
#    tkinter_window.run()
# class Tkinter_window(ShowBase):
#   def __init__(self):
#     ShowBase.__init__(self, windowType='none')
#     base.startTk()
#     # frame = base.tkRoot
#     # frame.update()
    
#     props = WindowProperties()
#     props.setParentWindow(root.winfo_id())
#     props.setOrigin(300, 300)
#     props.setSize(500, 500)

#     base.makeDefaultPipe()
#     base.openDefaultWindow(props=props)

#     scene = base.loader.loadModel("environment")
#     scene.reparentTo(render)

# leftframe = Frame(root, bg="#8080ff", borderwidth=6)  
# leftframe.pack(side=LEFT, fill="y")  
# # leftframe.grid(sticky=(S,W,N))
# topframe=Frame(root, bg="#8080ff", borderwidth=14)
# topframe.pack(side=TOP, fill="x")
# b1=Button(leftframe,text="hello", command=demo)
# b1.pack(side=TOP)
# # topframe.grid(sticky=(N,W,E))

# # tkinter_window = Tkinter_window()
# # tkinter_window.run()

# root.mainloop()
# from tkinter import *
# from tkvideo import tkvideo
# # create instance fo window
# root = Tk()
# # set window title
# root.title('Video Player')
# # create label
# video_label = Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("video/video3.mp4", video_label,
#                  loop = 1, size = (700, 500))
# player.play()
# root.mainloop()
# import pygame
# from tkinter import *
# root = Tk()
# pygame.init()
# def play():
#     pygame.mixer.music.load("video/video2.avi") #Loading File Into Mixer
#     pygame.mixer.music.play() #Playing It In The Whole Device
# Button(root,text="Play",command=play).pack()
# root.mainloop()
# import sys
# from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QWidget,QApplication
# from PyQt5.QtWebKitWidgets import *
# from PyQt5.QtCore import QUrl
# app=QApplication(sys.argv)

# mainWindow=QMainWindow()
# widget=QWidget()

# web=QWebView()
# web.load(QUrl("http://supercoders.in"))

# verticalLayout=QVBoxLayout()
# verticalLayout.addWidget(web)

# widget.setLayout(verticalLayout)
# mainWindow.setCentralWidget(widget)
# mainWindow.show()

# sys.exit(app.exec_())




# from tkinter import *
# from click import command
# import webview 
# # Create an instance of tkinter frame or window
# win = Tk()
# def demo():
#    web=webview
#    web.create_window('3d education', 'http://localhost:8668/player/player.html?load=../applications/app/male%20reproduction.gltf',frameless=True,easy_drag=False)
#    web.start()
# # Set the size of the window
# win.geometry("700x350")

# # Create a GUI window to view the HTML content
# # webview.base_uri('http://localhost:8668/applications/demo/demo.html')
# b1=Button(win,text="show",command=demo)
# b1.pack(side=TOP)
# win.mainloop()






# from tkinterweb import HtmlFrame #import the HTML browser
# try:
#   import tkinter as tk #python3
# except ImportError:
#   import Tkinter as tk #python2

# root = tk.Tk() #create the tkinter window
# frame = HtmlFrame(root) #create HTML browser

# frame.load_website("http://localhost:8668/applications/my_awesome_app/my_awesome_app.html") #load a website
# frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
# root.mainloop()





# import PyQt5
# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication, QWidget
# # from PyQt5.QtWebKitWidgets import QWebView , QWebPage
# # from PyQt5.QtWebKit import QWebSettings
# from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
# from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
# from PyQt5.QtNetwork import *
# import sys
# from optparse import OptionParser

# class MyBrowser(QWebPage):
#     ''' Settings for the browser.'''
    
#     def userAgentForUrl(self, url):
#         ''' Returns a User Agent that will be seen by the website. '''
#         return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

# class Browser(QWebView):
#     def __init__(self):
#         # QWebView
#         self.view = QWebView.__init__(self)
#         #self.view.setPage(MyBrowser())
#         self.setWindowTitle('Loading...')
#         self.titleChanged.connect(self.adjustTitle)
#         #super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&amp;)"), self.adjustTitle)

#     def load(self,url):
#         self.setUrl(QUrl(url))
    
#     def adjustTitle(self):
#         self.setWindowTitle(self.title())
    
#     def disableJS(self):
#         settings = QWebSettings.globalSettings()
#         settings.setAttribute(QWebSettings.JavascriptEnabled, False)

# app = QApplication(sys.argv)
# view = Browser()
# view.showMaximized()
# view.load("http://localhost:8668/applications/demo/demo.html")
# app.exec_()



# from tkinter import *
# import sys
# from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QWidget,QApplication
# from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
# from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
# from PyQt5.QtNetwork import *
# from PyQt5.QtCore import QUrl
# app=QApplication(sys.argv)

# mainWindow=QMainWindow()
# widget=QWidget()

# web=QWebView()
# web.load(QUrl("http://localhost/app/"))
# verticalLayout=QVBoxLayout()
# verticalLayout.addWidget(web)
# height=800
# width=800
# widget.setLayout(verticalLayout)
# # widget.setMaximumWidth(width)
# # widget.setMaximumHeight(height)
# mainWindow.setCentralWidget(widget)
# mainWindow.show()
# sys.exit(app.exec_())




from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys

class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("PyQt Video Player Widget Example - pythonprogramminglanguage.com") 

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        # Create new action
        openAction = QAction(QIcon('open.png'), '&Open', self)        
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open movie')
        openAction.triggered.connect(self.openFile)

        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        #fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())