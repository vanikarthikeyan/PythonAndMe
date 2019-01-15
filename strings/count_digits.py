print "Counting the number of digits in the string"
print "------------------------------------------"
str1=raw_input("Enter the String  :")
count=0
for ch in str1:
    if ch.isdigit():
         count=count+1
print "Number of digits in the given string is : ",count
