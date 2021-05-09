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

def search_tables_by_name(name):
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', port='5432')
    cursor = conn.cursor()

    query = '''SELECT * FROM STUDENT WHERE name=%s;'''
    cursor.execute(query, (name,))
    row = cursor.fetchone()

    display_search(row)
    conn.commit()
    conn.close()

def display_search(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert(END, row)

def display_all():
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', port='5432')
    cursor = conn.cursor()

    query = '''SELECT * FROM STUDENT;'''
    cursor.execute(query)
    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, column=1)
    for x in row:
        listbox.insert(END, x)

    conn.commit()
    conn.close()

root = Tk()

canvas = Canvas(root, width=480, height=500)
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

search_head = Label(frame, text="Search Data")
search_head.grid(row=5, column=1)

search_label = Label(frame, text="Search by Name")
search_label.grid(row=6, column=0)

name_search = Entry(frame)
name_search.grid(row=6, column=1)

go_search = Button(frame, text="Search", command= lambda: search_tables_by_name(name_search.get()))
go_search.grid(row=6, column=2)

display_all_items = Button(frame, text="Display all items", command= lambda: display_all())
display_all_items.grid(row=7, column=1)

root.mainloop()
