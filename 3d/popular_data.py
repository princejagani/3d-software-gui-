import db_module
def popular(ids,cat):
    if(cat=="model"):
        sql1=f"SELECT popular FROM model_file WHERE id={ids}"
        print(sql1)
        db_module.mycursor.execute(sql1)
        myresult=db_module.mycursor.fetchone()
        count=myresult[0]+1
        sql=f"UPDATE model_file SET popular={count} WHERE id={ids}"
        db_module.mycursor.execute(sql)
        try:
            db_module.mydb.commit()
        except:
            print("error for popular model")
    elif(cat=="video"):
        sql1=f"SELECT popular FROM video WHERE id={ids}"
        db_module.mycursor.execute(sql1)
        myresult=db_module.mycursor.fetchone()
        count=myresult[0]+1
        sql=f"UPDATE video SET popular={count} WHERE id={ids}"
        db_module.mycursor.execute(sql)
        try:
            db_module.mydb.commit()
        except:
            print("error for popular video")