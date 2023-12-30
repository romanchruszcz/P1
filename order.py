from tkinter import *
from tkinter import ttk

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
    order_window.title("Straty-dodaj stratę")
    order_window.configure(background=general_bg_color)

    order_window.mainloop()