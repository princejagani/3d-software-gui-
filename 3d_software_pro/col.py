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
from tkinter import *
import webview

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create a GUI window to view the HTML content
webview.create_window('tutorialspoint', 'https://www.tutorialspoint.com')
webview.start()

