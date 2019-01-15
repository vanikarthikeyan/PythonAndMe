print "Reverse the Number"
print "-------------------"
n=input("Number to Reverse :")
rev=0
while n!=0:
    r=n%10
    n=n/10
    rev=(rev*10)+r
print "Reverse the Number is : ",rev
