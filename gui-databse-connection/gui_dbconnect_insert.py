from Tkinter import *
import ttk
import pymysql
def insert():
    dbconnect=pymysql.connect("localhost","root",
"ebs123","gui")
    cur=dbconnect.cursor()
    rno=int(tb1.get())
    name=tb2.get()
    cur.execute("insert into sample(rollno,name) values('%d','%s')"%(rno,name))
    dbconnect.commit()
    dbconnect.close()
root=Tk()
root.title("GuiEnvironment")
root.geometry("500x500")
label1=Label(root,text="Rollno")
label1.pack()
tb1=Entry(root)
tb1.pack()
label2=Label(root,text="Name")
label2.pack()
tb2=Entry(root)
tb2.pack()
button2=Button(root,text="submit",command=insert)
button2.pack()
button1=Button(root,text="End",command=root.destroy)
button1.pack()
root.mainloop()
