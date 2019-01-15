import os
def odd():
    os.system("clear")
    print "ODD/EVEN Checking"
    print "-----------------"
    x=input("Number to check : ")
    if x%2==0:
        print x,' is EVEN number'
    else:
        print x,' is not ODD number'
def prime():
    os.system("clear")
    print "Prime Number Checking"
    print "---------------------"
    x=input("Number to check : ")
    i=2
    flag=0
    while i<x:
        if x%2==0:
            flag=flag+1
        i=i+1
    if flag==0:
        print x,' is prime number'
    else:
        print x, ' is not prime number'
def perfect():
    os.system("clear")
    print "Perfect Number Checking"
    print "----------------------"
    x=input("Number to Check : ")
    i=1
    s=0
    while i<x:
        if x%i==0:
            s=s+i
        i=i+1
    if x==s:
        return 1
    else:
        return 0
def armstrong(y):
    y1=y
    s=0
    while y!=0:
        r=y%10
        s=s+(r**3)
        y=y/10
    if s==y1:
        return 1
    else:
        return 0
choice=0
while choice!=5:
    print "Number Checking Using Functions"
    print "-------------------------------"
    print "    1. ODD/EVEN Checking"
    print "    2. Prime Number Checking"
    print "    3. Perfect Number Checking"
    print "    4. Armstrong Number Checking"
    print "    5. Exit"
    choice=input( "UR Choice : ")
    if choice==1:
        odd()
    if choice==2:
        prime()
    if choice==3:
        z=perfect()
        if z==1:
            print 'Given number is perfect number'
        else:
            print "Given number is not a perfect number"
    if choice==4:
        os.system("clear")
        print "Armstrong Number Checking"
        print "-------------------------"
        x=input("Number to Check : ")
        z=armstrong(x)
        if z==1:
            print "Given number is Armstrong"
        else:
            print "Given number is not Armstrong"
    if choice==5:
        break
print "Thank you"
