import os
import crypt
fp=open("username.txt","r")
list1=fp.readlines()
print "File Lines : ",list1
print "After removing newline character"
print "--------------------------------"
str1=""
for i in list1:
    if i!= "\n":
        str1=str1+i
print str1
list2=str1.split()
print "After Split the string into individual words"
print "---------------------------------------------"
print list2 
l=len(list2)
for i in range(0,l,2):
    pw=crypt.crypt(list2[i+1], "125")
    un="sudo useradd -m -p "+pw+" " +list2[i]
    print pw
    print un
    os.system(un)
