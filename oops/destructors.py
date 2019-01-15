class sample5():
    count=0
    def ___init__(self):
        sample5.count=sample5.count+1
        print "Object Number : ",sample5.count
    def __del__(self):
        print "Destroying object : ",sample5.count
        sample5.count=sample5.count-1
obj1=sample5()
obj2=sample5()
