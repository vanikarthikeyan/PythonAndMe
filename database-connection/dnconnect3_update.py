import pymysql
dbc=pymysql.connect("localhost","user1","hello123","dev")
cur=dbc.cursor()
#cur.execute("update student set name='ashok' where rollno=107")
x=106
cur.execute("update student set name='ashok' where rollno='%d'"%(x))
dbc.commit()
dbc.close()
