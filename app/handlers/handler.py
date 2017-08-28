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
        elem = {}
        elem['pdf'] = lines.pop(0)
        elem['range'] = lines[:]
        if len(lines) > 2:
            # TODO: Error messages
            return "Failed"
        return elem


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