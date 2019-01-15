from Tkinter import *
import ttk
root=Tk()
root.title("GuiEnvironment")
root.geometry("500x500")
label1=Label(root,text="Gender")
label1.pack()
rb1=ttk.Radiobutton(root,text="Male",value=1)
rb1.pack()
rb2=ttk.Radiobutton(root,text="Female",value=2)
rb2.pack()
button1=Button(root,text="End",command=root.destroy)
button1.pack()
root.mainloop()
