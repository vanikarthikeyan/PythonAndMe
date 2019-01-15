class tutors():
    def __init__(self,tname,texp,tinterest):
         self.tutorname=tname
         self.tutorexp=texp
         self.tutorinterest=tinterest
    def tdisplay(self):
         print "Tutor Information"
         print "-----------------"
         print "Tutor Name       : ",self.tutorname
         print "Tutor Experience : ",self.tutorexp
         print "Tutor Area of Interest :",self.tutorinterest
class students(tutors):
    def __init__(self,sname1,sdob1,scourse1,tname1,texp1,tinterest1):
         tutors.__init__(self,tname1,texp1,tinterest1)
         self.sname=sname1
         self.sdob=sdob1
         self.scourse=scourse1
    def sdisplay(self):
         print "Students Information"
         print "--------------------"
         print "Student Name : ",self.sname
         print "Student Dob  : ",self.sdob
         print "Courses      : ",self.scourse
s1=students("Jayanthi","22-02-2013","Python","Vani",17,"C,C++,Java and Python")
s1.tdisplay()
s1.sdisplay()
