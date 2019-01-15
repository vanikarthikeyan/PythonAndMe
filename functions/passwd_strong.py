def validate(pwd):
    lenthcheck=False
    uppercasecheck=False
    lowercasecheck=False
    numericcheck=False
    u=0
    l=0
    d=0
    l=len(pwd)
    if l>=8:
        lengthcheck=True
    for ch in pwd:
        if ch.isupper():
           u=u+1
        if ch.islower():
           l=l+1
        if ch.isdigit():
           d=d+1
    if u >0:
        uppercasecheck=True
    if l>0:
        lowercasecheck=True
    if d>0:
        numericcheck=True
    if uppercasecheck and lowercasecheck and numericcheck and  lengthcheck :
       return True
    else:
       return False
print "Password checking"
print "-------------------------"
uname=raw_input("User Name : ")
passwd=raw_input("Password : ")
flag=validate(passwd)
if flag:
    print "Password is strong. It contains >= 8chars,uppercase,lowercase,numeric"
else:
    print "Password is not Strong. It may miss uppercase,lowercase,numeric and may be <8chars"
