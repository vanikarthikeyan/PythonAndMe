print "List examples"
print "-------------"

x=[100,"vani",90.87,True,89+9j]
print "Given value is :",x

print "using while loop"
print "----------------"
i=0
l=len(x)
print "Total number of elements are :",l
while i<l:
    print x[i]
    i=i+1
    
print "using for loop"
print "---------------"

for y in x:
    print y

print x[:2]
