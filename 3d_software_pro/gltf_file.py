from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import load_prc_file
import simplepbr
from direct.task import Task
from math import pi, sin, cos
from panda3d.core import WindowProperties

load_prc_file('myconfig.prc')

class Slugrace3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self,windowType='none')
        simplepbr.init()
        ShowBase.start_tk()
        """props=WindowProperties()
        props.setTitle('test game')
        props.setSize(1200,675)
        props.setCursorHidden(True)
        base.win.requestProperties(props)"""
        frame = ShowBase.tkRoot
        frame.update()
        

        self.building=self.loader.loadModel("proj1.gltf")
        self.building.setPos(0,50,0)
        self.building.reparentTo(self.render)

app=Slugrace3D()    
app.run()

