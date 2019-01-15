import datetime,os
mtime=os.path.getmtime("/home/student/monitoring/disk-usage.py")
print mtime
ts=datetime.datetime.fromtimestamp(mtime)
print ts
mdate=ts.date()
print mdate
cdate=datetime.date.today()
print cdate
diff=cdate-mdate
print diff
dint=diff.days
print dint

