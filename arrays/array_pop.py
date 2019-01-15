import array as a
x=a.array('I',[12,34,56,78,656,100,56])
print "Given array x is :",x
y=x.pop(3)
print "After Removing third position value x is :",x
print "The Removed value is :",y
z=x.pop()
print "Pop() without index value removes last value so x is :",x
print "The Removed last vale is :",z
