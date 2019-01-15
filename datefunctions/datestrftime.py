import datetime,os
cdate=datetime.date.today()
print "Current date is :",cdate
print "current year is :",cdate.strftime("%Y")
print "current month is :",cdate.strftime("%B")
print "Week of the  year is :",cdate.strftime("%W")
print "Day of the week  is :",cdate.strftime("%w")
print "Day of the week in text is :",cdate.strftime("%A")
print "Day of the  year is :",cdate.strftime("%j")
print "Date is :",cdate.strftime("%d")
