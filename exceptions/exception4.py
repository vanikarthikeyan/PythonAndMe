try:
    x=input("First Number:")
    y=input("Second Number:")
    z=x/y
except ZeroDivisionError:
    print "Hai!!!! you are trying to divide the number by zero which is not possible"
    print "Give the value for y again!!!!!!!!!!!"
    y=input("Second Number:")
    z=x/y
    print "Divided value is :",z
else:
    print "congrts!!!!!!!!!!you have given correct values"
    print "Divided value is :",z

