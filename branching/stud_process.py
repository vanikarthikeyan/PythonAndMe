print 'Students Mark List'
print '-----------------'
rollno=input("Rollno       : ")
name=raw_input("Name         : ")
m1=input("Mark1        : ")
m2=input("Mark2        : ")
m3=input("Mark3        : ")
total=m1+m2+m3
avg=total/3.0
print "Total        : ",total
print "Average      : ",avg
if m1<50 or m2<50 or m3<50:
    result="Fail"
    clas="NIL"
elif avg>=85:
    result="Pass"
    clas="FWD" 
elif avg>=70 and avg<85:
    result="Pass"
    clas="FC"     
elif avg>=60 and avg<70:
    result="Pass"
    clas="SC"     
elif avg<60:
    result="Pass"
    clas="TC"     
print "Result       : ",result
print "Class        : ",clas
