from Tkinter import *
from tkFileDialog import askopenfilename
def NewFile():
    print "New File!"
def OpenFile():
    name=askopenfilename()
    print name
def About():
    print "This is a simple example of a menu"
root=Tk()
root.geometry("500x500")
m1=Menu(root)
root.config(menu=m1)
filemenu=Menu(m1)
m1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu=Menu(m1)
m1.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
mainloop()
