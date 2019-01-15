import matplotlib.pyplot as p
value=[10,20,14,10]
c=['r','g','b','y']
l=['Sports','Co-curricular','Extra-curricular','Academic']
p.pie(value,labels=l,colors=c,startangle=90,shadow=True,explode=(0,0,0.1,0),radius=1.2,autopct="%1.1F%%")
p.legend()
p.show()        
