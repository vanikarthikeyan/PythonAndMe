import os
print "storing the files with > 1kb into a separate file"
print "--------------------------------------------------"
x1=raw_input("Enter the path:")
x2=raw_input("Enter the output filename:")
f=open(x2,"w")
for paths,dirs,files in os.walk(x1):
    for name in files:
        x=os.path.join(paths,name)
        size=os.path.getsize(x)
        kb=size/1024
        if kb > 1:
            f.write(x+"\n")
f.close()
