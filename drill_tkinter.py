
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(660, 240))
        self.master.title('Check files')
        self.master.config(bg='gray92')

        self.varFile1 = StringVar()
        self.varFile2 = StringVar()


        self.txtFile1 = Entry(self.master, text=self.varFile1, font=("Helvetica", 15), fg='black', bg='white', width=33)
        self.txtFile1.grid(row=0, column=1, padx=(40,0), pady=(50,0))

        self.txtFile2 = Entry(self.master, text=self.varFile2, font=("Helvetica", 15), fg='black', bg='white', width=33)
        self.txtFile2.grid(row=1, column=1,  padx=(40,0), pady=(20,0))

        self.btnBrowse = Button(self.master, text="Browse...", width=13, height=1)
        self.btnBrowse.grid(row=0, column=0,  padx=(20,0), pady=(50,0))

        self.btnBrowse = Button(self.master, text="Browse...", width=13, height=1)
        self.btnBrowse.grid(row=1, column=0,  padx=(20,0), pady=(20,0))


        self.btnCheck = Button(self.master, text="Check for files...", width=13, height=2)
        self.btnCheck.grid(row=2, column=0,  padx=(20,0), pady=(20,0))

        self.btnCancel = Button(self.master, text="Close Program", width=13, height=2)
        self.btnCancel.grid(row=2, column=1,  padx=(0,0), pady=(20,0), sticky=NE)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
