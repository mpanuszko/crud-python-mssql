#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from functions import db

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()
    if index:
        selected_tuple = list1.get(index[0])
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[6])
        e7.delete(0, END)
        e7.insert(END, selected_tuple[7])
        e8.delete(0, END)
        e8.insert(END, selected_tuple[8])
        e9.delete(0, END)
        e9.insert(END, selected_tuple[9])
        

def view_command():
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


def search_command():
    list1.delete(0, END)
    for row in db.search(ProductName_text.get(), SupplierID_text.get(), CategoryID_text.get(),
                         QuantityPerUnit_text.get(), UnitPrice_text.get()):
        list1.insert(END, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


def add_command():
    db.insert(ProductName_text.get(), SupplierID_text.get(), CategoryID_text.get(), QuantityPerUnit_text.get(),
              UnitPrice_text.get(), UnitsInStock_text.get(), UnitsOnOrder_text.get(), ReorderLevel_text.get(),
              Discontinued_text.get())
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


def delete_command():
    db.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


def update_command():
    db.update(selected_tuple[0], ProductName_text.get(), SupplierID_text.get(), CategoryID_text.get(),
              QuantityPerUnit_text.get(), UnitPrice_text.get())
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))


def clear_command():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)

window = Tk()

MainFrame = Frame(window, pady=62, bg="gainsboro")
MainFrame.grid()

TitFrame = Frame(MainFrame, bd=1, padx=25, pady=32, bg="gainsboro", relief=RIDGE)
TitFrame.pack(side=TOP)

window.lblTit = Label(TitFrame, font=('arial', 37, 'bold'), text="Product Management System - Northwind Database",
                      bg="gainsboro")
window.lblTit.grid(sticky=N)

DataFrame = Frame(MainFrame, bd=0, pady=31, padx=21, relief=RIDGE, bg="Ghost White")
DataFrame.pack(side=BOTTOM)

ButtonFrame = Frame(DataFrame, bd=0, bg="Ghost White", relief=RIDGE)
ButtonFrame.pack(side=RIGHT)

DataFrameLEFT = LabelFrame(DataFrame, bd=0, relief=RIDGE, font=('arial', 20, 'bold'), bg="Ghost White",
                           text="Products:\n")
DataFrameLEFT.pack(side=LEFT)

DataFrameUp = Frame(DataFrame, padx=111, pady=60, bd=0, bg="Ghost White", relief=RIDGE)
DataFrameUp.pack(side=TOP)


def on_closing():
    dd = db
    if messagebox.askokcancel("Exit", "Are You Sure You Want To Quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)

l1 = Label(DataFrameUp, text="ProductName", height=2, width=12, bg="Ghost White")
l1.grid(row=0, column=0)

l2 = Label(DataFrameUp, text="SupplierID", height=2, width=12, bg="Ghost White")
l2.grid(row=1, column=0)

l3 = Label(DataFrameUp, text="CategoryID", height=2, width=12, bg="Ghost White")
l3.grid(row=2, column=0)

l4 = Label(DataFrameUp, text="QuantityPerUnit", height=2, width=12, bg="Ghost White")
l4.grid(row=3, column=0)

l5 = Label(DataFrameUp, text="UnitPrice", height=2, width=12, bg="Ghost White")
l5.grid(row=4, column=0)

l6 = Label(DataFrameUp, text="UnitsInStock", height=2, width=12, bg="Ghost White")
l6.grid(row=5, column=0)

l7 = Label(DataFrameUp, text="UnitsOnOrder", height=2, width=12, bg="Ghost White")
l7.grid(row=6, column=0)

l8 = Label(DataFrameUp, text="ReorderLevel", height=2, width=12, bg="Ghost White")
l8.grid(row=7, column=0)

l9 = Label(DataFrameUp, text="Discontinued", height=2, width=12, bg="Ghost White")
l9.grid(row=8, column=0)

ProductName_text = StringVar()
e1 = Entry(DataFrameUp, width=35, textvariable=ProductName_text)
e1.grid(row=0, column=1)

SupplierID_text = StringVar()
e2 = Entry(DataFrameUp, width=35, textvariable=SupplierID_text)
e2.grid(row=1, column=1)

CategoryID_text = StringVar()
e3 = Entry(DataFrameUp, width=35, textvariable=CategoryID_text)
e3.grid(row=2, column=1)

QuantityPerUnit_text = StringVar()
e4 = Entry(DataFrameUp, width=35, textvariable=QuantityPerUnit_text)
e4.grid(row=3, column=1)

UnitPrice_text = StringVar()
e5 = Entry(DataFrameUp, width=35, textvariable=UnitPrice_text)
e5.grid(row=4, column=1)

UnitsInStock_text = StringVar()
e6 = Entry(DataFrameUp, width=35, textvariable=UnitsInStock_text)
e6.grid(row=5, column=1)

UnitsOnOrder_text = StringVar()
e7 = Entry(DataFrameUp, width=35, textvariable=UnitsOnOrder_text)
e7.grid(row=6, column=1)

ReorderLevel_text = StringVar()
e8 = Entry(DataFrameUp, width=35, textvariable=ReorderLevel_text)
e8.grid(row=7, column=1)

Discontinued_text = StringVar()
e9 = Entry(DataFrameUp, width=35, textvariable=Discontinued_text)
e9.grid(row=8, column=1)

list1 = Listbox(DataFrameLEFT, height=25, width=75)
list1.grid(row=5, column=0, rowspan=15, columnspan=2)
    
sb1 = Scrollbar(DataFrameLEFT)
sb1.grid(row=5, column=2, rowspan=15, sticky='ns')
    
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
    
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(ButtonFrame, text="View All", font=('arial', 20, 'bold'), height=1, width=12, bd=4, command=view_command)
b1.grid(row=0, column=3)

b2 = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=12, bd=4, command=clear_command)
b2.grid(row=1, column=3)

b3 = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=12, bd=4, command=search_command)
b3.grid(row=2, column=3)

b4 = Button(ButtonFrame, text="Insert", font=('arial', 20, 'bold'), height=1, width=12, bd=4, command=add_command)
b4.grid(row=3, column=3)

b5 = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=12, bd=4,
            command=update_command)
b5.grid(row=4, column=3)

b6 = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=12, bd=4, command=delete_command)
b6.grid(row=5, column=3)

b7 = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=12, bd=4, command=on_closing)
b7.grid(row=6, column=3)

window.overrideredirect(True)
window.overrideredirect(False)
#window.attributes('-fullscreen', True)
window.mainloop()