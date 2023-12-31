from tkinter import *
import datetime

date_now = datetime.datetime.now()
date_converted = date_now.strftime("%Y-%m-%d")
time_converted = date_now.strftime("%H:%M")
print(time_converted)