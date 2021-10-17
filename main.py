from tkinter import *
import structure as st

# sistema de login

window = Tk()
window.title('faça seu login')
window.geometry('400x150')
window.resizable(False, False)
window.configure(background='#191970')


# mensagem e entrada de texto

user = Label(window, text='User:', background='#191970', foreground='#fff')
password = Label(window, text='password:', background='#191970', foreground='#fff')
status = Label(window, text='não logado', background='#F0E68C', relief='ridge')
user.place(x=10, y=10)
password.place(x=10, y=40)
status.place(x=20, y=100)

vsenha = StringVar
userin = Entry(window)
passwordin = Entry(window, textvariable=vsenha, show='#')
userin.place(x=80, y=10, width='250', height='20')
passwordin.place(x=80, y=40, width='250', height='20')

# botôes

login = Button(window, text='Login', command=lambda: st.login(userin, passwordin, status))
signup = Button(window, text='save', command=lambda: st.save(userin.get(), passwordin.get()))
logout = Button(window, text='logout', command=lambda: st.sair(status))
login.place(x=280, y=100, width='40', height='20')
signup.place(x=330, y=100, width='40', height='20')
logout.place(x=230, y=100, width='40', height='20')

window.mainloop()
