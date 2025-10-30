from tkinter import*

window =Tk()

window.title("app Tk")

window.geometry("600x480")

counter=0

def count():

    global counter #اجرای عمل بر متغیر در دف

    counter+=1

    count_.config(text="count:{}".format(counter))#confingتغیر در لیبل

count_=Label(window,text="count")

count_.pack()

Button(window,text="click me",command=count).pack()

window.mainloop()