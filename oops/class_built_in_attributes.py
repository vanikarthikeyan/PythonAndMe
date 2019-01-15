class builtin_attributes():
    """ this is sample class
      to demonstrate built-in attribute"""
    def __init__(self,a):
        self.x=a
    def display(self):
        print "Values is=",self.x
obj1=builtin_attributes(147)
obj1.display()
print "Built-inAttributes of class"
print "---------------------------"
print "Attributes of the class as dictionary values using ._ _dict_ _"
print "---------------------------------------------"
print obj1.__dict__
print "Comment line of the class using ._ _doc_ _"
print "----------------------------------------"
print obj1.__doc__
print "class name using . _ _name_ _"
print "--------------------------------"
print builtin_attributes.__name__
print "Baseclass name"
print "---------------"
print builtin_attributes.__bases__
