import numpy as n
import matplotlib.pyplot as p
 
# data to plot
n_groups = 4
bca_a= (90,85, 92, 78)
bca_b = (100, 92, 54,65)
 
# create plot
fig, ax = p.subplots()
index = n.arange(n_groups)

 
p.bar(index,bca_a ,width=0.2,color='b', label='BCA A')
 
p.bar(index +0.2, bca_b, width=0.2,color='g',label='BCA B')
 
p.xlabel('Subject')
p.ylabel('pass%')
p.title('pass % by each calss')
p.xticks(index + 0.2, ('OS', 'Java', 'GC', 'Accounts'))
p.legend()
 
p.tight_layout()
p.show()
