import array as a
import os
x=a.array('I',[12,34,56,78,656,100,56])
print "Given array x is :",x
fp=open("arraycontent.txt","w")
x.tofile(fp)
print "Array content in file is "
print "------------------------"
os.system("cat arraycontent.txt")
