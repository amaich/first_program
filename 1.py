from tkinter import *
from random import randrange as rnd, choice
import time

score = 0

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']


def new_ball():
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
    root.after(1000, new_ball)


def click(event):
    global score
    cub = (((event.x - x) ** 2) + ((event.y - y) ** 2)) ** 0.5
    if cub <= r:
        score += 1
        canv.create_text(800, 600, text=score,
                         anchor=SE, font="Times 14")
        print(score)


new_ball()
canv.bind('<Button-1>', click)
mainloop()