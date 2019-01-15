#import xlwt
try:
    import pymysql
    dbv=pymysql.connect("localhost","user1","hello123","ev")
except 1045:
    print "There is connection error contact admin!!!!"
