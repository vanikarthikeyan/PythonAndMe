import array as a
x=a.array('I',[12,34,56,78,656,100,56])
print "Given array x is :",x
fp=open("arraycontent.txt","w")
y=x.tolist()
print "Array content as list using tolist() :",y
