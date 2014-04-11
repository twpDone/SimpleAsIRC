#!/usr/bin/python
# -*- coding: utf-8 -*-

from Message import Message

##
# @interface Display
# Define how to interact with the user.
class Display:

    ##
    # Constructor
    def __init__(self):
        pass
    ##
    # Method to get inputs from user
    # @return string The user input.
    def getInput(self):
        pass

    ##
    # Method to display a Message to the user
    # @param message Message
    def display(self,message):
        pass

##
# Implements the Display interface
# Console User Inteface
class ConsoleDisplay(Display):

    ##
    # Constructor
    def __init__(self):
        Display.__init__(self)

    ##
    # Method to get inputs from user
    def getInput(self):
        try:
            # try to get raw input
            inp=raw_input(": ")
            return inp
        except:
            print "\nI Can't read"
    ##
    # Display a Message to the user
    # @param message Message
    def display(self,message):
        # affiche [destination] <source>: text of the Message 
        print "["+message.getDest()+"] "+message.getName().replace(":","")+": "+message.getText() 

