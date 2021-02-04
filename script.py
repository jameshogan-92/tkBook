from tkinter import *
from tkinter.ttk import * 
import sqlite3

btnText = "Submit"

conn = sqlite3.connect("lite1.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, author TEXT, quantity INTEGER, price REAL)")

window = Tk()

def insertBook():
    tit = title.get()
    auth = author.get()
    qty = quantity.get()
    prc = price.get()
    print('Hewwo')
    cursor.execute("INSERT INTO store VALUES(?,?,?,?)",(tit,auth,qty,prc))
    conn.commit()
    print(view())
    conn.close()
    # t1.insert(END, test)

b1 = Button(window,text=btnText, command=insertBook)
b1.grid(row=1,column=2)

title = StringVar()
e1 = Entry(window, textvariable=title)
e1.grid(row=0,column=0,columnspan=2)

author = StringVar()
e1 = Entry(window, textvariable=author)
e1.grid(row=1,column=0,columnspan=2)

quantity = StringVar()
e1 = Entry(window, textvariable=quantity)
e1.grid(row=2,column=0,columnspan=2)

price = StringVar()
e1 = Entry(window, textvariable=price)
e1.grid(row=3,column=0,columnspan=2)

t1 = Text(window, height=20,width=80)
t1.grid(row=4,column=0,rowspan=2)


# conn.close()

def view():
    connView = sqlite3.connect("lite1.db")
    cur = connView.cursor()
    connView.execute("SELECT * FROM store")
    rows = cur.fetchall()
    connView.close()
    return rows



window.mainloop()