import os
print "Counting the number of lowercases,upper cases and whitespaces in a file"
print "------------------------------------------------------------------------"
lower=0
upper=0
spaces=0
fp=open("sample.txt","r")
for line in fp.readlines():
    for ch in line:
        if ch.islower():
           lower=lower+1
        if ch.isupper():
           upper=upper+1
        if ch.isspace():
           spaces=spaces+1
print "File Contents"
print "-------------"
os.system("cat  sample.txt")
print "The Counting Details"
print "--------------------"
print "Number of lower case letters :  ",lower
print "Number of upper case letters :  ",upper
print "Number of white spaces are   : ",spaces
