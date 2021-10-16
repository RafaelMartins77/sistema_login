from tkinter import *

# sistema de login

window = Tk()
window.title('faça seu login')
window.geometry('400x150')

# mensagem e entrada de texto

user = Label(window, text='User:')
password = Label(window, text='password:')
user.place(x=10, y=10)
password.place(x=10, y=40)

userin = Entry(window)
passwordin = Entry(window)
userin.place(x=80, y=10, width='250', height='20')
passwordin.place(x=80, y=40, width='250', height='20')

# botôes

login = Button(window, text='Login')
signup = Button(window, text='save')
login.place(x=280, y=100, width='40', height='20')
signup.place(x=330, y=100, width='40', height='20')




window.mainloop()
