import os
import time
for p,s,f in os.walk("/home/student/monitoring"):
    for j in f:
        x=os.path.join(p,j)
        y=os.path.getsize(x)
        mt=os.path.getmtime(x)
        emt=time.ctime(mt)
        print x,y,mt,emt
   

