#!/usr/bin/python

from Message import Message

class Display:
    def __init__(self):
        pass
    def getInput(self):
        pass
    def display(self,message):
        pass

class ConsoleDisplay(Display):
    def __init__(self):
        Display.__init__(self)
    def getInput(self):
        try:
            inp=raw_input(": ")
            return inp
        except:
            print "\nI Can't read"

    def display(self,message):
        print message.getDest()+"<="+message.getName()+":"+message.getText()

