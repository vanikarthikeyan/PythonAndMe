print "Dictionary Example"
print "------------------"
d1={'tutor1':"Karthi",101:"Aws",'tutor2':"xyz",105:78.98,107:34+9j}
print "Given dictionary d1 is :",d1
x=d1.viewvalues()
print "x is :",x
for i in x:
    print i
y=d1.viewitems()
print "y is :",y
for i in y:
    print i
z=d1.values()
print "z is :",z
