#!/usr/bin/python

class Message:
    def __init__(self,dest,name,text):
        self.m_dest=dest;
        self.m_name=name;
        self.m_text=text;
    def getDest(self):
	dest=self.m_dest
        return dest;
    def getName(self):
        name=self.m_name;
        return name;
    def getText(self):
        text=self.m_text;
        return text;
