import pymysql
db = pymysql.connect(host='localhost',
                        user='root',
                        password='Veeru@410',
                        database='demo5',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query = "alter table employee add phno int(10)"
try:
       cursor.execute(query)
       db.commit()
except:
        db.rollback()
db.close()
