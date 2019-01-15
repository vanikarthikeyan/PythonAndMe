#print ord("A")
x=raw_input("Enter the string:")
l=len(x)
for i in range(l):
    y=ord(x[i])
    if y>=97 and y<=122:
        print y,"lowercase"
    else:
        print y,"Uppercase"
