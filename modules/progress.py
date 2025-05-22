from time import sleep

class Counter:
    def __init__(self, total, formatter: callable):
        self.total = total
        self.current = 0
        self.formatter = formatter

    def increment(self):
        self.current += 1
        self.display()

    def display(self):
        print('\r', str(self.formatter(self.current, self.total)), end = '')

    def finish(self):
        self.display()
        print("") #advances cursor to next line