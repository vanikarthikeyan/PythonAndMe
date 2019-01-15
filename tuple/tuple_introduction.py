print "Tuple examples"
print "--------------"

x=()
y=tuple()
z=(10,12.34,"Vani",56+9j,True)
print "x is :",x
print "y is :",y
print "z is :",z
'''z[0]=100
z.append(123)
print "After modifying z is :",z'''
print "4th positon element is :",z[4]
print "Using while loop"
print "---------------"
i=0
l=len(z)
while i<l:
    print z[i]
    i=i+1
print "Using for loop"
print "--------------"
for i in z:
    print i
