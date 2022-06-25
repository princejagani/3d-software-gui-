from hashlib import new
from tkinter import *
from PIL import Image, ImageTk
from click import command
from matplotlib.pyplot import fill
from numpy import size
import simplepbr
from direct.showbase.ShowBase import ShowBase
from tkVideoPlayer import TkinterVideo
from panda3d.core import WindowProperties
import tkinter.font as font

############################################### demo #####################################################


# class Tkinter_window(ShowBase):
#   def __init__(self):
#     ShowBase.__init__(self, windowType='none')
#     base.startTk()
    
#     frame = base.tkRoot
#     frame.update()
    
#     props = WindowProperties()
#     props.setParentWindow(frame.winfo_id())
#     props.setOrigin(0, 0)
#     props.setSize(500, 500)

#     base.makeDefaultPipe()
#     base.openDefaultWindow(props=props)

#     scene = base.loader.loadModel("environment")
#     scene.reparentTo(render)
    
# tkinter_window = Tkinter_window()
# tkinter_window.run()

############################################ all functions ########################################################


status1=1
status2=1
status3=1
def menu(val):
    global status1
    global status2
    global status3
    global st
    if(val==1):
        if (status1==1):
            top1frame.pack(side=TOP, fill="x")
            for i in range(0,len(st)-1):
                st[i].pack(side=LEFT,padx=10)
            status1=0
        elif(status1==0):
            top1frame.pack_forget()     
            for i in range(0,len(st)-1):
                st[i].pack_forget()    
            status1=1 
    elif(val==2):
        if (status2==1):
            top1frame.pack(side=TOP, fill="x")
            for i in range(0,len(st)-1):
                st[i].pack(side=LEFT,padx=10)
            status2=0
        elif(status2==0):
            top1frame.pack_forget()     
            for i in range(0,len(st)-1):
                st[i].pack_forget()    
            status2=1 
    elif(val==3):
        if (status3==1):
            top1frame.pack(side=TOP, fill="x")
            for i in range(0,len(st)-1):
                st[i].pack(side=LEFT,padx=10)
            status3=0
        elif(status3==0):
            top1frame.pack_forget()     
            for i in range(0,len(st)-1):
                st[i].pack_forget()    
            status3=1 

state=1
t1=''
# tkinter_window=""
def gltf(num=0):
    global state
    global tkinter_window
    global t1
    if(num==0):
        # global tkinter_window
        img1.pack_forget()
        img2.pack_forget()
        img3.pack_forget()
        img4.pack_forget()
        img5.pack_forget()
        img6.pack_forget()
        img7.pack_forget()
        img8.pack_forget()
        img9.pack_forget()
        centerframe1.pack_forget()
        centerframe2.pack_forget()
        centerframe3.pack_forget()
        t1.destroy()
        tkinter_window = Tkinter_window()
        tkinter_window.run()
       
    else:
        tkinter_window.destroy()

def home():
    vi1.pack_forget()
    b1.pack_forget()
    videoframe.pack_forget()
    centerframe1.pack(side=BOTTOM, expand=0, fill=X, pady=20)
    centerframe2.pack(side=BOTTOM, expand=0, fill=X, pady=20)
    centerframe3.pack(side=BOTTOM, expand=0, fill=X, pady=20)
    img1.pack(side=LEFT,padx=30)
    img2.pack(side=LEFT,padx=30)
    img3.pack(side=LEFT,padx=30)
    img4.pack(side=LEFT,padx=30)
    img5.pack(side=LEFT,padx=30)
    img6.pack(side=LEFT,padx=30)
    img7.pack(side=LEFT,padx=30)
    img8.pack(side=LEFT,padx=30)
    img9.pack(side=LEFT,padx=30)
    gltf(1)
 
def video():
     
     vi1.pack_forget()
     b1.pack_forget()
     img1.pack_forget()
     img2.pack_forget()
     img3.pack_forget()
     img4.pack_forget()
     img5.pack_forget()
     img6.pack_forget()
     img7.pack_forget()
     img8.pack_forget()
     img9.pack_forget()
     centerframe1.pack_forget()
     centerframe2.pack_forget()
     centerframe3.pack_forget()
     videoframe.pack(side=BOTTOM, expand=True, fill=BOTH)
     v1.grid(row=0,column=0,padx=30,pady=30)
     v2.grid(row=0,column=1,padx=30,pady=30)
     v3.grid(row=0,column=2,padx=30,pady=30)
     v4.grid(row=0,column=3,padx=30,pady=30)
     v5.grid(row=1,column=0,padx=30,pady=30)
     v6.grid(row=1,column=1,padx=30,pady=30)
     v7.grid(row=1,column=2,padx=30,pady=30)
     v8.grid(row=1,column=3,padx=30,pady=30)
     v9.grid(row=2,column=0,padx=30,pady=30)
     gltf(1)
v=0
def play():
    global v
    if(v==0):
        vi1.pause()
        v=1
        b1['text'] = 'resume'
        
    elif(v==1):
        vi1.play()
        v=0
        b1['text'] = 'pause'

