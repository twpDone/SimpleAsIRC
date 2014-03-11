#!/usr/bin/python

from Message import Message
from Action import Action

import socket
import string
import re
import time
#ssl support 
from ssl import SSLSocket

class Core:
    def __init__(self,channel="#dut.info",name="twp_bot",port=6667,host='irc.freenode.net'):
        self.m_channel=channel
        self.m_host=host
        self.m_port=port
        self.m_name=name
        self.m_socket=self.createSocket();
    def start(self):
        self.m_socket.connect((self.m_host, self.m_port))
        self.m_socket.sendall('PASS irc\r\n')
        self.m_socket.sendall('NICK '+self.m_name+'\r\n')
        self.m_socket.sendall('USER '+self.m_name+' 127.0.0.1 '+self.m_host+' '+self.m_name+'\r\n')
        self.m_socket.sendall('JOIN '+self.m_channel+'\r\n')
    def createSocket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def send2Chan(self,Message):
        time.sleep(1)
        self.m_socket.sendall("PRIVMSG "+Message.getDest()+" : "+Message.getText()+" \r\n")
    def sendAction2Chan(self,Message):
        time.sleep(1)
        self.m_socket.sendall("PRIVMSG "+Message.getDest()+" :"+chr(1)+"ACTION "+Message.getText()+chr(1)+" \r\n")
    def read(self):
        try:
            data = self.m_socket.recv(1024)
            #recuperation des donnees pour le Message
            tabData=data.split(":")
            pseudo=data.split("!")[0]
            prompt="<"+"".join(pseudo)+"> : "
            tabData.pop(0)
            tabData.pop(0)
            msg=":".join(tabData)
            #manque recuperation du destinataire
            regName = ".*(PRIVMSG|NOTICE) "+self.m_name+" :.*"
            if re.match(regName.lower(),data.lower())!=None:
                return Message(self.m_name,pseudo,msg)
            regChan = ".*PRIVMSG "+self.m_channel+" :.*"
            if re.match(regChan.lower(),data.lower())!=None:
                return Message(self.m_channel,pseudo,msg)
            if data.upper().__contains__("PING"):
                self.m_socket.sendall('PONG\r\n')
        except Exception as ex:
            print("Erreur de reception")
            print(ex)
    def quit(self):
        self.m_socket.close();

class secureCore(Core):
    def __init__(self,channel="#dut.info",name="twp_bot",port=6697,host='irc.freenode.net'):
        Core.__init__(self,channel="#dut.info",name="twp_bot",port=6697,host='irc.freenode.net')
        self.m_socket=self.createSocket()
    def createSocket(self):
        return SSLSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

