print '\nRead the content from the file, split and store it in a list'
print '--------------------------------------------------------'
filename=open("sample22.txt","r")
for line in filename:
    line=line.rstrip()
    print line
filename.close()
filename=open("sample22.txt","r")
print "\n Extracted mail lines from the file"
print "-------------------------------------"
for line in filename:
    line=line.rstrip()
    if not line.startswith('From'):
        continue
    words=line.split()
    print words