def dis_video():
     videoframe.pack_forget()
     img1.pack_forget()
     img2.pack_forget()
     img3.pack_forget()
     img4.pack_forget()
     img5.pack_forget()
     img6.pack_forget()
     img7.pack_forget()
     img8.pack_forget()
     img9.pack_forget()
     centerframe1.pack_forget()
     centerframe2.pack_forget()
     centerframe3.pack_forget()
     vi1.load(r"video/video2.avi")
     b1.pack(side=BOTTOM, fill=X)
     vi1.pack(side=BOTTOM,expand=True, fill=BOTH)
     vi1.play()
     
################################# win starts here #######################################################
root = Tk()
class Tkinter_window(ShowBase):
      def __init__(self):
       ShowBase.__init__(self, windowType='none')
    #    simplepbr.init()
       base.startTk()    
    #    frame = base.tkRoot
    #    frame.update()
    #    frame.geometry("%dx%d"%(width, height))
       
    
       props = WindowProperties()
       props.setParentWindow(root.winfo_id())
       props.setOrigin(60, 120)
       props.setSize(1850, 1000)

       base.makeDefaultPipe()
       base.openDefaultWindow(props=props)

       scene = base.loader.loadModel("environment")
       scene.reparentTo(render)

############################################################################################################
class Tkinter_window1(ShowBase):
      def __init__(self):
       ShowBase.__init__(self, windowType='none')
    #    simplepbr.init()
       base.startTk()    
    #    frame = base.tkRoot
    #    frame.update()
    #    frame.geometry("%dx%d"%(width, height))
       
    
       props = WindowProperties()
       props.setParentWindow(root.winfo_id())
       props.setOrigin(1,1)
       props.setSize(1,1)

       base.makeDefaultPipe()
       base.openDefaultWindow(props=props)

       scene = base.loader.loadModel("environment")
       scene.reparentTo(render)

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d"%(width, height))
################################### left and top  side frame #############################################
leftframe = Frame(root, bg="#8080ff", borderwidth=10)  
leftframe.pack(side=LEFT, fill="y")  
# leftframe.grid(sticky=(S,W,N))
topframe=Frame(root, bg="#8080ff", borderwidth=18)
topframe.pack(side=TOP, fill="x")
# topframe.grid(sticky=(N,W,E))
centerframe1=Frame(root, bg="white", borderwidth=6) 
centerframe1.pack(side=BOTTOM, expand=0, fill=X, pady=20)
centerframe2=Frame(root, bg="white", borderwidth=6) 
centerframe2.pack(side=BOTTOM, expand=0, fill=X, pady=20)
centerframe3=Frame(root, bg="white", borderwidth=6) 
centerframe3.pack(side=BOTTOM, expand=0, fill=X, pady=20)
# centerframe.grid(sticky=(N,E,S,W))
videoframe=Frame(root,bg="white", borderwidth=6)
b1=Button(root,text="Pause", command=play, height=2,font=2)
vi1=TkinterVideo(master=root,scaled=True)
################################## images ################################################################
p1 = Image.open("icons/MicrosoftTeams-image_1.png")
image1 = p1.resize((30,30), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
p2 = Image.open("icons/MicrosoftTeams-image_2.png")
image2 = p2.resize((30,30), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
p3 = Image.open("icons/MicrosoftTeams-image_3.png")
image3 = p3.resize((30,30), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
p4 = Image.open("icons/MicrosoftTeams-image_4.png")
image4 = p4.resize((30,30), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)
p5 = Image.open("icons/MicrosoftTeams-image_5.png")
image5 = p5.resize((30,30), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)
p6 = Image.open("icons/search.png")
image6 = p6.resize((20,20), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(image6)
p7 = Image.open("icons/user.png")
image7 = p7.resize((30,30), Image.ANTIALIAS)
photo7 = ImageTk.PhotoImage(image7)
################################## frame button st name ######################################################
top1frame=Frame(root, bg="#b3b3ff", borderwidth=14)
st=[]
s=12
for i in range(0,13):
    st.append(Button(top1frame, text=str(s)+"TH"))
    s=s-1
#################################################### left frame button ################################
fg_icons="skyblue"
bg_icons="#8080ff"
abg_icons="white"
height_icons="40px"
width_icons="30px"
pad_icons="10px"
btn1 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo1, height=height_icons,width=width_icons,relief=RIDGE,pady=pad_icons)  
btn1.pack(side=TOP) 
btn2 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo2, height=height_icons,width=width_icons,relief=RIDGE,command=home,pady=pad_icons)  
btn2.pack(side=TOP) 
btn3 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo3, height=height_icons,width=width_icons,relief=RIDGE,pady=pad_icons)  
btn3.pack(side=TOP)  
btn4 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo4
, height=height_icons,width=width_icons,relief=RIDGE, pady=pad_icons ,command=video)  
btn4.pack(side=TOP)
btn4 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo5 , height=height_icons,width=width_icons,relief=RIDGE,pady=pad_icons)  
btn4.pack(side=TOP)
btn5 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo7, height=height_icons,width=width_icons,relief=RIDGE,pady=pad_icons)  
btn5.pack(side=BOTTOM)  
###################################################top frame button #####################################################################################################
bg_c_p_b="#8080ff"
abg_cpb="gray"
fg_cpb=abg_icons
myFont = font.Font(size=12)
btn4 = Button(topframe, text="Physics", fg=fg_cpb, bg=bg_c_p_b, bd=0, activebackground = abg_cpb, relief=RIDGE, font=myFont, padx="10px", command=lambda:menu(1)) 
btn4.pack(side=LEFT)  
btn5 = Button(topframe, text="Chemistry", fg=fg_cpb, bg=bg_c_p_b, bd=0, activebackground = abg_cpb, relief=RIDGE, font=myFont, padx="10px", command=lambda:menu(2))  
btn5.pack(side=LEFT)  
btn6 = Button(topframe, text="Biology", fg=fg_cpb, bg=bg_c_p_b, bd=0, activebackground = abg_cpb, relief=RIDGE, font=myFont, padx="10px", command=lambda:menu(3))
btn6.pack(side=LEFT)
btn7 = Button(topframe, fg=abg_icons, bg=fg_cpb, bd=1, activebackground =abg_cpb, relief=RIDGE, height="18px", width="22px", image=photo6)  
btn7.pack(side=RIGHT)
e1=Entry(topframe, bg=abg_icons,font=0)
e1.pack(side=RIGHT)
############################################################################ center images ###############################################################################
p1 = Image.open("icons/download1.jpg")
images = p1.resize((300,150), Image.ANTIALIAS)
img11 = ImageTk.PhotoImage(images)
p2 = Image.open("icons/download2.jpg")
images1 = p2.resize((300,150), Image.ANTIALIAS)
img12 = ImageTk.PhotoImage(images1)
p3 = Image.open("icons/download3.jpg")
images2 = p3.resize((300,150), Image.ANTIALIAS)
img13 = ImageTk.PhotoImage(images2)
img1=Button(centerframe3, text="caption", image=img11,compound=TOP, command=gltf)
img1.pack(side=LEFT,padx=30)
img2=Button(centerframe3, text="caption", image=img11,compound=TOP, command=gltf)
img2.pack(side=LEFT,padx=30)
img3=Button(centerframe3, text="caption", image=img11,compound=TOP, command=gltf)
img3.pack(side=LEFT,padx=30)
img4=Button(centerframe3, text="caption", image=img11,compound=TOP, command=gltf)
img4.pack(side=LEFT,padx=30)
img5=Button(centerframe2, text="caption", image=img12,compound=TOP, command=gltf)
img5.pack(side=LEFT,padx=30)
img6=Button(centerframe2, text="caption", image=img12,compound=TOP, command=gltf)
img6.pack(side=LEFT,padx=30)
img7=Button(centerframe2, text="caption", image=img12,compound=TOP, command=gltf)
img7.pack(side=LEFT,padx=30)
img8=Button(centerframe2, text="caption", image=img12,compound=TOP, command=gltf)
img8.pack(side=LEFT,padx=30)
img9=Button(centerframe1, text="caption", image=img13,compound=TOP, command=gltf)
img9.pack(side=LEFT,padx=30)
img10=Button(centerframe1, text="caption", image=img13,compound=TOP, command=gltf)
img10.pack(side=LEFT,padx=30)
# img11=Button(centerframe1, text="caption", image=img13,compound=TOP, command=gltf)
# img11.pack(side=LEFT,padx=30)
# img12=Button(centerframe1, text="caption", image=img13,compound=TOP, command=gltf)
# img12.pack(side=LEFT,padx=30)

