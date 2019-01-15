import pymysql
dbc=pymysql.connect("localhost","user1","hello123","dev")
cur=dbc.cursor()
cur.execute("select * from student")
r=cur.rowcount
for i in range(r):
    x=cur.fetchone()
    print x
dbc.close()
