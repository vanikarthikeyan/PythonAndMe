print "Check if the number is prime or not"
print "------------------------------------"
n=input("Number for prime number checking : ")
i=2
flag=0
while i<=n/2:
    if n%i ==0:
        flag=flag+1
    i=i+1
if flag==0:
    print str(n)+" is prime number"
else:
    print str(n)+" is not a prime number"
