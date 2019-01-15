print "Fibonacci Series"
print "----------------"
n=input("Number of terms : ")
f1=-1
f2=1
i=1
while i<=n:
    f3=f1+f2
    print f3
    f1=f2
    f2=f3
    i=i+1
