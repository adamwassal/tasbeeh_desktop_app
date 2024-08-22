from tkinter import *


win = Tk()
win.title("Tasbeeh")
win.geometry("300x300")

c = 0


def plus():
    global c
    c += 1
    count.config(text=c)


def minus():
    global c
    if c > 0:
        c -= 1
        count.config(text=c)


def clear():
    global c
    c = 0
    count.config(text=c)


count = Label(win, text=c, font=("Times 25"))
count.pack(pady=10)

btn_plus = Button(
    win,
    text="+",
    font=("Times 16"),
    bg="red",
    fg="white",
    cursor="hand2",
    command=lambda: plus(),
)
btn_plus.pack()

btn_minus = Button(
    win,
    text="-",
    font=("Times 16"),
    bg="red",
    fg="white",
    cursor="hand2",
    command=lambda: minus(),
)
btn_minus.pack(pady=10)

btn_clear = Button(
    win,
    text="clear",
    font=("Times 16"),
    bg="red",
    fg="white",
    cursor="hand2",
    command=lambda: clear(),
)
btn_clear.pack(pady=10)
win.mainloop()
