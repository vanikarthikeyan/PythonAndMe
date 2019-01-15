'''def add(x,y):
    z=x+y
    print "Added value is :",z
def add1(a,b,c):
    d=a+b+c
    print "added value is :",d'''
def add(*x):
    print x
    s=0
    for i in x:
        s=s+i
    print "ADded value is :",s



  

add(12,13)
add(12,14,67)
add(1,2,3,4)

