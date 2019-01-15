import array as a
x=a.array("I",[100,200,300,400,500])
print "Array datatype is :",x.typecode
print "Array length in bytes :",x.itemsize
print " Address and length :",x.buffer_info()
