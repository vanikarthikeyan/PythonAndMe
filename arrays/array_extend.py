import array as a
x=a.array('I',[12,34,56,78,656])
print "Given array x is :",x
y=a.array('I',[1,2,3,4,5])
print "given array y is :",y
x.extend(y)
print "After exnding x is :",x
l=[100,200,300,400]
print "Given list is :",l
x.extend(l)
print "After extending x from list l is :",x
