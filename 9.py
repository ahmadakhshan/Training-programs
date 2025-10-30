from tkinter import*
window =Tk()
window.title("app Tk")
window.geometry("600x480")

s=""

def enter():
    global ent
    ent.set(s)


ent=StringVar()
entry=Entry(window,textvariable=ent)
entry.pack()

b=Button(window,text="click me",command=enter)
b.pack()
window.mainloop()