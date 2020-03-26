import tkinter

root = tkinter.Tk()
root.geometry('800x600')

canv = tkinter.Canvas(root, bg='white')

canv.pack(fill=tkinter.BOTH, expand=1)

black_color = tkinter.Button(height=50, width=50, text='Black')
red_color = tkinter.Button(height=50, width=50, text='Red')
green_color = tkinter.Button(height=50, width=50, text='Green')
blue_color = tkinter.Button(height=50, width=50, text='Blue')

color = 'Black'


def bl_colorista(event):
    global color
    color = 'Black'


def r_colorista(event):
    global color
    color = 'Red'


def g_colorista(event):
    global color
    color = 'Green'


def b_colorista(event):
    global color
    color = 'Blue'


black_color.bind('<Button-1>', bl_colorista)
red_color.bind('<Button-1>', r_colorista)
green_color.bind('<Button-1>', g_colorista)
blue_color.bind('<Button-1>', b_colorista)


def painer(event):
    global x, y
    x = event.x
    y = event.y
    canv.create_oval(x+10, y+10, x-10, y-10, fill=color, width=0)

canv.bind('<Button-1>', painer)



root.mainloop()