import psycopg2
from tkinter import *
import tkinter as tk

def insert_data(name, age, address):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', port='5432')
    cursor = conn.cursor()

    query = '''INSERT INTO student (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);'''
    cursor.execute(query, (name, age, address))

    print('Inserted.')
    conn.commit()
    conn.close()

root = Tk()

canvas = Canvas(root, width=300, height=480)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.2, relwidth=0.8, relheight=0.8)

heading_label = Label(frame, text="Add data")
heading_label.grid(row=0, column=1)

name_label = Label(frame, text="Name")
name_label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

age_label = Label(frame, text="Age")
age_label.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

address_label = Label(frame, text="Address")
address_label.grid(row=3, column=0)
entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

submit_button = Button(frame, text="Add", command= lambda: insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
submit_button.grid(row=4, column=1)

root.mainloop()
