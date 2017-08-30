import os
import arrow
from tkinter import filedialog, Frame
from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from tkinter.scrolledtext import ScrolledText
from components.logging import Logging
from components.csv import Csv
from components.file_view import FileView

FONT = ("Verdana", "12", "bold")


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid(padx=(10, 0), pady=30)
        self.csv_file = None
        self.create_widgets()

    @property
    def pdf_dict(self):
        return self.file_window.get_dict()

    @property
    def csv_loaded(self):
        return self.csv_file is not None

    def create_widgets(self):
        """
        Creates all widgets used in templte
        """
        self.__create_csv_widgets()
        self.__create_logging_widgets()
        self.__create_file_view()
        
        self.button = Button(self, text='Merge It!',
                              command=self.merge_pdf)
        self.button.grid(row=6, column=5, sticky=W, padx=10)

    def __create_file_view(self):
        """
        Creates file view widget
        """
        self.file_window = FileView(self)

    def __create_logging_widgets(self):
        """
        Creates logging widgets
        """
        self.logger = Logging(self)

    def __create_csv_widgets(self):
        """
        Creates CSV widgets
        """
        self.csv_component = Csv(self)

    def log_info(self, message):
        self.logger.log_info(message)

    def merge_pdf(self):
        filetypes = ("pdf files", "*.pdf"), ("all files", "*.*")
        filepath = filedialog.asksaveasfilename(initialdir='~',
                                                title='Save File',
                                                filetypes=filetypes)
        
        # Call handler save here
        
        print(filepath)
        print("file saved")


    # Create a logger
    # With time format
    # http://arrow.readthedocs.io/en/latest/