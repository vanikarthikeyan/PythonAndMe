from Tkinter import *
import ttk
root=Tk()
root.title("GuiEnvironment")
root.geometry("500x500")
label1=Label(root,text="Day of the week")
label1.pack()
days=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
cb1=ttk.Combobox(root, values=days)
cb1.pack()
button1=Button(root,text="End",command=root.destroy)
button1.pack()
root.mainloop()
