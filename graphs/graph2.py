import matplotlib.pyplot as p
passpercentage1=[77.89,100,89,96]
passpercentage2=[80,98,92.5,96]
subject=["OS","Java","CG","SE"]
p.xlabel=("subjects")
p.ylabel("Pass%")
p.title("Pass % of students")
p.plot(subject,passpercentage1,label="I BCA A")
p.plot(subject,passpercentage2,label="I BCA B")
p.legend()
p.show()        
