import matplotlib.pyplot as p
  
p.style.use('fivethirtyeight') 
fig = p.figure() 
  
p1 = fig.add_subplot(221) 
p2 = fig.add_subplot(222) 
p3 = fig.add_subplot(223) 
p4 = fig.add_subplot(224) 

x=['OS','Java','CG','Accounts']
y=[98,88,82,81]
p1.bar(x, y, color =('r','g','b','y'),width=0.2) 
p1.set_title('Result 2014') 
  
x=['OS','Java','CG','Accounts']
y=[81,100,92,88]
p2.bar(x,y,color =('r','g','b','y'),width=0.2) 
p2.set_title('Result 2015') 

x=['OS','Java','CG','Accounts']
y=[100,98,84,87]
p3.bar(x, y, color =('r','g','b','y'),width=0.2) 
p3.set_title('Result 2016') 

x=['OS','Java','CG','Accounts']
y=[100,81,100,99]
p4.bar(x, y, color =('r','g','b','y'),width=0.2) 
p4.set_title('Result 2017') 
# adjusting space between subplots 
fig.subplots_adjust(hspace=.5,wspace=0.5) 
  
# function to show the plot 
p.show()

