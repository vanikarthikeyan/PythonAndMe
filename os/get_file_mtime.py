import os
for p,s,f in os.walk("/home/student/monitoring"):
    for j in f:
        x=os.path.join(p,j)
        y=os.path.getsize(x)
        mt=os.path.getmtime(x)
        print x,y,mt
   

