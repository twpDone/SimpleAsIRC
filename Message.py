#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# Store a Message 
class Message:

    ##
    # Constructor.
    # @param self Self.
    # @param dest Destination of the message.
    # @param name Source of the message.
    # @param text Text of the message.
    def __init__(self,dest,name,text):

        ## @var m_dest
        # Destination of the message
        self.m_dest=dest;

        ## @var m_name
        # Source of the message
        self.m_name=name;

        ## @var m_text
        # Text of the message.
        self.m_text=text;

    ##
    # Returns the destination of the message.
    # @return Destination of the message.
    def getDest(self):
	dest=self.m_dest
        return dest;

    ##
    # Returns the source's name of the message.
    # @return Source's name of the message.
    def getName(self):
        name=self.m_name;
        return name;

    ##
    # Returns the text of the message.
    # @return Text of the message.
    def getText(self):
        text=self.m_text;
        return text;
