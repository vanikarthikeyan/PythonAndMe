#print ord("A")
x=raw_input("Enter the string:")
l=len(x)
flag=0
for i in range(l):
    y=ord(x[i])
    if y>=65 and y<=91:
        flag=flag+1
if flag==0:
    print "True"
else:
    print "False"


