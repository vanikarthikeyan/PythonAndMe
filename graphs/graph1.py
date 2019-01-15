import matplotlib.pyplot as p
passpercentage=[77.89,100,89,96]
subject=["OS","Java","CG","SE"]
p.xlabel=("subjects")
p.ylabel("Pass%")
p.title("Pass % of students")
p.plot(subject,passpercentage)
p.show()        
