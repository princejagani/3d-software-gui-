
# # drives = win32api.GetLogicalDriveStrings()
# # drives = drives.split('\000')[:-1]
# # print (drives)

# # pd=[]
# drives = win32api.GetLogicalDriveStrings()
# pd = drives.split('\000')[:-1]

# while True:
#     drives = win32api.GetLogicalDriveStrings()
#     drives = drives.split('\000')[:-1]

#     if pd != drives:
#         temp=[]
#         # print('hi')
#         for i in pd:
#             if i not in drives and i not in temp:
#                 temp.append(i)
#         for i in drives:
#             if i not in pd and i not in temp:
#                 temp.append(i)
#         for i in temp:
#             if os.path.exists(i):
#                 print(i)
#                 src= r'E:\Untitled.png'
#                 dst = r'D:\ro.png'
#                 shutil.copyfile(src, dst)


#         pd=drives
    # time.sleep(1) 



from turtle import mode
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import win32api
import win32con
import win32file
import win32api,time,os,shutil

class usb_drive():
    def __init__(self):
        self.val=False
    
    def btn_click(self):
        self.val=True
        self.start_progressBar.hide()
        return self.val
    def detect_usb(self,model_widget,gridLayout,ok_btn,success_label,internet_btn,cd_btn,sub_title_label):
        global mymsg
        mymsg=QMessageBox()
        rdrives=[]
        folder_name='demo'
        status=True
        global msg
        def get_removable_drives():
            drives = [i for i in win32api.GetLogicalDriveStrings().split('\x00') if i]
            rdrives = [d for d in drives if win32file.GetDriveType(d) == win32con.DRIVE_REMOVABLE]
            return rdrives

        # print(get_removable_drives())
        pd=[]
        
   

        self.start_progressBar = QtWidgets.QProgressBar(model_widget)
        self.start_progressBar.setMinimumSize(QtCore.QSize(600, 40))
        self.start_progressBar.setMaximumSize(QtCore.QSize(600, 40))
        self.start_progressBar.hide()
        self.start_progressBar.setGeometry(420, 290, 300, 40)
        self.start_progressBar.setStyleSheet("\n"
    "\n"
    "QProgressBar\n"
    "{\n"
    "\n"
    "    background-color: rgb(53, 53, 53);\n"
    "\n"
    "    color: rgb(0, 0, 0);\n"
    "\n"
    "}\n"
    "QProgressBar::chunk \n"
    "{\n"
    "background-color:rgb(248,180,100);\n"
    "border-radius :10px;\n"
    "}  ")
        # self.start_progressBar.setProperty("value", 100)
        self.start_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.start_progressBar.setObjectName("start_progressBar")
        gridLayout.addWidget(self.start_progressBar, 0, 1, 1, 3)
        # gridLayout.addWidget(self.ok_btn)
        
        drives=get_removable_drives()
        if pd != drives:
            for i in drives:
                file_list=os.listdir(f"{i}")
                if(folder_name in file_list):
                    file_list=os.listdir(f"{i}/{folder_name}")
                    self.start_progressBar.show()
                    self.start_progressBar.setMaximum(len(file_list)-1)
                    for j in range(0,len(file_list)):
                        
                        try:
                            src= f'{i}{folder_name}\\{file_list[j]}'
                            dst = f'D:\\{file_list[j]}'
                            shutil.copyfile(src, dst)
                            time.sleep(0.05)
                            self.start_progressBar.setValue(j)
                        except:
                            print("Error")
                            status=False
                            mymsg.setIcon(QMessageBox.Information)
                            mymsg.setText("We have face some error please try again later")
                            mymsg.setStandardButtons(QMessageBox.Ok)
                            mymsg.resize(400,200)
                            mymsg.show()
                    if(status==True):
                        success_label.show()
                        ok_btn.show()
                        
                        # start_progressBar.setValue(101)
                        # mymsg.setIcon(QMessageBox.Information)
                        # mymsg.setText("Data copied successfully")
                        # mymsg.setStandardButtons(QMessageBox.Ok)
                        # mymsg.resize(400,200)
                        # mymsg.show()
                        print("Data Cpoied")
                        msg="Data Cpoied"
                        return msg
                else:
                    cd_btn.show()
                    internet_btn.show()
                    sub_title_label.show()
                    mymsg.setIcon(QMessageBox.Information)
                    mymsg.setText("Pendrive not suitable")
                    mymsg.setStandardButtons(QMessageBox.Ok)
                    mymsg.resize(400,200)
                    mymsg.show()
            pd=drives
            time.sleep(0.05)
        else:
            cd_btn.show()
            internet_btn.show()
            sub_title_label.show()
            mymsg.setIcon(QMessageBox.Information)
            mymsg.setText("Please attach pendrive")
            mymsg.setStandardButtons(QMessageBox.Ok)
            mymsg.resize(400,200)
            mymsg.show()
            msg="Please Attach Pendrive"
            return msg
    






