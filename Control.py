#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @package SimpleAsIrc
# @file Control.py
# Controls for the application.

from Core import *

import threading
import re
import sys
import time

##
# @class Control
# @Brief Controleur de l'application.
# @brief Contain references to Core, Action and Display objects.
# @see Core
# @see Display
# @see Action
class Control:

    ##
    # @brief Contructor of the Control class.
    # @param self Self reference.
    # @param core Core object reference.
    # @param display Display object reference.
    # @see Core
    # @see Display
    def __init__(self,core,display):
        ## @var core
        # Core object
        self.core=core

        ## @var display
        # Display object
        self.display=display

        ## @var actions 
        # Action object list
        self.actions=[] 
        
    ## 
    # Init the actions array
    def loadActions(self):
        #add Actions here
        pass
    
    ##
    # @brief Check if the application have to perform one action.
    # Checks if the Message match with one Action's trigger in the actions list.
    # If it matches, perfom the Action
    # @param self Self
    # @param Message Message object.
    # @param actions Action objects list in wich searching the Action that will be triggered by  the message.
    def check(self,Message,actions):
        for action in self.actions:
            data=Message.getText() # Get the Message text
            # if the Action trigger text is contained in the message, perform the action
            if data.__contains__(action.m_triggerText):
                action.doAction(self.core,Message) # perfom the action by calling the Action.doAction method.
    
    ##
    # Define how the application react while reading messages.
    # @param self Self.
    def ecoute(self):
        while 1:
            m=self.core.read() # read with the read core function.
            if m!=None:
                self.display.display(m) # display the received message by the Display.display method
                self.check(m,self.actions) # check if the application have to perform one action.

    ##
    # Define how the application react for sending messages.
    # @param self Self.
    def write(self):
        while 1:
            inp=self.display.getInput() # gets the user input by the Display.getInput method
            if inp=="quit":
                break # ends the function if the user type "quit"
            else:
                # send the message to the chan
                self.core.send2Chan(Message(self.core.m_channel,self.core.m_name,inp))

    ##
    # Start the application and controls the running application
    # @param self Self.
    def start(self):
        self.core.start() #start the Core
        
        tEcoute=threading.Thread(None, self.ecoute, None, (), {}) # create a (listen) thread for the ecoute method
        tEcoute.start() #start the thread

        tWrite=threading.Thread(None, self.write, None, (), {}) # create a thread for the write  method
        tWrite.start() #start the thread


        print("Control started")
        # if one thread is stopped, ends the application
        while 1:
            if not tWrite.isAlive(): 
                break
            if not tEcoute.isAlive():
                break

        tWrite._Thread__stop() # stop write thread
        tEcoute._Thread__stop() # stop ecoute (listen) thread
        self.core.quit() # quit the Core/ Ends irc protocol

##
# Overload the Function of the Control class to implement a Bot behaviour.
# @note the loadActions is overloaded to load the actions to be performed by the bot.
class BotControl(Control):
    ##
    # Constructor
    # @note load Actions when the object is constructed
    # @param self Self reference.
    # @param core Core object reference.
    # @param display Display object reference.
    # @see Core
    # @see Display
    def __init__(self,core,display):
        Control.__init__(self,core,display)
        self.loadActions() # load the actions
    
    ##
    # Load the actions to be performed by the bot.
    # @param self Self.
    def loadActions(self):
        # load the actions to be performed by the bot from the premadeActions file         
        from premadeActions import actionTab #import the actionTab list from the premadeActions file 
        for act in actionTab:
            self.actions.append(act) # add each Action in the self.actions list
