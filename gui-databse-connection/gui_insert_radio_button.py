from Tkinter import *
import ttk
import pymysql
def insert():
    dbconnect=pymysql.connect("localhost","root","ebs123","gui")
    cur=dbconnect.cursor()
    rno=int(tb1.get())
    name=tb2.get()
    select=gen.get()
    if select==1:
        genval="Male"
    elif select==2:
        genval="Female"
    cur.execute("insert into sample values('%d','%s', '%s')"%(rno,name,genval))
    dbconnect.commit()
    dbconnect.close()
root=Tk()
root.title("GuiEnvironment")
root.geometry("600x600")
app=Frame(root)
app.grid()
gen=IntVar()
tlabel=Label(root,text="Data base connection")
tlabel.grid(row=1,column=15)
tlabel1=Label(root,text="---------------------------------")
tlabel1.grid(row=2,column=15)
label1=Label(root,text="Rollno")
label1.grid(row=6,column=0)
tb1=Entry(root)
tb1.grid(row=6,column=5)
label2=Label(root,text="Name")
label2.grid(row=6,column=11)
tb2=Entry(root)
tb2.grid(row=6,column=13)
label3=Label(root,text="Gender")
label3.grid(row=10,column=0)
rb1=Radiobutton(root,text="Male",variable=gen,value=1)
rb1.grid(row=11,column=0)
rb2=Radiobutton(root,text="Feale",variable=gen,value=2)
rb2.grid(row=11,column=1)
button2=Button(root,text="submit",command=insert)
button2.grid(row=50,column=10)
button1=Button(root,text="End",command=root.destroy)
button1.grid(row=50,column=13)
root.mainloop()
