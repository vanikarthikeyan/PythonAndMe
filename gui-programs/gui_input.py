from Tkinter import *
import ttk
root=Tk()
root.title("GuiEnvironment")
root.geometry("500x500")
label1=Label(root,text="TextBox")
label1.pack()
tb1=Entry(root)
tb1.pack()
button1=Button(root,text="End",command=root.destroy)
button1.pack()
root.mainloop()
