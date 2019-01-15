print "Students.txt file content with line numbers"
print "-------------------------------------------"
count=1
fp=open("students.txt","r")
for l in fp:
    print str(count)+' : '+str(l)
    count=count+1
