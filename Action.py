#!/usr/bin/python
# -*- coding: utf-8 -*-

from Message import Message
import subprocess

##
# Class to store one Action
class Action:

    ##
    # Constructor.
    # @param self Self.
    # @param triggerText Text to trigger the Action.
    # @param functionToExecute Execute the Action
    # @note If Text matches the Action should be performed.
    def __init__(self,triggerText,functionToExecute):

        ## @var m_triggerText 
        # Text to trigger the Action
        self.m_triggerText=triggerText;

        ## @var m_functionToExecute
        # Fonction a executer
        self.m_functionToExecute=functionToExecute;

    ##
    # Perform the stored function.
    # @param Core Core object.
    # @param Message Message object.
    def doAction(self,Core,Message):
        try:
            # Try to execute the function
            self.m_functionToExecute(Core,Message);
        except Exception as e:
            print("Erreur lors du declenchement de l'action : ")
            print(e)

