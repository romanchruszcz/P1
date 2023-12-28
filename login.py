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

def login_window():
    new_window = Tk()
    w = 400
    h = 200

    x1 = new_window.winfo_screenwidth()
    y1 = new_window.winfo_screenheight()

    x2 = (x1/2)-(w/2)
    y2 = (y1/2)-(h/2)

    new_window.geometry('%dx%d+%d+%d' % (w, h, x2, y2))
    new_window.title("Log in")
    new_window.configure(background=general_bg_color)
    login_label = Label(new_window,width=15,text="Login:",background=general_bg_color,font=font_small)
    login_label.place(x=50, y=50)
    password_label = Label(new_window,width=15,text="Password:",background=general_bg_color,font=font_small)
    password_label.place(x=30, y=100)
    login_entry = Entry(new_window,width=15,background=active_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color,font=font_small)
    login_entry.place(x=200,y=50)
    password_entry = Entry(new_window,width=15,background=active_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color,font=font_small,show="*")
    password_entry.place(x=200,y=100)

    login_entry.focus()

    OK_button=Button(new_window,width=15,text="Zaloguj",pady=5)
    OK_button.place(x=80,y=150)
    NOT_OK_button=Button(new_window,width=15,text="Anuluj",pady=5,command=new_window.destroy)
    NOT_OK_button.place(x=220,y=150)
    new_window.mainloop()
