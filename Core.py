#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# Core of the application, implement a part of the RFC 1459: Internet Relay Chat ProtocolA (Client side).

from Message import Message
from Action import Action

import socket
import string
import re
import time
#ssl support 
from ssl import SSLSocket

##
# Core of the application.
class Core:

    ##
    # Constructor.
    # @param self Self. 
    # @param channel Channel to connect.
    # @param name Nickname for the IRC user.
    # @param port Port to use.
    # @param host IRC Server host.
    def __init__(self,channel="#dut.info",name="twp_bot",port=6667,host='irc.freenode.net'):

        ##
        # @val m_channel Channel to connect.
        self.m_channel=channel

        ##
        # @val m_host IRC Server host.
        self.m_host=host

        ##
        # @val m_port Port to use.
        self.m_port=port

        ##
        # @val m_name Nickname for the IRC user.
        self.m_name=name

        ##
        # @val m_socket Socket to use for I/O.
        self.m_socket=self.createSocket();

    ##
    # Start the communication
    # @note connect the .m_socket
    # @param self Self.
    def start(self):
        self.m_socket.connect((self.m_host, self.m_port)) # connect the socket
        self.helloIRC() # start the IRC protocol

    ##
    # Start the IRC protocol.
    # @param self Self.
    def helloIRC(self):
        self.m_socket.sendall('PASS irc\r\n') #send password
        self.m_socket.sendall('NICK '+self.m_name+'\r\n') # define  nickname
        self.m_socket.sendall('USER '+self.m_name+' 127.0.0.1 '+self.m_host+' '+self.m_name+'\r\n') # define user
        self.m_socket.sendall('JOIN '+self.m_channel+'\r\n') # Join channel

    ##
    # Create a new TCP socket.
    # @param self Self.
    def createSocket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new TCP socket.

    ##
    # Send a Message to a channel or destination user
    # @param self Self.
    # @param Message Message object to send.
    def send2Chan(self,Message):
        time.sleep(1) # wait 1 second, avoid the flood kick
        # Send the Message to a channel or destination user
        self.m_socket.sendall("PRIVMSG "+Message.getDest()+" : "+Message.getText()+" \r\n") 

    ##
    # Send a Message as an IRC Action to a channel or destination user.
    # @param self Self.
    # @param Message Message object to send.
    def sendAction2Chan(self,Message):
        time.sleep(1) # wait 1 second, avoid the flood kick
         # Send the Message as an IRC Action to a channel or destination user.
        self.m_socket.sendall("PRIVMSG "+Message.getDest()+" :"+chr(1)+"ACTION "+Message.getText()+chr(1)+" \r\n")

    ##
    # Read from the m_socket, if the message dest is the joined chan or the current nickname.
    # @note Define how the application react for the "nickname already in use" warning
    # @note Send Pong (Ping back) to avoid IRC Time out.
    # @return Return a Message Object if the read data match .
    # @param self Self.
    def read(self):
        try:
            data = self.m_socket.recv(1024) # read from socket
            # delete \r and \n line's ending
            data=data.replace("\r","")
            data=data.replace("\n","")
            
            #get data for constructing the Message objet.
            tabData=data.split(":")
            pseudo=data.split("!")[0] # get source's nickname
            prompt="<"+"".join(pseudo)+"> : " # def prompt 
            
            # pop useless infos
            tabData.pop(0)
            tabData.pop(0)
            
            msg=":".join(tabData) # re-join text

            # if "nickname already in use" warning
            if re.match(".*already in use.*".lower(),data.lower())!=None:
                self.m_name+="_" # append an underscore to the current nickname
                self.m_socket.sendall('NICK '+self.m_name+'\r\n') # define the new nickname
                self.m_socket.sendall('JOIN '+self.m_channel+'\r\n') # join the channel with the new nickname
            
            #manque recuperation du destinataire
            regName = ".*(PRIVMSG|NOTICE) ("+self.m_name+"|\*) :.*" # define the regex wich must match

            # if the regex matches
            if re.match(regName.lower(),data.lower())!=None:
                # return a new Message object.
                return Message(self.m_name,pseudo,msg) 
            
            # define the regex wich must match
            regChan = ".*PRIVMSG "+self.m_channel+" :.*"
            if re.match(regChan.lower(),data.lower())!=None:
                # return a new Message object.
                return Message(self.m_channel,pseudo,msg)

            # if the server sends a ping, ping back => send pong
            if data.upper().__contains__("PING"):
                self.m_socket.sendall('PONG\r\n')

        except Exception as ex:
            print("Erreur de reception")
            print(ex)

    ##
    # Ends the IRC protocol
    # @note Close the socket
    # @param self Self.
    def quit(self):
        self.m_socket.close();

##
# Overload the Core class to use a SSL Socket.
class secureCore(Core):
    def __init__(self,channel="#dut.info",name="twp_bot",port=6697,host='irc.freenode.net'):
        Core.__init__(self,channel,name,port,host)
        self.m_socket=self.createSocket()

    ##
    # Overload the Core.createSocket to use a SSL Socket.
    def createSocket(self):
        return SSLSocket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

