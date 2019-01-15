print "List Methods"
print "------------"

x=[12,45.789,"vani"]
print "Given list is :",x
#z=10
z=[12,23,34]
#x.insert(2,z)
x.insert(2,x.extend(z))
print "After inserting into the list :",x
