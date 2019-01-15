x=open("vani.txt","r")
y=x.read(6)
print "First five chars are :",y
z=x.read(7)
print "next 7 chars are:",z
a=x.read()
print "Remaing chars are:",a
x.close()

