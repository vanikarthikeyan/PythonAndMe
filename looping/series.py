print "Sum of  the Series 1/30+2/29+3/28+.......30/1"
print "----------------------------------------------"
i=1
j=30
ans=0.0
while i<=30:
    k=j*1.0
    ans=ans+(i/j)
    i=i+1
    j=j-1
print "Sum of the Series is : ",ans
