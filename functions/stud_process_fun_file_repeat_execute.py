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
    fp=open("students1.txt","a")
    op=str(rollno)+"     "+name+"     "+str(python)+"     "+str(java)+"     "+str(c)+"     "+str(total)+"     "+str(avg)+"\n"
    print "Content to be write the file : ",op
    fp.write(op)
    fp.close()
choice='y'
while choice=='y' or choice=='Y':
    print "Students Mark List using function"
    print "----------------------------------"
    datainput()
    calculate()
    output()
    choice=raw_input("Do U wish to add another record : ")
print "Students.txt file content"
print "-------------------------"
os.system("cat students1.txt")
