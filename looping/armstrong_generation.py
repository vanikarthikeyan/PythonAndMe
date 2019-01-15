print "Armstrong number Generation "
print "----------------------------"
n=input("Range to Generate : ")
j=1
while j<=n:
    n1=j
    ans=0
    while n1!=0:
        r=n1%10
        ans=ans+(r**3)
        n1=n1/10
    if ans==j:
       print j
    j=j+1
