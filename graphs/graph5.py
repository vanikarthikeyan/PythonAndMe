import matplotlib.pyplot as p
import numpy as n
ngroup=4
passpercentage1=[77,100,89,96]
passpercentage2=[100,89,96,81]
subject=["OS","Java","CG","SE"]
p.xlabel=("subjects")
p.ylabel("Pass%")
p.title("Pass % of students")
index=n.arange(ngroup)
fig,ax=p.subplots()
p.bar(index,passpercentage1,width=0.3,color="blue",label="I BCA A")
p.bar(index,passpercentage2,width=0.3,color="green",label="I BCA B")
p.legend()
p.show()        
