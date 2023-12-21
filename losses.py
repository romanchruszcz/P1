from tkinter import *

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

def losses_window():
    loss_window= Tk()
    loss_window.geometry("1000x1000")
    loss_window.title("Straty")
    loss_window.configure(background=general_bg_color)

    loss_window.mainloop()
