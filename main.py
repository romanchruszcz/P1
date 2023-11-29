from tkinter import *
from tkinter import ttk 

general_bg_color = "#cdced1"
frame_color = "black"
active_color = "white"
font_big = ("Helvetica",26,"bold")
root = Tk()
root.geometry("1920x1080")
root.config(background=general_bg_color)
Frame_Top = Frame(root,width=1540,height=115,background=general_bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
Frame_Top.place(x=5,y=10)
Label_in_Top = Label(Frame_Top, width = 79, height= 1, background=active_color,borderwidth=2,relief="solid",text="DANE PODSTAWOWE")
Label_in_Top.configure(font=font_big)
Label_in_Top.place(x=10,y=10)




root.mainloop()