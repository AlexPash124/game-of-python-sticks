from random import *
from tkinter import *
from tkinter import messagebox

pal = 20


def start():
    global pal
    pal = randint(15, 25)
    palichki.config(text=pal * '|')


def btnOne():
    global pal
    pal = pal - 1
    palichki.config(text=pal * '|')
    if pal <= 0:
        messagebox.showinfo('Результат', 'Ви програли!!!')
        start()
    btn1['state'] = 'disabled'
    btn2['state'] = 'disabled'
    btn3['state'] = 'disabled'
    btnComp['state'] = 'active'


def btnTwo():
    global pal
    pal = pal - 2
    palichki.config(text=pal * '|')
    if pal <= 0:
        messagebox.showinfo('Результат', 'Ви програли!!!')
        start()
    btn1['state'] = 'disabled'
    btn2['state'] = 'disabled'
    btn3['state'] = 'disabled'
    btnComp['state'] = 'active'


def btnThree():
    global pal
    pal = pal - 3
    palichki.config(text=pal * '|')
    if pal <= 0:
        messagebox.showinfo('Результат', 'Ви програли!!!')
        start()
    btn1['state'] = 'disabled'
    btn2['state'] = 'disabled'
    btn3['state'] = 'disabled'
    btnComp['state'] = 'active'


def btnCompFun():
    global pal
    comp = randint(1, 3)
    if pal == 3:
        pal = pal - 2
    elif pal == 2:
        pal = pal - 1
    else:
        pal = pal - comp
    palichki.config(text=pal * '|')
    if pal <= 0:
        messagebox.showinfo('Результат', 'Ви виграли!!!')
        start()
    btnComp['state'] = 'disabled'
    btn1['state'] = 'active'
    btn2['state'] = 'active'
    btn3['state'] = 'active'


window = Tk()
window.title("Палички")
window.geometry('600x600')
window.resizable(False, False)
window.config(bg='#123')

palichki = Label(window, text="|",
                 font=('Arial', 60, 'bold'), bg='#123', fg='yellow')
palichki.place(x=50, y=50)
btn1 = Button(window, command=btnOne, text='1', font=('Arial', 30, 'bold'), bg='#123', fg='yellow')
btn1.place(x=50, y=400)
btn2 = Button(window, text='2', command=btnTwo, font=('Arial', 30, 'bold'), bg='#123', fg='yellow')
btn2.place(x=150, y=400)
btn3 = Button(window, text='3', command=btnThree, font=('Arial', 30, 'bold'), bg='#123', fg='yellow')
btn3.place(x=250, y=400)

btnComp = Button(window, command=btnCompFun, text='Хід компа', font=('Arial', 30, 'bold'),
                 bg='#123', fg='yellow')
btnComp.place(x=350, y=400)

start()
window.mainloop()
