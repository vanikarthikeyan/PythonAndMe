from Tkinter import Tk,Label,Button
root=Tk()
root.title("Demo for GUI")
root.geometry("500x300+150+150")
text1=Label(root,text="sample")
text1.pack()
button1=Button(root,text="Exit",command=root.destroy)
button1.pack()
root.mainloop()
