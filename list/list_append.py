print '\nAppend the values in the list by getting the values from user'
print '----------------------------------------------------------------'
print '\n List is created list()'
print '------------------------'
tutors=list()
while True:
    value=raw_input("Enter the tutor Names : ")
    if value=='end':
        break;
    tutors.append(value)
print '\nValues of the list'
print '--------------------'
print tutors
