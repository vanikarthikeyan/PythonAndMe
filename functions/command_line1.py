import sys
print "\nCommand Line Arguments"
print "----------------------"
print "\nArguments with file name"
print sys.argv
print "\nArguments without filename"
arguments=sys.argv[1:]
print arguments
print '\nNumber of words in the string is :',len(arguments)
