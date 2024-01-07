from tkinter import *
import datetime
add_date_and_time():
    date_now = datetime.datetime.now()
    date_converted = date_now.strftime("%Y-%m-%d")
    time_converted = date_now.strftime("%H:%M")
add_date_and_time2():
    date_now = datetime.datetime.now()
    time_converted2 = date_now.strftime("%H:%M")
print(time_converted)