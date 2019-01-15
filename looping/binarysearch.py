li =[23,56,7,23,1,58,98,67,567,890,234]
print "Given values are"
print "----------------"
print li
li.sort()
print "After Sorting"
print "-------------"
print li
s=input("Enter value to search : ")
start=0
end=len(li)-1
found=False
first=0
last=len(li)-1
while (first <= last and not found):
    mid=(start+end)//2
    if(li[mid]==s):
        found=True
        pos=mid
    elif (s<li[mid]):
        end=mid - 1
        last=end
    else:
        start=mid + 1
        first=start
if (found):
    print(s,"found at", mid)
else:
    print(s,"not found")
