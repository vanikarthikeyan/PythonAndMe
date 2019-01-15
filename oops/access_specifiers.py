class accessspecifier():
    def __init__(self,a,b):
        self.x=a
        self.__y=b
    def __display(self):
        print "From private method display public variable x is  : ",self.x
        print "From private method display private variable y is : ",self.__y
    def display1(self):
        print "From public method display1 public variable x is : ",self.x
        print "From public method display1 private variable y is : ",self.__y
        print "Calling the private method display inside the public function display1"
        print "-------------------------------------------------------"
        self.__display()
obj1=accessspecifier(10,20)
print "Calling of public method"
print "------------------------"
obj1.display1()
print "Calling the private method using objectname and classname"
print "----------------------------------------------------------"
obj1._accessspecifier.__display()
print "Calling the private method using object name only"
print "--------------------------------------------------"
obj1.__display()
