import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="3d_db")
mycursor=mydb.cursor()