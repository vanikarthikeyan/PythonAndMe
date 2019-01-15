class attributes():
    def __init__(self,a):
        self.x=a
    def display(self):
        print "Values is=",self.x
obj1=attributes(147)
obj1.display()
print "Object has attribute x : ",hasattr(obj1,'x')
print "Object has the attribute y :", hasattr(obj1,'y')
setattr(obj1,'x',134)
print "The new value for the attribute x using setattr fn:",obj1.x
setattr(obj1,'z',345)
print "Creating new attribute 'z' and set value to it using setattr fn :",obj1.z
delattr(obj1,'z')
print "After deleting the attribute z using delarrt fun : ", obj1.z
