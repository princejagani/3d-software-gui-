from  db_module import *
from PyQt5 import QtCore, QtGui
icon=QtGui.QIcon()
def fav(id,btn):
        print(id)
        sql1=f"SELECT favorite FROM video WHERE id={id}"
        mycursor.execute(sql1)
        myresult=mycursor.fetchall()
        if(myresult[0][0]==0):
            sql=f"UPDATE  video SET favorite={True} WHERE id={id}"
            mycursor.execute(sql)
            mydb.commit()
            icon.addPixmap(QtGui.QPixmap("icon/favorites.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn.setIcon(icon)
        elif(myresult[0][0]==1):
            sql=f"UPDATE  video SET favorite={False} WHERE id={id}"
            mycursor.execute(sql)
            mydb.commit()
            icon.addPixmap(QtGui.QPixmap("icon/favorite1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn.setIcon(icon)

def fav_model(id,btn):
        sql11=f"SELECT favorite FROM model_file WHERE id={id}"
        print(sql11)
        mycursor.execute(sql11)
        myresult1=mycursor.fetchall()
        print(myresult1)
        if(myresult1[0][0]==0):
            sqli=f"UPDATE  model_file SET favorite={True} WHERE id={id}"
            mycursor.execute(sqli)
            mydb.commit()
            icon.addPixmap(QtGui.QPixmap("icon/favorites.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn.setIcon(icon)       
        elif(myresult1[0][0]==1):
            sqli=f"UPDATE  model_file SET favorite={False} WHERE id={id}"
            mycursor.execute(sqli)
            mydb.commit()
            icon.addPixmap(QtGui.QPixmap("icon/favorite1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            btn.setIcon(icon)
 



            