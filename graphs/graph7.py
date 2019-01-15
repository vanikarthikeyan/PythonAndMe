import matplotlib.pyplot as p
passpercentage1=[77.89,100,89,96]
subject=["OS","Java","CG","SE"]
p.xlabel=("subjects")
p.ylabel("Pass%")
p.title("Pass % of students")
p.scatter(subject,passpercentage1,label="stars",color="blue",marker="v",s=30)
p.show()        
