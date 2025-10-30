from tkinter import*
window =Tk()
window.title("app Tk")
window.geometry("600x480")

Label(window,text="hi word").pack()#نوشتن
Label(window,text="hi word",font="Tahoma").pack()#فونت
Label(window,text="hi word",font=("Tahoma",20)).pack()#سایز
Label(window,text="hi word",fg="white",bg="black").pack()#رنگ

window.mainloop()