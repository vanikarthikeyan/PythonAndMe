print "List within a list"
print "------------------"
x=[[10,20],3,"python",[30,40,50],"BSS"]
print "Given list is : ",x
print "using for loop"
print "---------------"
for i in x:
    print i
print "Accessing inner list values"
print "---------------------------"
print "0th position's 1st value :",x[0][1]
print "3rd position's 0th value :",x[3][0]
print "After changing tha values in a list"
print "-----------------------------------"
x[1]=33
x[3][0]=300
print "List x : ",x
