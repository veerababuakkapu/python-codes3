import pymysql
db = pymysql.connect(host='localhost',
                        user='root',
                        password='Veeru@410',
                        database='demo5',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query = "DELETE FROM employee where age>20"
try:
       cursor.execute(query)
       db.commit()
except:
        db.rollback()
db.close()
