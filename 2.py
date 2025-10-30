from tkinter import*#اضافه کردن کتابخانه all=*
window =Tk()#اضافه کردن پنجره
window.title("app Tk")#تغیر تیتر
window.minsize(300,300)#حداقل اندازه 
window.maxsize(700,700)#نهایت اندازه
window.geometry("600x480")#اندازه اولیه
window.resizable(width=False,height=True)#فیکس کردن اندازه
window.mainloop()#باز کردن و تغییر دادن به پنجره باید در آخر کد ها باشد 