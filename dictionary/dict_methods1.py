print "Dictionary Example" 
print "------------------"
d1={'tutor1':"Karthi",101:"Aws",'tutor2':"xyz",105:78.98,107:34+9j}
print "Given dictionary d1 is :",d1
d2=d1.copy()
print "Copied dictionary is :",d2
d2.clear()
print "After clear() d2 is :",d2
print d1.get('tutor2')
d1.popitem()
print "After popitem() d1 is :",d1
d1.pop(107)
print "After pop() d1 is :",d1

