print "Prime Number Generation"
print "-----------------------"
n=input("Range for Generation : ")
j=1
while j<=n:
    i=2
    flag=0
    while i<=j/2:
        if j%i ==0:
            flag=flag+1
        i=i+1
    if flag==0:
        print j
    j=j+1
