from Tkinter import *
root=Tk()
root.title("GUI Environment")
root.geometry("500x500")
label1=Label(root,text="List box")
label1.pack()
lb1=Listbox(root, width=20,selectmode='multiple')
lb1.pack()
departments=('CSE','ECE','Mechanical','IT','CIVIL','EEE')
for i in departments:
    lb1.insert(lb1.size(),i)
button1=Button(root,text="End",command=root.destroy)
button1.pack()
root.mainloop()
