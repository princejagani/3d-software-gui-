from click import command
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from tkinter import *
class Tkinter_window(ShowBase):
  def __init__(self):
    ShowBase.__init__(self, windowType='none')
    base.startTk()
    base.geometry("1000x800")
    frame = base.tkRoot
    frame.update()
    
    props = WindowProperties()
    props.setParentWindow(frame.winfo_id())
    props.setOrigin(300, 300)
    props.setSize(500, 500)

    base.makeDefaultPipe()
    base.openDefaultWindow(props=props)

    scene = base.loader.loadModel("environment")
    scene.reparentTo(render)

tkinter_window = Tkinter_window()
tkinter_window.run()

# btn1 = Button(root,text="hello",command=fun)  
# btn1.pack(side=BOTTOM)   

# class main():
#     def __init__(self, master):

#         self.runv = True 

#         m1 = PanedWindow(relief=RAISED, sashrelief=RAISED)
#         m1.pack(fill=BOTH, expand=1)

#         frame1 = Frame(m1, bg="#3a3b3d")

#         menubutton = Menubutton(frame1, text = "File", bg="#3a3b3d", fg="#ffffff", activebackground="#3a3b3d")    
            
#         menubutton.menu = Menu(menubutton)   
#         menubutton["menu"]= menubutton.menu   
        
#         var1 = IntVar() 
#         var2 = IntVar() 
#         var3 = IntVar() 
        
#         menubutton.menu.add_checkbutton(label = "New", 
#                                         variable = var1)   
#         open_file_button = menubutton.menu.add_checkbutton(label = "Open", 
#                                         variable = var2) 
#         menubutton.menu.add_checkbutton(label = "Save", 
#                                         variable = var3) 
            
#         menubutton.pack(anchor="nw")  

#         self.app = Tkinter_window(m1)
#         m1.add(self.app)

#         m1.add(frame1, width=400)
#         self.right = Text(frame1, bg="#3a3b3d", fg="#ffffff", insertbackground='white')
#         self.right.pack(fill=BOTH, expand=1)

#         rightb = Button(frame1, text="run")
#         rightb.pack()

# if __name__ == '__main__':
#     root =Tk()
#     root.title("Shaun Engine")
#     app = main(root)
#     root.mainloop()