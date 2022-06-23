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
# player = tkvideo("video/video1.mp4", video_label,
#                  loop = 1, size = (700, 500))

# player.play()
# root.mainloop()
val=0
def play():
    global val
    if(val==0):
        v1.play()
        val=1
        b1['text'] = 'pause'
        
    elif(val==1):
        v1.pause()
        val=0
        b1['text'] = 'resume'

from tkinter import *
from marshmallow import pre_load
from pygame import SCALED
from tkVideoPlayer import TkinterVideo
root = Tk()
v1=TkinterVideo(master=root,scaled=True)
v1.load(r"video/video1.mp4")
v1.pack(side=LEFT)
b1=Button(root,text="play", command=play)
b1.pack(side=LEFT)

root.mainloop()


# from tkinter import *
# from tkvideo import tkvideo


# from tkinter import *
# from PIL import Image, ImageTk
# import threading
# import imageio
# # create instance for window
# root = Tk()
# # set window title
# root.title('Video Player')
# # read video
# video = imageio.get_reader('video/video1.mp4')
# def display_video(label):
#    # iterate through video data
#    for image in video.iter_data():
#       # convert array into image
#       img = Image.fromarray(image)
#       # Convert image to PhotoImage
#       image_frame = ImageTk.PhotoImage(image = img)
#       # configure video to the lable
#       label.config(image=image_frame)
#       label.image = image_frame
# # create label for video
# video_label = Label(root)
# video_label.pack()
# # create and start thread
# thread = threading.Thread(target=display_video, args=(video_label,))
# thread.start()
# root.mainloop()