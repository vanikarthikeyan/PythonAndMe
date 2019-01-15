def ascend(list1):
    i=0
    x=len(list1)
    if x==0:
        return True
    else:
        while i<x-1:
            if list1[i+1] < list1[i]:
                return False
            i=i+1
        return True
x=ascend([])
print "Ascending order : ",x
x=ascend([3,3,4])
print "Ascending order : ",x
x=ascend([7,18,17,19])
print "Ascending order : ",x
