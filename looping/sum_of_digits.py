print "Sum of the Digits"
print "---------------"
n=input("Number to sum the digits :")
rev=0
while n!=0:
    r=n%10
    n=n/10
    rev=rev+r
print "Sum of the digits is  : ",rev
