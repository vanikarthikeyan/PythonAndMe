import datetime
cdate=datetime.datetime.today()
print "Current date is :",cdate
df=datetime.timedelta(days=10)
print "after converting :",df
'''pdate=cdate-10
ndate=cdate+10
print "previous date is :",pdate
print "next date is :",ndate'''

pdate=cdate-df
ndate=cdate+df

print "previous date is :",pdate
print "next date is :",ndate
