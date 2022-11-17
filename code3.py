import pymysql
db = pymysql.connect(host='localhost',
                        user='root',
                        password='Veeru@410',
                        database='demo5',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query1 = 'INSERT INTO employee VALUES("John","dell",24,"0812c")'
query2= 'INSERT INTO employee VALUES("bhanu","HP",24,"0812c")'
try:
       cursor.execute(query1)
       cursor.execute(query2)
       db.commit()
except:
        db.rollback()
db.close()
