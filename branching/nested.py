#Program for if statements
#Author:K.Vani
#Date:16.12.1018
#Batch :Devops December 2018
print "Example for if satement"
print "----------------------"
x=input("Enter the Value for x:")
y=input("Enter the value for y:")
z=input("Enter the Value for z:")
a=input("Enter the value for a:")
"""if x>y and x>z and x>a :
    print "x is greatest among the all"
else:
    print "other number is greateri" """
    
if x>y and x>z and x>a :
    print "x is greatest among the all"
elif y>x and y>z and y>a:
    print "y is greatest"
elif z>x and z>y and z>a:
        print "z is greatest"
else:
    print "a is greatest"
'''if x>y:
    if x>z:
        if x>a:
            print "X is greatest among all 4 numbers"
        else:
            print "x is not greater than a"
    else:
        print "X is not greater than z"
else:
    print "X is not greater than y"'''
