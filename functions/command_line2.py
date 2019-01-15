import sys
print "\nDemo for Command line Arguments"
print "---------------------------------"
print "\n 0th argument is",sys.argv[0]
print "\n\n Arguments are"
print "------------------"
for i in sys.argv:
    print i
print "\n\n Store the arguments in a variable and accessing"
print "---------------------------------------------------\n"
values=sys.argv[1:]
print values
