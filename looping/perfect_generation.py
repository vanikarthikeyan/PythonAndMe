print "Perfect Number Generation "
print "--------------------------"
n=input("Range to generate : ")
j=1
while j<=n:
    i=1
    ans=0
    while i<j:
        if j%i==0:
            ans=ans+i
        i=i+1
    if ans==j:
        print j
    j=j+1
