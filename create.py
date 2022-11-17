import pymysql
db = pymysql.connect(host='localhost',
                        user='root',
                        password='Veeru@410',
                        database='demo2',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()
query = 'CREATE TABLE employee(fname varchar(50),lname varchar(50), accountnum varchar(10) primary key'
try:
       cursor.execute(query)
       db.commit()
except:
        db.rollback()
db.close()
