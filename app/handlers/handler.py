import csv
import pdfrw


class MainController(object):
    def __init__(self):
        self.queue = MyQueue()

    def read_csv(self, path):
        try:
            with open(path, newline='') as csvfile:
                sp = csv.reader(csvfile, delimiter=' ', quotechar=',')
                for row in sp:
                    line = row.pop(0)
                    split = self.split_csv_line(line)
                    self.queue.put(split)
        except:
            # TODO: Error messages
            return "Failed"

    def split_csv_line(self, line):
        lines = list(map(lambda x: int(x), line.split(',')))
        if len(lines) != 3:
            # TODO: Error messages
            return "Failed"
        elem = {}
        elem['pdf'], elem['from'], elem['to'] = lines[:]
        return elem

    def generate_pdf(self, filename):
        pass

    def join_pages(self):
        pass
    
    def read_pdfs(self, ordered_pdfs):
        pass

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
    
    def get(self):
        if self.empty:
            return None
        return self.__queue.pop(0)

    def put(self, elem):
        self.__queue.append(elem)