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
add_date_entry = funcs.add_date()
add_time_entry = funcs.add_time()
add_time_entry2 = funcs.add_time2()
def orders_window():
    
    order_window= Tk()
    
    w = 600
    h = 800
    x1 = order_window.winfo_screenwidth()                       # gathering of the screen width
    y1 = order_window.winfo_screenheight()                      # gathering of the screen height
    x2 = (x1/2)-(w/2)                                           # screen width/2 - order_window width/2
    y2 = (y1/2)-(h/2)                                           # screen height/2 - order_window height/2

    order_window.geometry('%dx%d+%d+%d' % (w, h, x2, y2))       # initial position of the window
    order_window.title("Rozpoczęcie / Zakończenie zlecenia")    # title of the window
    order_window.configure(background=general_bg_color)         # configuration of the background color

    general_frame = Frame(order_window,width=590,height=200,background=general_bg_color,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1)
    general_frame.place(x=5,y=5)

    left_frame = Frame(order_window,width=295,height=200,background=general_bg_color,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1)
    left_frame.place(x=5,y=210)



    label_in_Top = Label(general_frame, width = 37, height= 1, background=active_color,borderwidth=2,relief="solid",text="Informacje dot. zlecenia")  # basic informations
    label_in_Top.configure(font=font_mid)
    label_in_Top.place(x=10,y=10)

    date_label = Label(general_frame,text="Data:", font=font_small,background=general_bg_color)
    date_label.place(x=180,y=55)
    date_entry = Entry(general_frame,width=10,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    date_entry.place(x=240,y=55)
    date_entry.insert(0,add_date_entry)

    order_number_label = Label(general_frame, text="Numer zlecenia:",font=font_small,background=general_bg_color)
    order_number_label.place(x=80,y=90)
    order_numer_entry = Entry(general_frame,width=15,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    order_numer_entry.place(x=240,y=90)
    product_number_label = Label(general_frame, text="Numer produktu:",font=font_small,background=general_bg_color)
    product_number_label.place(x=70,y=125)
    product_numer_entry = Entry(general_frame,width=15,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    product_numer_entry.place(x=240,y=125)


    machine_speed_label = Label(general_frame, text="Prędkość maszyny:",font=font_small,background=general_bg_color)
    machine_speed_label.place(x=43,y=160)
    machine_speed_entry = Entry(general_frame,width=3,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    machine_speed_entry.place(x=240,y=160)








    label_on_Left = Label(left_frame, width = 22, height= 1, background=active_color,borderwidth=2,relief="solid",text="Rozpoczęcie zlecenia")  # basic informations
    label_on_Left.configure(font=font_small)
    label_on_Left.place(x=10,y=10)

    time_label = Label(left_frame,text="Godzina startu:", font=font_small,background=general_bg_color)
    time_label.place(x=60,y=50)
    time_entry = Entry(left_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    time_entry.place(x=215,y=50)
    time_entry.insert(0,add_time_entry[0])
    order_exp_quantity_label = Label(left_frame,text="Wielkość zlecenia:", font=font_small,background=general_bg_color)
    order_exp_quantity_label.place(x=30,y=90)
    order_exp_quantity_entry = Entry(left_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    order_exp_quantity_entry.place(x=215,y=90)

    changeover_start_label = Label(left_frame,text="Czas przezbrojenia:", font=font_small,background=general_bg_color)
    changeover_start_label.place(x=15,y=130)
    changeover_start_entry = Entry(left_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    changeover_start_entry.place(x=215,y=130)

    right_frame = Frame(order_window,width=290,height=200,background=general_bg_color,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1)
    right_frame.place(x=305,y=210)

    label_on_Right = Label(right_frame, width = 22, height= 1, background=active_color,borderwidth=2,relief="solid",text="Zakończenie zlecenia")  # basic informations
    label_on_Right.configure(font=font_small)
    label_on_Right.place(x=10,y=10)

    time_label = Label(right_frame,text="Godzina zakończenia:", font=font_small,background=general_bg_color)
    time_label.place(x=5,y=50)
    time_entry = Entry(right_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    time_entry.place(x=215,y=50)
    time_entry.insert(0,add_time_entry[1])    

    order_pro_quantity_label = Label(right_frame,text="Ilość wyprodukowana:", font=font_small,background=general_bg_color)
    order_pro_quantity_label.place(x=2,y=90)
    order_pro_quantity_entry = Entry(right_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    order_pro_quantity_entry.place(x=215,y=90)

    changeover_end_label = Label(right_frame,text="Czas przezbrojenia:", font=font_small,background=general_bg_color)
    changeover_end_label.place(x=27,y=130)
    changeover_end_entry = Entry(right_frame,width=5,font=font_small,highlightbackground=frame_color,highlightcolor=frame_color,highlightthickness=1,justify=RIGHT)
    changeover_end_entry.place(x=215,y=130)



    #, rodzaj przezbrojenia, ilosc czasu przezbrojenia,  zmiane predkosci maszyny
    # ilosci dobre, odpad, zakonczenie produkcji






    order_window.mainloop()