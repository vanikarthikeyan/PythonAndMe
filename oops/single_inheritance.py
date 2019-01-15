class personal():
    def get_values(self):
        print "Getting the values"
        print "------------------"
        self.name=raw_input("Enter the Name     : ")
        self.addr=raw_input("Enter the Address  : ")
        self.course=raw_input("Enter the Course : ")
    def pdisplay(self):
        print "Personal Information"
        print "--------------------"
        print "Name          : ",self.name
        print "Address       : ",self.addr
        print "Course        : ",self.course
class academic(personal):
    def avalue(self):
        self.m1=input("Enter the Mark1 : ")
        self.m2=input("Enter the Mark2 : ")
        self.m3=input("Enter the Mark3 : ")
        self.total=self.m1+self.m2+self.m3
        self.avg=self.total/3
    def adisplay(self):
        print "Academic Information"
        print "--------------------"
        print "Mark1   : ",self.m1
        print "Mark2   : ",self.m2
        print "Mark3   : ",self.m3
        print "Total   : ",self.total
        print "Average : ",self.avg
obj1=academic()
obj1.get_values()
obj1.avalue()
obj1.pdisplay()
obj1.adisplay()
