import pymysql
connection = pymysql.connect(host='localhost',
                        user='root',
                        password='Veeru@410',
                        database='demo2',
                        cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "SELECT * FROM STUDENT "
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)


