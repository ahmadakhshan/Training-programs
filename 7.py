from tkinter import*

window =Tk()

window.title("app Tk")

window.geometry("600x480")

def sing():

    sing_in.config(text="welcom ms/mr {} {}".format(first_name.get(),last_name.get()))

Label(window,text="first name").pack()

first_name=Entry(window)

first_name.pack()

Label(window,text="last name").pack()

last_name=Entry(window)

last_name.pack()

Button(window,text="sing in",command=sing).pack()

sing_in=Label(window,text="")

sing_in.pack()

window.mainloop()