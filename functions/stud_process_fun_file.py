import os
python=0
java=0
c=0
total=0
avg=0.0
def datainput():
    global python,java,c,rollno,name
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
    fp=open("students.txt","a")
    op=str(rollno)+"     "+name+"     "+str(python)+"     "+str(java)+"   "+str(c)+"   "+str(total)+"   "+str(avg)+"\n"
    print "Content to be write the file : ",op
    fp.write(op)
    fp.close()
print "Students Mark List using function"
print "--------------------------------"
datainput()
calculate()
output()
datainput()
calculate()
output()
datainput()
calculate()
output()
print "Students.txt file content"
print "-------------------------"
os.system("cat students.txt")
