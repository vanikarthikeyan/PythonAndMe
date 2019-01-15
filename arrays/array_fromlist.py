import array as a
x=a.array('I',[12,34,56,78,656])
print "Given array x is :",x
l=[100,200,300,400]
print "Given list is :",l
x.fromlist(l)
print "After adding list content using fromlist() is :",x
