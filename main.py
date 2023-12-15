from tkinter import *
from tkinter import ttk 

# settings for fonts and colors for backgrounds
general_bg_color = "#cdced1"
frame_color = "black"
active_color = "white"
font_big = ("Helvetica",24,"bold")
font_mid = ("Helvetica", 18,"bold")
font_small = ("Helvetica", 14,"bold")
login_color = "Blue"
ending_color = "red"
starting_color = "green"
losses_color = "yellow"

root = Tk()
root.geometry("1920x1080")
root.config(background=general_bg_color)
root.resizable(0,0)
frame_Top = Frame(root,width=1500,height=115,background=general_bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
frame_Top.place(x=5,y=10)
label_in_Top = Label(frame_Top, width = 77, height= 1, background=active_color,borderwidth=2,relief="solid",text="DANE PODSTAWOWE")  # basic informations
label_in_Top.configure(font=font_big)
label_in_Top.place(x=10,y=10)
date_label_A = Label(frame_Top,text="Data:",background=general_bg_color)
date_label_A.configure(font=font_mid)
date_label_A.place(x=10,y=70)
date_label_B= Label(frame_Top,text="2023-11-29",background=general_bg_color)
date_label_B.configure(font=font_mid)
date_label_B.place(x=80,y=70)
shift_label = Label(frame_Top,text="Zmiana:",background=general_bg_color)
shift_label.configure(font=font_mid)
shift_label.place(x=250,y=70)
shift_list = ttk.Combobox(frame_Top,values=[1,2,3],width=5)
shift_list.current(0)
shift_list.configure(font=font_mid)
shift_list.place(x=360,y=70)

work_time_label = Label(frame_Top,text="Czas pracy:",background=general_bg_color)
work_time_label.configure(font=font_mid)
work_time_label.place(x=490,y=70)
work_time_list = ttk.Combobox(frame_Top,values=[480,600,60,120,180,340,400,540],width=5)     # how long time production will work  choice done by user
work_time_list.current(0)
work_time_list.configure(font=font_mid)
work_time_list.place(x=650,y=70)

break_time_label_A = Label(frame_Top,text="Czas przerwy:",background=general_bg_color)
break_time_label_A.configure(font=font_mid)
break_time_label_A.place(x=770,y=70)

break_time_label_B = Label(frame_Top,text="20",background=general_bg_color)
break_time_label_B.configure(font=font_mid)
break_time_label_B.place(x=950,y=70)

user_label_A = Label(frame_Top,text="Użytkownik:",background=general_bg_color)
user_label_A.configure(font=font_mid)
user_label_A.place(x=1020,y=70)

user_label_B = Label(frame_Top,text="SUPERUSER",background=general_bg_color)
user_label_B.configure(font=font_mid,foreground="BLUE")
user_label_B.place(x=1180,y=70)


frame_Mid = Frame(root,width=1500,height=150,background=general_bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
frame_Mid.place(x=5,y=135)





label_in_Mid = Label(frame_Mid, width = 77, height= 1, background=active_color,borderwidth=2,relief="solid",text="AKTUALNE ZLECENIE",foreground="green")
label_in_Mid.configure(font=font_big)
label_in_Mid.place(x=10,y=10)


current_order_columns = ('Nr zlecenia',
                         'Nr produktu',
                         'Przezbrojenie rozp.',
                         'Typ przezb.',
                         'Przezbrojenie zakoń.',
                         'Suma strat',
                         'Ilość wyprodukowana',
                         'Godz. rozpoczęcia',
                         'Godz. zakończenia',
                         'Czas pracy',
                         'Cel',
                         'Wynik OEE')
current_order_treeview = ttk.Treeview(frame_Mid,columns=current_order_columns,show="headings",height=2)
current_order_treeview.heading('Nr zlecenia', text='Nr zlecenia')
current_order_treeview.column('Nr zlecenia',minwidth=0,width=100,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Nr produktu', text='Nr produktu')
current_order_treeview.column('Nr produktu', minwidth=0,width=220,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Przezbrojenie rozp.', text='Przezbrojenie rozp.') 
current_order_treeview.column('Przezbrojenie rozp.',  minwidth=0,width=112,stretch=NO,anchor=CENTER)


current_order_treeview.heading('Typ przezb.', text='Typ przezb.')
current_order_treeview.column('Typ przezb.', minwidth=0,width=90,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Przezbrojenie zakoń.', text='Przezbrojenie zakoń.')
current_order_treeview.column('Przezbrojenie zakoń.', minwidth=0,width=114,stretch=NO,anchor=CENTER)


current_order_treeview.heading('Suma strat', text='Suma strat')
current_order_treeview.column('Suma strat', minwidth=0,width=100,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Ilość wyprodukowana', text='Ilość wyprodukowana')
current_order_treeview.column('Ilość wyprodukowana', minwidth=0,width=130,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Godz. rozpoczęcia', text='Godz. rozpoczęcia')
current_order_treeview.column('Godz. rozpoczęcia', minwidth=0,width=130,stretch=NO,anchor=CENTER)


current_order_treeview.heading('Godz. zakończenia', text='Godz. zakończenia')
current_order_treeview.column('Godz. zakończenia', minwidth=0,width=130,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Czas pracy', text='Czas pracy')
current_order_treeview.column('Czas pracy', minwidth=0,width=100,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Cel', text='Cel')
current_order_treeview.column('Cel', minwidth=0,width=120,stretch=NO,anchor=CENTER)

current_order_treeview.heading('Wynik OEE', text='Wynik OEE')
current_order_treeview.column('Wynik OEE',minwidth=0,width=120,stretch=NO,anchor=CENTER)
current_order_treeview.place(x=10,y=70)

order_start_button = Button(root,width=25,text="Rozpoczęcie zlecenia",font=font_small,background=starting_color)
order_start_button.place(x=10,y=300) 
order_start_button = Button(root,width=25,text="Zakończenie zlecenia",font=font_small,background=ending_color)
order_start_button.place(x=1190,y=300) 

frame_Bottom = Frame(root,width=1500,height=570,background=general_bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
frame_Bottom.place(x=5,y=355)

label_in_Bottom = Label(frame_Bottom, width = 77, height= 1, background=active_color,borderwidth=2,relief="solid",text="LISTA ZLECEŃ ZAKOŃCZONYCH",foreground="BLUE")
label_in_Bottom.configure(font=font_big)
label_in_Bottom.place(x=10,y=10)

current_order_columns = ('Nr zlecenia',
                         'Nr produktu',
                         'Przezbrojenie rozp.',
                         'Typ przezb.',
                         'Przezbrojenie zakoń.',
                         'Suma strat',
                         'Ilość wyprodukowana',
                         'Godz. rozpoczęcia',
                         'Godz. zakończenia',
                         'Czas pracy',
                         'Cel',
                         'Wynik OEE')
finished_order_treeview = ttk.Treeview(frame_Bottom,columns=current_order_columns,show="headings",height=22)
finished_order_treeview.heading('Nr zlecenia', text='Nr zlecenia')
finished_order_treeview.column('Nr zlecenia',minwidth=0,width=100,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Nr produktu', text='Nr produktu')
finished_order_treeview.column('Nr produktu', minwidth=0,width=220,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Przezbrojenie rozp.', text='Przezbrojenie rozp.') 
finished_order_treeview.column('Przezbrojenie rozp.',  minwidth=0,width=112,stretch=NO,anchor=CENTER)


finished_order_treeview.heading('Typ przezb.', text='Typ przezb.')
finished_order_treeview.column('Typ przezb.', minwidth=0,width=90,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Przezbrojenie zakoń.', text='Przezbrojenie zakoń.')
finished_order_treeview.column('Przezbrojenie zakoń.', minwidth=0,width=114,stretch=NO,anchor=CENTER)


finished_order_treeview.heading('Suma strat', text='Suma strat')
finished_order_treeview.column('Suma strat', minwidth=0,width=100,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Ilość wyprodukowana', text='Ilość wyprodukowana')
finished_order_treeview.column('Ilość wyprodukowana', minwidth=0,width=130,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Godz. rozpoczęcia', text='Godz. rozpoczęcia')
finished_order_treeview.column('Godz. rozpoczęcia', minwidth=0,width=130,stretch=NO,anchor=CENTER)


finished_order_treeview.heading('Godz. zakończenia', text='Godz. zakończenia')
finished_order_treeview.column('Godz. zakończenia', minwidth=0,width=130,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Czas pracy', text='Czas pracy')
finished_order_treeview.column('Czas pracy', minwidth=0,width=100,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Cel', text='Cel')
finished_order_treeview.column('Cel', minwidth=0,width=120,stretch=NO,anchor=CENTER)

finished_order_treeview.heading('Wynik OEE', text='Wynik OEE')
finished_order_treeview.column('Wynik OEE',minwidth=0,width=120,stretch=NO,anchor=CENTER)
finished_order_treeview.place(x=10,y=70)

login_button = Button(root,width=20,background=login_color,text="LOGOWANIE",foreground=active_color,font=font_small,pady=5)
login_button.place(x=1510,y=10)

clear_button = Button(root,width=18,background=ending_color,text="CZYSZCZENIE",foreground=losses_color,height=1,pady=11)
clear_button.place(x=1770,y=10)

add_losses = Button(root,width=20,background=losses_color,text="DODAJ STRATY",font=font_small,pady=5)
add_losses.place(x=1510,y=78)

remove_loss_button = Button(root,width=18,background=ending_color,text="USUŃ STRATĘ",foreground=losses_color,height=1,pady=11)
remove_loss_button.place(x=1770,y=78)


frame_Right = Frame(root,width=405,height=790,background=general_bg_color,highlightthickness=1,highlightbackground=frame_color,highlightcolor=frame_color)
frame_Right.place(x=1510,y=135)

#mylist=(434343,3434343434,22,2255,2424,2424)
#finished_order_treeview.insert('',END,values=mylist)































root.mainloop()