print '\nAppend the values in the list by getting the values from user'
print '--------------------------------------------------------------'
print '\n List is created with specified size using [0]*5'
print '----------------------------------------------------------'
tutors=[0]*5
index=0
while index<5:
    value=raw_input("Enter the tutor Names : ")
    tutors[index]=value
    index=index+1
print '\nValues of the list'
print '-----------------------'
print tutors
