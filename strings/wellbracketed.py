def bracketchecking(str1):
    c1=0
    c2=0
    for i in str1:
        if i=='(':
            c1=c1+1
        if i==')':
            c2=c2+1
    if c1==c2:
        print "True"
    else:
        print "False"
str2=raw_input("Enter the string : ")
bracketchecking(str2)
