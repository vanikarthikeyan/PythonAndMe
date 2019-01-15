print "Check if  the number is palindrome or not"
print "-----------------------------------------"
n=input("Number to check palindrome :")
rev=0
n1=n
while n!=0:
    r=n%10
    n=n/10
    rev=(rev*10)+r
if rev==n1:
   print str(n1)+ " is palindrome"
else:
   print str(n1)+ " is not palindrome"
