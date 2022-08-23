# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="3d_db")
# mycursor=mydb.cursor()
import sqlite3
mydb = sqlite3.connect('database/3d_db.db') 
mycursor = mydb.cursor()
std_table='''CREATE TABLE IF NOT EXISTS std 
(std_id INTEGER PRIMARY KEY AUTOINCREMENT,
 std_name CHAR(25) NOT NULL);'''

sub_table='''CREATE TABLE IF NOT EXISTS sub 
(sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
 sub_name CHAR(25) NOT NULL);'''

ch_table='''CREATE TABLE IF NOT EXISTS chapter 
(ch_id INTEGER PRIMARY KEY AUTOINCREMENT,
 ch_name CHAR(25) NOT NULL);'''

model_table='''CREATE TABLE IF NOT EXISTS model_file
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 std_id INTEGER NOT NULL,
 sub_id INTEGER NOT NULL,
 ch_id INTEGER NOT NULL,
 topic_name CHAR(50) NOT NULL,
 filename CHAR(50) NOT NULL,
 thumbnail_name CHAR(50) NOT NULL,
 model_desc CHAR(50) NOT NULL,
 favorite BOOLEAN NOT NULL,
 FOREIGN KEY(std_id) REFERENCES std(std_id),
 FOREIGN KEY(sub_id) REFERENCES sub(sub_id),
 FOREIGN KEY(ch_id) REFERENCES chapter(ch_id));'''

video_table='''CREATE TABLE IF NOT EXISTS video
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 std_id INTEGER NOT NULL,
 sub_id INTEGER NOT NULL,
 ch_id INTEGER NOT NULL,
 topic_name CHAR(50) NOT NULL,
 v_name CHAR(50) NOT NULL,
 thumbnail_name CHAR(50) NOT NULL,
 video_desc CHAR(50) NOT NULL,
 favorite BOOLEAN NOT NULL,
 FOREIGN KEY(std_id) REFERENCES std(std_id),
 FOREIGN KEY(sub_id) REFERENCES sub(sub_id),
 FOREIGN KEY(ch_id) REFERENCES chapter(ch_id));'''

history_table='''CREATE TABLE IF NOT EXISTS history
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 m_v_id INTEGER NOT NULL,
 type CHAR(50) NOT NULL,
 date_time TEXT NOT NULL)'''
del_tab='''DROP TABLE history'''
update=f'''UPDATE model_file set favorite={True} WHERE id=1'''
insert=f'''INSERT INTO std(std_name) VALUES('1st')'''
# mycursor.execute(std_table)
mycursor.execute(sub_table)
mycursor.execute(ch_table)
mycursor.execute(model_table)
mycursor.execute(video_table)
# mycursor.execute(del_tab)
mycursor.execute(history_table)
mycursor.execute(update)
mydb.commit()
# mycursor.execute(insert)
# mydb.commit()
