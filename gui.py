from tkinter import *
from PIL import Image, ImageTk
from click import command
from matplotlib.pyplot import fill
from regex import L
import gltf_file
############################################ all functions ########################################################
def menu():
    global status
    if (status==1):
        top1frame.pack(side=TOP, fill="x")
        st12.pack(side=LEFT,padx=10)
        st11.pack(side=LEFT,padx=10)
        st9.pack(side=LEFT,padx=10)
        st8.pack(side=LEFT,padx=10)
        st7.pack(side=LEFT,padx=10)
        st6.pack(side=LEFT,padx=10)
        st5.pack(side=LEFT,padx=10)
        st4.pack(side=LEFT,padx=10)
        st3.pack(side=LEFT,padx=10)
        st2.pack(side=LEFT,padx=10)
        st1.pack(side=LEFT,padx=10)
        status=0
    elif(status==0):
        top1frame.pack_forget()
        st12.pack_forget()
        st11.pack_forget()
        st10.pack_forget()
        st9.pack_forget()
        st8.pack_forget()
        st7.pack_forget()
        st6.pack_forget()
        st5.pack_forget()
        st4.pack_forget()
        st3.pack_forget()
        st2.pack_forget()
        st1.pack_forget()
        status=1

# def gltf():
#     app=gltf_file.Slugrace3D()    
#     app.run()

root = Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" % (width,height))

################################### left and top  side frame #############################################
leftframe = Frame(root, bg="#8080ff", borderwidth=6)  
leftframe.pack(side=LEFT, fill="y")  
topframe=Frame(root, bg="#8080ff", borderwidth=14)
topframe.pack(side=TOP, fill="x")
centerframe=Frame(root, bg="#fff", borderwidth=6) 
centerframe.pack(side=BOTTOM, expand=1, fill=BOTH, pady=10)
# centerframe.grid(column=1,row=2)
status=1
################################## images ################################################################
p = Image.open("icons/add-user.png")
image = p.resize((20,20), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
p = Image.open("search.ico")
image = p.resize((16,16), Image.ANTIALIAS)
photos = ImageTk.PhotoImage(image)
################################## frame button st name ######################################################
top1frame=Frame(root, bg="#b3b3ff", borderwidth=14)
st12=Button(top1frame, text="12TH")
st11=Button(top1frame, text="11TH")
st10=Button(top1frame, text="10TH")
st9=Button(top1frame, text="09TH")
st8=Button(top1frame, text="08TH")
st7=Button(top1frame, text="07TH")
st6=Button(top1frame, text="06TH")
st5=Button(top1frame, text="05TH")
st4=Button(top1frame, text="04TH")
st3=Button(top1frame, text="03TH")
st2=Button(top1frame, text="02TH")
st1=Button(top1frame, text="01TH")
#################################################### left frame button ################################
btn1 = Button(leftframe, text="Submit", fg="skyblue", bg="#8080ff", bd=0, activebackground = "white", image=photo, height="30px",width="30px",relief=RIDGE)  
btn1.pack(side=TOP) 
btn2 = Button(leftframe, text="Submit", fg="skyblue", bg="#8080ff", bd=0, activebackground = "white", image=photo, height="30px",width="30px",relief=RIDGE)  
btn2.pack(side=TOP) 
btn3 = Button(leftframe, text="Submit", fg="skyblue", bg="#8080ff", bd=0, activebackground = "white", image=photo, height="30px",width="30px",relief=RIDGE)  
btn3.pack(side=TOP)  
btn4 = Button(leftframe, text="Submit", fg="skyblue", bg="#8080ff", bd=0, activebackground = "white", image=photo, height="30px",width="30px",relief=RIDGE)  
btn4.pack(side=TOP)
btn4 = Button(leftframe, text="Submit", fg="skyblue", bg="#8080ff", bd=0, activebackground = "white", image=photo, height="30px",width="30px",relief=RIDGE)  
btn4.pack(side=TOP)
btn5 = Button(leftframe, text="Submit", fg="skyblue", bg="#8080ff", bd=0, activebackground = "white", image=photo, height="30px",width="30px",relief=RIDGE)  
btn5.pack(side=BOTTOM)  
###################################################top frame button ###############################
btn4 = Button(topframe, text="Physics", fg="white", bg="#8080ff", bd=0, activebackground = "gray", relief=RIDGE, padx="10px", command=menu)  
btn4.pack(side=LEFT)  
btn5 = Button(topframe, text="Chemistry", fg="white", bg="#8080ff", bd=0, activebackground = "gray", relief=RIDGE, padx="10px", command=menu)  
btn5.pack(side=LEFT)  
btn6 = Button(topframe, text="Biology", fg="white", bg="#8080ff", bd=0, activebackground = "gray", relief=RIDGE, padx="10px", command=menu)  
btn6.pack(side=LEFT)
btn7 = Button(topframe, fg="white", bg="white", bd=1, activebackground = "gray", relief=RIDGE, height="18px", width="22px", image=photos)  
btn7.pack(side=RIGHT)
e1=Entry(topframe, bg="white",font=0)
e1.pack(side=RIGHT)
############################################################################ center images ##############################################################
p1 = Image.open("search.ico")
images = p1.resize((300,150), Image.ANTIALIAS)
img11 = ImageTk.PhotoImage(images)
img1=Button(centerframe, text="caption", image=img11,compound=TOP)
img1.place()
img1=Button(centerframe, text="caption", image=img11,compound=TOP)
img1.grid(row=1,column=0)
img1=Button(centerframe, text="caption", image=img11,compound=TOP)
img1.grid(row=2,column=0)
img1=Button(centerframe, text="caption", image=img11,compound=TOP)
img1.grid(row=3,column=0)
img1=Button(centerframe, text="caption", image=img11,compound=TOP)
img1.grid(row=4,column=0)
img1=Button(centerframe, text="caption", image=img11,compound=TOP)
img1.grid(row=5,column=0)
myscrollbar=Scrollbar(centerframe, orient="vertical")
myscrollbar.pack(side="right",fill="y")
root.mainloop()
