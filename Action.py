#!/usr/bin/python

from Message import Message
import subprocess

class Action:
    def __init__(self,triggerText,functionToExecute):
        self.m_triggerText=triggerText;
        self.m_functionToExecute=functionToExecute;
    def doAction(self,Core,Message):
        try:
            self.m_functionToExecute(Core,Message);
        except Exception as e:
            print("Erreur lors du declenchement de l'action : ")
            print(e)

