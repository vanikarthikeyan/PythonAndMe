import os
filename=raw_input("Enter the filename:")
mtime=os.path.getmtime(filename)
print 'File Modified time is :',mtime)
