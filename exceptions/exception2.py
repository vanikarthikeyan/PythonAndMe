try:
    x=input("First Number:")
    y=input("Second Number:")
    z=x/y
    print "Divided value is :",z
except ZeroDivisionError:
    print "Hai!!!! you are trying to divide the number by zero which is not possible"
except NameError:
    print "Hau!! you are trying to give name instead of number"

