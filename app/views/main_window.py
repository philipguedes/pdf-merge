import os
import arrow
from tkinter import filedialog, Frame
from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from tkinter.scrolledtext import ScrolledText
from components.logging import Logging


FONT = ("Verdana", "12", "bold")


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid(padx=(10, 0), pady=30)
        self.csv_file = None
        self.create_widgets()

    @property
    def pdf_dict(self):
        pdfs = {}
        children = self.file_window.get_children()
        for child in children:
            data = self.file_window.item(child)
            print(data)
            key = data.get('text')
            tags = data.get('tags')
            path = tags.pop(0)
            pdfs.update({key: path})
        return pdfs

    @property
    def csv_loaded(self):
        return csv_file is None

    def create_widgets(self):
        """
        Creates all widgets used in templte
        """
        self.__create_pdf_widgets()
        self.__create_csv_widgets()
        self.__create_logging_widgets()
        self.__create_file_view()
        self.button4 = Button(self, text='Merge It!',
                              command=self.merge_pdf)
        self.button4.grid(row=6, column=5, sticky=W, padx=10)

    def __create_file_view(self):
        """
        Creates file view widget
        """
        self.file_window = Treeview(self, height=10, columns=('path'), selectmode='extended')
        self.file_window.heading('#0', text='index', anchor=CENTER)
        self.file_window.column('#0', minwidth=50, width=50, stretch=NO)
        self.file_window.heading('#1', text='path', anchor=CENTER)
        self.file_window.column('#1', minwidth=20, width=300, anchor=CENTER)
        self.file_window.grid(row=1, rowspan=4, columnspan=4, sticky='nsew')

    def __create_pdf_widgets(self):
        """
        Creates pdf widgets
        """
        Label(self, text='PDF Files', font=FONT).grid(row=0, sticky=NW)

        # Create add PDF button
        self.button1 = Button(self, text='Load PDF',
                              command=self.open_pdf_file)
        self.button1.grid(row=6, column=0, sticky=W)

        # Create remove PDF button
        self.button2 = Button(self, text='Remove PDF',
                              command=self.remove_selected_pdf)
        self.button2.grid(row=6, column=1, sticky=W)

    def __create_logging_widgets(self):
        """
        Creates logging widgets
        """
        self.logger = Logging(self)

    def __create_csv_widgets(self):
        """
        Creates CSV widgets
        """
        Label(self, text='Load CSV', font=FONT).grid(row=0, column=5, sticky=NW, padx=10)

        # Create Load CSV button
        self.button3 = Button(self, text='Load CSV',
                              command=self.load_csv_file)
        self.button3.grid(row=2, column=5, sticky=W, padx=10)

    def remove_selected_pdf(self):
        selected = self.file_window.focus()
        item = self.file_window.item(selected).get('values')
        name = item.pop(0)
        self.file_window.delete(selected)
        self.update_file_index()
        self.log_info('{} removed'.format(name))

    def load_csv_file(self):
        filetypes = ("csv files", "*.csv"), ("all files", "*.*")
        filename = filedialog.askopenfilename(initialdir='~',
                                              title='Select File',
                                              filetypes=filetypes)
        if filename.endswith('.csv'):
            self.csv_loaded = True
            self.csv_file = filename

    def log_info(self, message):
        self.logger.log_info(message)

    def update_file_index(self):
        for index, item in enumerate(self.file_window.get_children()):
            self.file_window.item(item, text=index+1)
        self.log_info('updated file index')

    def open_pdf_file(self):
        filetypes = ("pdf files", "*.pdf"), ("all files", "*.*")
        # TODO: Change this initialdir
        filename = filedialog.askopenfilename(initialdir='~/dev/pdf-merge',
                                              title="Select file",
                                              filetypes=filetypes)
        # Check if filename is None
        if os.path.isfile(filename):
            name = os.path.basename(filename)
            self.file_window.insert('', 'end', text='erro', values=name, tag=filename)
            self.update_file_index()
            
        print(filename)
        print(self.pdf_dict)

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