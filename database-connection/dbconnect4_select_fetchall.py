import pymysql
dbc=pymysql.connect("localhost","user1","hello123","dev")
cur=dbc.cursor()
cur.execute("select * from student")
result=cur.fetchall()
print result
for i in result:
    print i
dbc.close()
