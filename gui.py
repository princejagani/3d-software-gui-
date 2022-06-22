from codecs import BufferedIncrementalDecoder
from hashlib import new
from tkinter import *
from PIL import Image, ImageTk
from click import command
from matplotlib.pyplot import fill
from regex import L
import simplepbr
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

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

def gltf():
    global state
    img1.pack_forget()
    img2.pack_forget()
    img3.pack_forget()
    img4.pack_forget()
    img5.pack_forget()
    class Tkinter_window(ShowBase):
      def __init__(self):
       ShowBase.__init__(self, windowType='none')
    #    simplepbr.init()
       base.startTk()
    
       frame = base.tkRoot
       frame.update()
    
       props = WindowProperties()
       props.setParentWindow(root.winfo_id())
       props.setOrigin(400, 300)
       props.setSize(500, 500)

       base.makeDefaultPipe()
       base.openDefaultWindow(props=props)

       scene = base.loader.loadModel("environment")
       scene.reparentTo(render)
       
    
    tkinter_window = Tkinter_window()
    tkinter_window.run()
   

    
################################# win starts here #######################################################
root = Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" % (width,height))
################################### left and top  side frame #############################################
leftframe = Frame(root, bg="#8080ff", borderwidth=6)  
leftframe.pack(side=LEFT, fill="y")  
# leftframe.grid(sticky=(S,W,N))
topframe=Frame(root, bg="#8080ff", borderwidth=14)
topframe.pack(side=TOP, fill="x")
# topframe.grid(sticky=(N,W,E))
centerframe=Frame(root, bg="#fff", borderwidth=6) 
centerframe.pack(side=BOTTOM, expand=1, fill=BOTH, pady=10)
# centerframe.grid(sticky=(N,E,S,W))
################################## images ################################################################
p1 = Image.open("icons/MicrosoftTeams-image_1.png")
image1 = p1.resize((20,20), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)
p2 = Image.open("icons/MicrosoftTeams-image_2.png")
image2 = p2.resize((20,20), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
p3 = Image.open("icons/MicrosoftTeams-image_3.png")
image3 = p3.resize((20,20), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)
p4 = Image.open("icons/MicrosoftTeams-image_4.png")
image4 = p4.resize((20,20), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)
p5 = Image.open("icons/MicrosoftTeams-image_5.png")
image5 = p5.resize((20,20), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)
p6 = Image.open("icons/search.png")
image6 = p6.resize((20,20), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(image6)
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
height_icons="30px"
width_icons="30px"
btn1 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo1, height=height_icons,width=width_icons,relief=RIDGE)  
btn1.pack(side=TOP) 
btn2 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo2, height=height_icons,width=width_icons,relief=RIDGE)  
btn2.pack(side=TOP) 
btn3 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo3, height=height_icons,width=width_icons,relief=RIDGE)  
btn3.pack(side=TOP)  
btn4 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo4
, height=height_icons,width=width_icons,relief=RIDGE)  
btn4.pack(side=TOP)
btn4 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo5 , height=height_icons,width=width_icons,relief=RIDGE)  
btn4.pack(side=TOP)
btn5 = Button(leftframe, fg=fg_icons, bg=bg_icons, bd=0, activebackground = abg_icons, image=photo1, height=height_icons,width=width_icons,relief=RIDGE)  
btn5.pack(side=BOTTOM)  
###################################################top frame button #####################################################################################################
bg_c_p_b="#8080ff"
abg_cpb="gray"
fg_cpb=abg_icons
btn4 = Button(topframe, text="Physics", fg=fg_cpb, bg=bg_c_p_b, bd=0, activebackground = abg_cpb, relief=RIDGE, padx="10px", command=lambda:menu(1)) 
btn4.pack(side=LEFT)  
btn5 = Button(topframe, text="Chemistry", fg=fg_cpb, bg=bg_c_p_b, bd=0, activebackground = abg_cpb, relief=RIDGE, padx="10px", command=lambda:menu(2))  
btn5.pack(side=LEFT)  
btn6 = Button(topframe, text="Biology", fg=fg_cpb, bg=bg_c_p_b, bd=0, activebackground = abg_cpb, relief=RIDGE, padx="10px", command=lambda:menu(3))
btn6.pack(side=LEFT)
btn7 = Button(topframe, fg=abg_icons, bg=fg_cpb, bd=1, activebackground =abg_cpb, relief=RIDGE, height="18px", width="22px", image=photo6)  
btn7.pack(side=RIGHT)
e1=Entry(topframe, bg=abg_icons,font=0)
e1.pack(side=RIGHT)
############################################################################ center images ###############################################################################
p1 = Image.open("icons/search.png")
images = p1.resize((300,150), Image.ANTIALIAS)
img11 = ImageTk.PhotoImage(images)
img1=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img1.pack(side=LEFT,padx=8)
img2=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img2.pack(side=LEFT,padx=8)
img3=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img3.pack(side=LEFT,padx=8)
img4=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img4.pack(side=LEFT,padx=8)
img5=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img5.pack(side=LEFT,padx=8)
img5=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img5.pack(side=LEFT,padx=8)
img5=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img5.pack(side=TOP,padx=8)
img5=Button(centerframe, text="caption", image=img11,compound=TOP, command=gltf)
img5.pack(side=TOP,padx=8)
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
root.mainloop()
