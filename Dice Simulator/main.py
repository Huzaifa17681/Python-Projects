from tkinter import *
import random

root = Tk()

#fuction
def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    r = random.choice(dice)
    result.config(text=f'{r}')

#config
root.geometry('300x300')
root.resizable('False', 'False')
root.title('Roll The Dice; By Huzaifa')
root.config(bg='lightblue')

#label
result = Label(root,font=('Calibri',100),bg="lightblue",fg="white")
result.pack()

#button
btn1 = Button(text='Roll The Dice!',bd=1,width=20,height=1,fg="red",bg="lightblue",font=("Calibri",13),command=roll)
btn1.place(x=61,y=190)

root.mainloop()
