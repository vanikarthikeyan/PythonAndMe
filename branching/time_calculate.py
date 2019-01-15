print 'Time Calculator'
print '--------------'
sec=input("Enter the number of seconds : ")
if sec>86400:
    day=sec/86400
    r=sec%86400
    hours=r/3600
    r=r%3600
    minu=r/60
elif sec>3600:
    day=0
    hours=sec/3600
    r=sec%3600
    minu=r/60
else:
    day=0
    hours=0
    minu=sec/60
print "Number of Days    : ",day
print "Number of Hours   : ",hours
print "Number of minutes : ",minu