# img1.place(relx = 0.2, rely = 0.0, anchor ="ne")
# img1=Button(centerframe, text="caption", image=img11,compound=TOP)
# img1.grid(row=1,column=0)
# img1=Button(centerframe, text="caption", image=img11,compound=TOP)
# img1.grid(row=2,column=0)
# img1=Button(centerframe, text="caption", image=img11,compound=TOP)
# img1.grid(row=3,column=0)
# img1=Button(centerframe, text="caption", image=img11,compound=TOP)
# img1.grid(row=4,column=0)
# img1=Button(centerframe, text="caption", image=img11,compound=TOP)
# img1.grid(row=5,column=0)
# myscrollbar=Scrollbar(centerframe, orient="vertical")
# myscrollbar.pack(side="right",fill="y")

################################################## video ####################################################
v1=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video,bg="#4dd2ff",foreground="white")
v2=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video,bg="#4dd2ff", foreground="white")
v3=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video,bg="#4dd2ff", foreground="white")
v4=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video,bg="#4dd2ff", foreground="white")
v5=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video,bg="#4dd2ff",foreground="white")
v6=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video,bg="#4dd2ff", foreground="white")
v7=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video, bg="#4dd2ff", foreground="white")
v8=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video, bg="#4dd2ff", foreground="white")
v9=Button(videoframe, text="play", image=img11,compound=TOP, command=dis_video, bg="#4dd2ff", foreground="white")
t1=Tkinter_window1()
t1.run()



root.mainloop()
