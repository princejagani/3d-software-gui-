import win32api,time,os,shutil

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




import win32api
import win32con
import win32file

def get_removable_drives():
    drives = [i for i in win32api.GetLogicalDriveStrings().split('\x00') if i]
    rdrives = [d for d in drives if win32file.GetDriveType(d) == win32con.DRIVE_REMOVABLE]
    return rdrives

# print(get_removable_drives())
pd=[]

while True:

    drives=get_removable_drives()
    if pd != drives:
        for i in drives:
            print(i)
            src= f'{i}demo/demo.txt'
            dst = f'D:\\demo.txt'
            shutil.copyfile(src, dst)
        pd=drives

    
    time.sleep(1) 






