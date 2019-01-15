print "Armstrong number Checking"
print "--------------------------"
n=input("Number to Check : ")
n1=n
ans=0
while n!=0:
    r=n%10
    ans=ans+(r**3)
    n=n/10
if ans==n1:
   print str(n1)+" is Armstrong Number"
else:
   print str(n1)+" is not Armstrong Number"
