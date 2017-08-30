import os
import arrow
from tkinter import filedialog, Frame
from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from tkinter.scrolledtext import ScrolledText

FONT = ("Verdana", "12", "bold")


class Csv(object):
    def __init__(self, instance):
        self.master = instance

        Label(instance, text='Load CSV', font=FONT).grid(row=0, column=5, sticky=NW, padx=10)

        # Create Load CSV button
        self.button = Button(instance, text='Load CSV',
                             command=self.load_csv_file)
        self.button.grid(row=2, column=5, sticky=W, padx=10)

    def load_csv_file(self):
        filetypes = ("csv files", "*.csv"), ("all files", "*.*")
        filename = filedialog.askopenfilename(initialdir='~',
                                              title='Select File',
                                              filetypes=filetypes)
        if filename.endswith('.csv'):
            self.master.csv_file = filename
            message = 'Loaded <{}> file'.format(os.path.basename(filename))
            self.master.log_info(message)
