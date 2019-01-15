class SmallError:
    pass
class BigError:
    pass
try:
    x=raw_input("Enter the Name:")
    m1=input("Enter the mark:")
    if m1<0:
        raise SmallError
    elif m1>100:
        raise BigError
except SmallError:
    print "Mark should not be negaive number!!!!!!!!!!!!!!!!"
except BigError:
    print "Mark should not be > 100!!!!!!!!!!!!!!!!!!!!"
else:
    print "congrts you have given correct range of errors!!!!!!!!"
    print "Name is :",x
    print "Mark is :",m1
