from datetime import datetime
from db_module import *

def count_history(id,type):
    date_time= datetime.now()
    sql=f"INSERT INTO history(m_v_id,type,date_time) VALUES({id},'{type}','{date_time}');"
    mycursor.execute(sql)
    try:
        mydb.commit()
    except:
        print("error for histroy")

# sql=f"SELECT * FROM history ORDER BY date_time DESC"
# mycursor.execute(sql)
# myresult=mycursor.fetchall()
# print(myresult)
