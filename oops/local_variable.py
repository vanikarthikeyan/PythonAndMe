class sample():
    c=0
    def __init__(self):
        sample.c=sample.c+1
    def display(self,c):
        self.c=c+10
        print "Local variable c:",c
        print "Object variable c :",self.c
        print "class variable c:",sample.c
s1=sample()
s2=sample()
s3=sample()
s1.display(100)
s2.display(200)
s3.display(300)
