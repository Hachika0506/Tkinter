from tkinter import *
from tkinter import messagebox

from Lib.logging import info
from PIL import Image, ImageTk
window = Tk()
window.title('My Photo Album')
window.geometry('400x420')

title = Label(window, text='My Photo Album')
title.pack(pady=10)
log_file = Image.open('img.jfif')
log_file = log_file.resize((300,100))
photo = ImageTk.PhotoImage(log_file)
plc = Label(window, Image=photo)
plc.pack(pady=5)

def show_message():
messagebox.showinfo('Great','You clicked the photo')
msg_btn = Button(window, text='click to Reset', bg='blue', fg='white', command=show_message)
msg_btn.pack(pady=5)

def show_details():
top = Toplevel()
top.title('photo details')
top.geometry('200x120')
info.pack(pady=10)
place = Label(top, text='Location my Garden')
place.pack()
top.mainloop()
details_btn = Button(window, text='See Details', fg='white',command=show_details)
details_btn.pack(pady=5)

window.mainloop()