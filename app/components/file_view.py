import os
from tkinter import filedialog, Frame
from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from tkinter.scrolledtext import ScrolledText

FONT = ("Verdana", "12", "bold")


class FileView(object):
    def __init__(self, instance):
        self.master = instance

        self.view = Treeview(instance, height=10, columns=('path'), selectmode='extended')
        self.view.heading('#0', text='index', anchor=CENTER)
        self.view.column('#0', minwidth=50, width=50, stretch=NO)
        self.view.heading('#1', text='path', anchor=CENTER)
        self.view.column('#1', minwidth=20, width=300, anchor=CENTER)
        self.view.grid(row=1, rowspan=4, columnspan=4, sticky='nsew')

        Label(instance, text='PDF Files', font=FONT).grid(row=0, sticky=NW)

        # Create add PDF button
        self.button1 = Button(instance, text='Load PDF',
                              command=self.open)
        self.button1.grid(row=6, column=0, sticky=W)

        # Create remove PDF button
        self.button2 = Button(instance, text='Remove PDF',
                              command=self.remove)
        self.button2.grid(row=6, column=1, sticky=W)

    def remove(self):
        selected = self.view.focus()
        item = self.view.item(selected).get('values')
        name = item.pop(0)
        self.view.delete(selected)
        self.update()
        self.master.log_info('Removed <{}> file'.format(name))      

    def open(self):
        filetypes = ("pdf files", "*.pdf"), ("all files", "*.*")
        filename = filedialog.askopenfilename(initialdir='~',
                                              title="Select file",
                                              filetypes=filetypes)
        if os.path.isfile(filename):
            name = os.path.basename(filename)
            self.view.insert('', 'end', text='', values=name, tag=filename)
            self.update()
            self.master.log_info('Loaded <{}> file'.format(name))

    def update(self):
        for index, item in enumerate(self.view.get_children()):
            self.view.item(item, text=index+1)

    def get_dict(self):
        pdfs = {}
        children = self.view.get_children()
        for child in children:
            data = self.view.item(child)
            key = data.get('text')
            tags = data.get('tags')
            path = tags.pop(0)
            pdfs.update({key: path})
        return pdfs