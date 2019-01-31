from tkinter import *
from tkinter import ttk

root=Tk()
root.title("tkinter window")
root.geometry("1000x300")
root.resizable(0,0)
title=Label(root,text="HELLO THERE!!!")
title.config(font=("",32))
title.pack()
button=Button(root,text="CLICK ME")
button.pack()
ent=Entry(root)
ent.pack()
var=StringVar()
rad1=Radiobutton(root,text="MALE",variable=var,value="MALE")
rad1.pack()
rad2=Radiobutton(root,text="FEMALE",variable=var,value="FEMALE")
rad2.pack()
degree=ttk.Combobox(root,state="readonly")
degree['value']=["BBA","BIT","BSC","BTEC","BE","BAC"]
degree.pack()
root.mainloop()