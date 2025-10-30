from tkinter import*

window =Tk()

window.title("app Tk")

window.geometry("600x480")

def get_state():

    if male_var.get()==1:

        print("do silent mode")

    else:

        print("do regular mode")

male_var=IntVar()

Checkbutton(window,text="male",variable=male_var).pack()

Button(window,text="show state",command=get_state).pack()

window.mainloop()