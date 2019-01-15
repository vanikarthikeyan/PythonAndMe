print "Multiplication Table"
print "--------------------"
n=input("Enter the number to generate multiplication table : ")
i=1
while i<=20:
    ans=i*n
    print str(i)+"  * "+str(n)+"="+str(ans)
    i=i+1
