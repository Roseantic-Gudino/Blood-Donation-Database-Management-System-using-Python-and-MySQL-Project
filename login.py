from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields can not be empty')
    elif usernameEntry.get()=='BD04' and passwordEntry.get()=='bd04':
        messagebox.showinfo('Login Successful','Welcome ')
        window.destroy()
        import final

    else:
        messagebox.showerror('Error','Please enter correct details')

window=Tk()
window.resizable(False,False)
window.title('Login Page')

window.geometry('1100x619+50+50')

bgImage=ImageTk.PhotoImage(file='bg login page.jpg')
bgLabel=Label(window,image=bgImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,width=100,height=100,bg='gray89')
loginFrame.pack(pady=20)
loginFrame.place(x=280,y=120)

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage, text='Username',compound=LEFT , font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0,pady=10, padx=20)

usernameEntry=Entry(loginFrame, font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10, padx=20)

passwordImage=PhotoImage(file='padlock.png')
passwordLabel=Label(loginFrame,image=passwordImage, text='Password',compound=LEFT , font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=10, padx=20)

passwordEntry=Entry(loginFrame, font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10, padx=20)

loginButton=Button(loginFrame,text='Login', font=('times new roman',14,'bold'), width=15, fg='white', bg='cornflowerblue', activebackground='cornflowerblue', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3,column=1, pady=10,)

window.mainloop()