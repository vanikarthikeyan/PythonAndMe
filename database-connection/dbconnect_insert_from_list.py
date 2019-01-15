import pymysql
dbc=pymysql.connect("localhost","user1","hello123","dev")
cur=dbc.cursor()
x=[[106,'xxxx','bodi'],[107,'yyyy','zzzzz']]
for i in x:
    cur.execute("insert into student values('%d','%s','%s')"%(i[0],i[1],i[2]))
dbc.commit()
dbc.close()
