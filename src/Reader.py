# -*- coding: utf-8 -*-


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.msg = ""

    def read(self):
        f = open(self.filename)
        self.msg =  f.read()
        
        return self.msg
    def lines(self):
        f = open(self.filename)
        self.lines = f.readlines()
        return self.lines

a = Reader("Tokenizer.py")
print a.lines()

