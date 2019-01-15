print "Counting the number of spaces in the string"
print "--------------------------------------------"
str1=raw_input("Enter the String  :")
count=0
for ch in str1:
    if ch.isspace():
         count=count+1
print "Number of spaces in the given string is : ",count
