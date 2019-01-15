python=0
rollno=0
name=""
def datainput():
    global python
    global rollno
    global name
    print "Data Input Function"
    print "-------------------"
    rollno=input("Roll no     : ")
    name=raw_input("Name        : ")
    python=input("Python Mark : ")
def output():
    print "Data Output Function"
    print "--------------------"
    print "Roll no     : ",rollno
    print "Name       : ",name
    print "Python      : ",python
print "Use of Global variables"
print "-----------------------"    
datainput()
output()
