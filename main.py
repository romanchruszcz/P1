from tkinter import *
from tkinter import ttk 

bg_color = "darkgrey"
frame_color = "black"
root = Tk()
root.geometry("1920x1080")
root.config(background=bg_color)
Frame_Top = Frame(root,width=1540,height=115,background=bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
Frame_Top.place(x=5,y=10)    
root.mainloop()