class sample4():
    def __init__(self,a):
       self.x=a
    def display(self):
        print "object variable x from display fn is : ",self.x
obj1=sample4(10)
obj2=sample4(20)
obj1.display()
obj2.display()
