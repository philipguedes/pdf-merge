import csv
from pdfrw import PdfFileReader, PdfFileWriter


class MainController(object):
    def __init__(self):
        self.queue = MyQueue()

    @property
    def queue_empty(self):
        return self.queue.empty

    def get_line(self):
        return self.queue.get()

    def read_csv(self, path):
        try:
            with open(path, newline='') as csvfile:
                sp = csv.reader(csvfile, delimiter=' ', quotechar=',')
                for row in sp:
                    line = row.pop(0)
                    split = self.split_csv_line(line)
                    self.queue.put(split)
        except:
            self.queue.clear()

    def split_csv_line(self, line):
        lines = list(map(lambda x: int(x), line.split(',')))
        if len(lines) == 3:
            elem = {}
            elem['pdf'], elem['from'], elem['to'] = lines[:]
            return elem

    def merge(self, pdfs, csv_file, dst_path):
        writer = PdfFileWriter()
        
        self.read_csv(csv_file)

        while self.queue_empty is False:
            elem = self.get_line()
            key = elem['pdf']
            
            path = pdfs.get(key)
            reader = PdfFileReader(fname=path)
            
            for x in range (-1, elem['to']-elem['from']):
                writer.addPage(reader.getPage(x+elem['from']))

        writer.write(fname=dst_path)


class MyQueue(object):
    def __init__(self):
        # Implementation of a FIFO queue
        self.__queue = []

    @property
    def size(self):
        return len(self.__queue)

    @property
    def empty(self):
        return self.size == 0

    def clear(self):
        self.__queue = []
    
    def get(self):
        if self.empty:
            return None
        return self.__queue.pop(0)

    def put(self, elem):
        self.__queue.append(elem)