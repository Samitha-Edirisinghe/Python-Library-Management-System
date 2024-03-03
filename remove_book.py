from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import sys

py = sys.executable

class rb(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,250)
        self.minsize(500,250)
        self.title("Remove book")
        a = StringVar()

        def aaa():
            if len(a.get()) == 0:
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                c = messagebox.askyesno('Remove Book', 'Are You Sure You Want To Remove The Book')
                if c:
                    try:
                        self.conn = sqlite3.connect('library_administration.db')
                        self.mycursor = self.conn.cursor()
                        self.mycursor.execute("DELETE FROM books WHERE Book_Id = ?",[a.get()])
                        messagebox.showinfo('Remove', 'Succesfully Removed')
                        self.conn.commit()
                        self.conn.close()
                        d = messagebox.askyesno("Confirm","Do you want to remove another book")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'remove_book.py'))
                        else:
                            self.destroy()
                    except Error:
                        messagebox.showerror("Error", "Something Goes Wrong")

        lb = Label(self, text="Enter Book Id", font=('Comic Scan Ms', 20, 'bold'))
        lb.place(x=30, y=70)
        e = Entry(self, textvariable=a, width=30).place(x=240, y=75)
        bt = Button(self, text="Remove", width=20, command=aaa).place(x=240, y=120)

rb().mainloop()
