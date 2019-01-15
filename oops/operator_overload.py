class op_overload():
     def getvalue(self):
         print "Getting values"
         print "--------------"
         self.x=input("Enter the value for x : ")
     def display(self):
         print "x=",self.x
     def __add__(self,obj4):
         temp=op_overload()
         temp.x=self.x+obj4.x
         return temp
obj1=op_overload()
obj2=op_overload()
obj3=op_overload()
obj1.getvalue()
obj2.getvalue()
obj3=obj1+obj2
print "After adding two objects using operator overloading concept"
print "-----------------------------------------------------------"
obj1.display()
obj2.display()
obj3.display()
