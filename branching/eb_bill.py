print 'Electric Bill Calculation'
print '-------------------------'
cid=input("Id           : ")
name=raw_input("Name         : ")
addr=raw_input("Address      : ")
units=input("Units        : ")
if units<=100:
    amt=100.00
elif units >100 and units<=200:
    amt=100.00+(units-100)*2.25
elif units >200 and units<=300:
    amt=100.00+(50*2.25)+(50*2.75)+(units-200)*3.25
elif units >300:
    amt=100.00+(50*2.25)+(50*2.75)+(100*3.25)+(units-300)*3.75
print "Amount       : ",amt	
