from tkinter import *
from tkinter import ttk
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

    w = 500
    h = 445

    x1 = loss_window.winfo_screenwidth()
    y1 = loss_window.winfo_screenheight()

    x2 = (x1/2)-(w/2)
    y2 = (y1/2)-(h/2)

    loss_window.geometry('%dx%d+%d+%d' % (w, h, x2, y2))
    loss_window.title("Straty-dodaj stratę")
    loss_window.configure(background=general_bg_color)

    category_frame=Frame(loss_window,width=490,height=100,highlightthickness=1,background=general_bg_color,highlightcolor=frame_color,highlightbackground=frame_color)
    category_frame.place(x=5, y=5)
    cat_value = IntVar()
    categories = ["Człowiek","Maszyna","Metoda","Materiał","Środowisko","Miara"]
    Cat1 = Radiobutton(category_frame,text=categories[0],variable=cat_value,value =1,font=font_small,background=general_bg_color)
    Cat1.place(x=5,y=5)
    Cat2 = Radiobutton(category_frame,text=categories[1],variable=cat_value,value =2,font=font_small,background=general_bg_color)
    Cat2.place(x=205,y=5)
    Cat3 = Radiobutton(category_frame,text=categories[2],variable=cat_value,value =3,font=font_small,background=general_bg_color)
    Cat3.place(x=380,y=5)
    Cat4 = Radiobutton(category_frame,text=categories[3],variable=cat_value,value =4,font=font_small,background=general_bg_color)
    Cat4.place(x=5,y=55)
    Cat5 = Radiobutton(category_frame,text=categories[4],variable=cat_value,value =5,font=font_small,background=general_bg_color)
    Cat5.place(x=205,y=55)
    Cat6 = Radiobutton(category_frame,text=categories[5],variable=cat_value,value =6,font=font_small,background=general_bg_color)
    Cat6.place(x=380,y=55)
    loss_reasons = ttk.Treeview(loss_window,columns="Przyczyna",show="headings",height=15)
    loss_reasons.heading("Przyczyna", text="Przyczyna")
    loss_reasons.column("Przyczyna",minwidth=0,width=250,stretch=NO,anchor=CENTER)
    loss_reasons.place(x=5,y=110)

    minutes_entry = Entry(loss_window, width=5,justify=RIGHT,background=active_color,highlightcolor=frame_color,highlightthickness=1,highlightbackground=frame_color,font=font_big)
    minutes_entry.place(x = 330, y= 140)
    add_loss_button_to_main = Button(loss_window, width = 15,height=2,text = "Dodaj stratę",background=starting_color,font=font_small)
    add_loss_button_to_main.place(x = 285, y= 260)
    close_loss_window = Button(loss_window, width = 15,text = "Zamknij",background=ending_color,font=font_small)
    close_loss_window.place(x = 285, y= 370)
    loss_window.mainloop()
