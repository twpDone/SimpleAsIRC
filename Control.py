#!/usr/bin/python

from Core import *

import threading
import re
import sys
import time

class Control:
    def __init__(self,core,display):
        self.core=core
        self.display=display
        self.actions=[]
    
    def loadActions(self):
        #add Actions here
        pass
    
    def check(self,Message,actions):
        for action in self.actions:
            data=Message.getText()
            if data.__contains__(action.m_triggerText):
                action.doAction(self.core,Message)
    
    def ecoute(self):
        while 1:
            m=self.core.read()
            if m!=None:
                self.display.display(m)
                self.check(m,self.actions)
    
    def start(self):
        self.core.start()
        
        tEcoute=threading.Thread(None, self.ecoute, None, (), {})
        tEcoute.start()

        print("Control started")
        #should be in a separate method 
        while 1:
            inp=self.display.getInput()
            if inp=="quit":
                break
            else:
                self.core.send2Chan(Message(self.core.m_channel,self.core.m_name,inp))
        
        tEcoute._Thread__stop()
        self.core.quit()


class BotControl(Control):
    def __init__(self,core,display):
        Control.__init__(self,core,display)
        self.loadActions()

    def loadActions(self):
        #add Actions here            
        from premadeActions import actionTab
        for act in actionTab:
            self.actions.append(act)
