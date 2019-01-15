import matplotlib.pyplot as p
passpercentage1=[77.89,100,89,96]
subject=["OS","Java","CG","SE"]
p.xlabel=("subjects")
p.ylabel("Pass%")
p.title("Pass % of students")
p.bar(subject,passpercentage1,width=0.5,color=['red','green','yellow','blue'])
p.show()        
