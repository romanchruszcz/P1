from tkinter import *
from tkinter import ttk 

general_bg_color = "#cdced1"
frame_color = "black"
active_color = "white"
font_big = ("Helvetica",24,"bold")
font_mid = ("Helvetica", 18,"bold")
root = Tk()
root.geometry("1920x1080")
root.config(background=general_bg_color)
Frame_Top = Frame(root,width=1540,height=115,background=general_bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
Frame_Top.place(x=5,y=10)
Label_in_Top = Label(Frame_Top, width = 79, height= 1, background=active_color,borderwidth=2,relief="solid",text="DANE PODSTAWOWE")
Label_in_Top.configure(font=font_big)
Label_in_Top.place(x=10,y=10)
Date_Label_A = Label(Frame_Top,text="Data:",background=general_bg_color)
Date_Label_A.configure(font=font_mid)
Date_Label_A.place(x=10,y=70)
Date_Label_B= Label(Frame_Top,text="2023-11-29",background=general_bg_color)
Date_Label_B.configure(font=font_mid)
Date_Label_B.place(x=80,y=70)



root.mainloop()