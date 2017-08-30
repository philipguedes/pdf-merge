import os
import arrow
from tkinter import filedialog, Frame
from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from tkinter.scrolledtext import ScrolledText

FONT = ("Verdana", "12", "bold")


class Logging(object):
    def __init__(self, instance):
        self.master = instance
        Label(instance, text='Status', font=FONT).grid(row=3, column=5,
                                                       sticky=W, padx=10)
        self.logging = ScrolledText(instance, width=40, height=8, wrap=WORD,
                                    state='disabled', bg="white", relief=SUNKEN)

        self.grid()
        
    def grid(self):
        self.master.logging = self.logging
        self.master.logging.grid(row=4, column=5, rowspan=2, padx=10)

    def log_info(self, message):
        self.master.logging.configure(state='normal')
        self.master.logging.insert(END, message + '\n')
        self.master.logging.configure(state='disabled')
