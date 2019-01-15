print "Perfect Number Checking"
print "------------------------"
n=input("Number to check : ")
i=1
ans=0
while i<n:
    if n%i==0:
        ans=ans+i
    i=i+1
if ans==n:
    print str(n)+" is perfect number"
else:
    print str(n)+" is not a perfect number"
