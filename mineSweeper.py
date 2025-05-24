from tkinter import *
from cell import Cell
import settings
import util



root = Tk()
root.configure(bg="black")
#Window divide



root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Mine Sweeper')
root.resizable(False, False)

scoreFrame = Frame(
    root,
    bg ='black',
    width = settings.WIDTH,
    height = util.hpercent(15)

)
scoreFrame.place(x = 0, y=0)

deetsFrame = Frame(
    root,
    bg ='black',
    width = util.wpercent(10),
    height = util.hpercent(85)
)

deetsFrame.place(x=0, y=util.hpercent(15))

center = Frame(
    root,
    bg ='white',
    width = util.wpercent(90),
    height = util.hpercent(85)
)

center.place(x=util.wpercent(10), y=util.hpercent(15))

btn1 = Button(
    center,
    bg = 'blue',
    text = 'START'
)

btn1.place(x=util.wpercent(40), y=util.hpercent(35))

c1 = Cell

#run
root.mainloop()
