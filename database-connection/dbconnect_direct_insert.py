import pymysql
dbc=pymysql.connect("localhost","user1","hello123","dev")
cur=dbc.cursor()
cur.execute("insert into student values(105,'gokul','Kerala')")
dbc.commit()
dbc.close()
