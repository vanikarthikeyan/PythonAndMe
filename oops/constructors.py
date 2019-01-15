class student():
    def __init__(self,v1,v2):
       self.rollno=v1
       self.name=v2
    def display(self):
        print "Roll No : ",self.rollno
        print "Name    : ",self.name
obj1=student(100,"Vibaashini")
obj2=student(101,"Sundar")
obj1.display()
obj2.display()
