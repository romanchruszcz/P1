from tkinter import *
from tkinter import ttk
import funcs
# settings for fonts and colors for backgrounds
general_bg_color = "#cdced1"    # light grey
frame_color = "#000000"         # black
active_color = "#ffffff"        # white
login_color = "#1a1aff"         # blue
ending_color = "#ff3300"        # red
starting_color = "#00ff55"      # green
losses_color = "#ffff1a"        # yellow
font_big = ("Helvetica",24,"bold")
font_mid = ("Helvetica", 18,"bold")
font_small = ("Helvetica", 14,"bold")


def orders_window():
    order_window= Tk()

    w = 1200
    h = 800
    x1 = order_window.winfo_screenwidth()
    y1 = order_window.winfo_screenheight()
    x2 = (x1/2)-(w/2)
    y2 = (y1/2)-(h/2)

    order_window.geometry('%dx%d+%d+%d' % (w, h, x2, y2))
    order_window.title("Rozpoczęcie / Zakończenie zlecenia")
    order_window.configure(background=general_bg_color)

    general_frame = Frame(order_window,width=1190,height=300,background=general_bg_color,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1)
    general_frame.place(x=5,y=5)

    label_in_Top = Label(general_frame, width = 61, height= 1, background=active_color,borderwidth=2,relief="solid",text="Rozpoczęcie zlecenia")  # basic informations
    label_in_Top.configure(font=font_big)
    label_in_Top.place(x=10,y=10)

    date_label = Label(general_frame,text="Data:", font=font_small,background=general_bg_color)
    date_label.place(x=10,y=65)
    date_entry = Entry(general_frame,width=10,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    date_entry.place(x=80,y=65)
    date_entry.insert(0,funcs.date_converted)

    time_label = Label(general_frame,text="Godzina startu:", font=font_small,background=general_bg_color)
    time_label.place(x=210,y=65)
    time_entry = Entry(general_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    time_entry.place(x=370,y=65)
    time_entry.insert(0,funcs.time_converted)

    order_window.mainloop()