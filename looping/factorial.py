print "Factorial of the Given Number"
print "----------------------------"
n=input("Number to find Factorial : ")
i=1
ans=1
while i<=n:
    ans=ans*i
    i=i+1
print "Factorial of "+str(n)+" is :  "+str(ans)
