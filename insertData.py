import time
import MySQLdb

def insertData(data):
    db = MySQLdb.connect("localhost", "pyUser", "meiyoumima", "MainDB")

    cursor = db.cursor()

    sql = "INSERT INTO tempData (PM, latitude, longitude, time) VALUES("
    sql += str(data['PM']) +','
    sql += str(data['latitude']) + ','
    sql += str(data['longitude']) + ','
    sql += "'" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + "'" + ');'

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()
