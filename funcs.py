from tkinter import *
import datetime

changeover_type_list = ["Krótkie","Średnie","Długie"]

def add_date():
    date_now = datetime.datetime.now()
    date_converted = date_now.strftime("%Y-%m-%d")
    return date_converted
def add_time():
    date_now = datetime.datetime.now()
    time_converted = date_now.strftime("%H:%M")
    return time_converted, ""
def add_time2():
    date_now = datetime.datetime.now()
    time_converted2 = date_now.strftime("%H:%M")
    return time_converted2