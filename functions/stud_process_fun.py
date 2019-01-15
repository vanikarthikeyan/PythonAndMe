python=0
java=0
c=0
total=0
avg=0.0
def datainput():
    global python,java,c
    rollno=input("Roll no     : ")
    name=raw_input("Name        : ")
    python=input("Python Mark : ")
    java=input("Java Mark   : ")
    c=input("C Marks     : ")
def calculate():
    global total,avg
    total=python+java+c
    avg=total/3
def output():
    print "Total      : ",total
    print "Average    : ",avg
print "Students Mark List using function"
print "----------------------------------"
datainput()
calculate()
output()
