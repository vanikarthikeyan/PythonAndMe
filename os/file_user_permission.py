import os
pathname=raw_input("Enter the path name : ")
fname=raw_input("Enter Resultant File : ")
f=open(fname,"a")
for paths,subdirs,files in os.walk(pathname):
    for fname in files:
        x=os.path.join(paths,fname);
        if os.access(x,os.W_OK):
            if os.access(x,os.R_OK):
                if os.access(x,os.X_OK):
                   f.write(x+"\n")
f.close()
