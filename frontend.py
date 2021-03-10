"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close
"""
from tkinter import *
from backend import Database

database = Database("books.db")
class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("BookStore")

        b1 = Button(window, text = "View all", width = 10, command = self.view_command)
        b1.grid(row = 2, column = 3)
        b2 = Button(window, text = "Search entry", width = 10, command = self.search_command)
        b2.grid(row = 3, column = 3)
        b3 = Button(window, text = "Add entry", width = 10, command = self.insert_command)
        b3.grid(row = 4, column = 3)
        b4 = Button(window, text = "Update entry", width = 10, command = self.update_command)
        b4.grid(row = 5, column = 3)
        b5 = Button(window, text = "Delete", width = 10, command = self.delete_command)
        b5.grid(row = 6, column = 3)
        b6 = Button(window, text = "Close", width = 10, command = window.destroy)
        b6.grid(row = 7, column = 3)

        l1 = Label(window, text = "Title")
        l1.grid(row = 0, column = 0)
        l2 = Label(window, text = "Author")
        l2.grid(row = 0, column = 2)
        l3 = Label(window, text = "Year")
        l3.grid(row = 1, column = 0)
        l4 = Label(window, text = "ISBN")
        l4.grid(row = 1, column = 2)

        self.e1_value = StringVar()
        self.e1 = Entry(window, textvariable = self.e1_value)
        self.e1.grid(row = 0, column = 1)

        self.e2_value = StringVar()
        self.e2 = Entry(window, textvariable = self.e2_value)
        self.e2.grid(row = 0, column = 3)

        self.e3_value = StringVar()
        self.e3 = Entry(window, textvariable = self.e3_value)
        self.e3.grid(row = 1, column = 1)

        self.e4_value = StringVar()
        self.e4 = Entry(window, textvariable = self.e4_value)
        self.e4.grid(row = 1, column = 3)

        self.lb1 = Listbox(window, height = 6, width = 35)
        self.lb1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

        sb1 = Scrollbar(window)
        sb1.grid(row = 2, column = 2, rowspan = 6)

        self.lb1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.lb1.yview)
        self.lb1.bind('<<ListboxSelect>>', self.get_selected_row)


    def view_command(self):
        self.lb1.delete(0, END)
        for row in database.view():
            self.lb1.insert(END, row)

    def search_command(self):
        self.lb1.delete(0, END)
        for row in database.search(self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get()):
            self.lb1.insert(END, row)

    def insert_command(self):
        database.insert(self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get())
        self.lb1.delete(0, END)
        self.lb1.insert(END, (self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get()))

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lb1.curselection()[0]
            self.selected_tuple  = self.lb1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.e1_value.get(), self.e2_value.get(), self.e3_value.get(), self.e4_value.get())


    # window.wm_title("BookStore")

    # b1 = Button(window, text = "View all", width = 10, command = view_command)
    # b1.grid(row = 2, column = 3)
    # b2 = Button(window, text = "Search entry", width = 10, command = search_command)
    # b2.grid(row = 3, column = 3)
    # b3 = Button(window, text = "Add entry", width = 10, command = insert_command)
    # b3.grid(row = 4, column = 3)
    # b4 = Button(window, text = "Update entry", width = 10, command = update_command)
    # b4.grid(row = 5, column = 3)
    # b5 = Button(window, text = "Delete", width = 10, command = delete_command)
    # b5.grid(row = 6, column = 3)
    # b6 = Button(window, text = "Close", width = 10, command = window.destroy)
    # b6.grid(row = 7, column = 3)
    #
    # l1 = Label(window, text = "Title")
    # l1.grid(row = 0, column = 0)
    # l2 = Label(window, text = "Author")
    # l2.grid(row = 0, column = 2)
    # l3 = Label(window, text = "Year")
    # l3.grid(row = 1, column = 0)
    # l4 = Label(window, text = "ISBN")
    # l4.grid(row = 1, column = 2)
    #
    # e1_value = StringVar()
    # e1 = Entry(window, textvariable = e1_value)
    # e1.grid(row = 0, column = 1)
    #
    # e2_value = StringVar()
    # e2 = Entry(window, textvariable = e2_value)
    # e2.grid(row = 0, column = 3)
    #
    # e3_value = StringVar()
    # e3 = Entry(window, textvariable = e3_value)
    # e3.grid(row = 1, column = 1)
    #
    # e4_value = StringVar()
    # e4 = Entry(window, textvariable = e4_value)
    # e4.grid(row = 1, column = 3)
    #
    # lb1 = Listbox(window, height = 6, width = 35)
    # lb1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
    #
    # sb1 = Scrollbar(window)
    # sb1.grid(row = 2, column = 2, rowspan = 6)
    #
    # lb1.configure(yscrollcommand = sb1.set)
    # sb1.configure(command = lb1.yview)
    # lb1.bind('<<ListboxSelect>>', get_selected_row)
window = Tk()
Window(window)
window.mainloop()
