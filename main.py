from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Canberra Weekly Weather")
root.configure(bg="light blue")
width = 1000
height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


TableMargin = Frame(height=500, width=500)
TableMargin.pack(side=TOP)
tree = ttk.Treeview(TableMargin, columns=("Date", "Temp", "Weather", "Rain"), height=300, selectmode="extended")
tree.heading('Date', text="Date", anchor=W)
tree.heading('Temp', text="Temp", anchor=W)
tree.heading('Weather', text="Weather", anchor=W)
tree.heading("Rain", text="Rain", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=200)
tree.column('#4', stretch=NO, minwidth=0, width=200)
tree.pack()

with open('data.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        date = row['date']
        temp = row['temp']
        weather = row['weather']
        rain = row['rain']
        tree.insert("", 7, values=(date, temp, weather, rain))

#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()