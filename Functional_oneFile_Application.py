#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import socket
import time
import threading
import re
import sys
from ssl import SSLSocket
import subprocess

HOST = 'irc.freenode.net'    # The remote host
PORT = 6667              # The same port as used by the server
SSLPORT=6697
BOTNAME = "twp_bot"
CHAN = "#dut.info"
regChan = ".*"+CHAN+".*"
SECURE=False


def send2Chan(message):
    time.sleep(1)
    s.sendall("PRIVMSG "+CHAN+" : "+message+" \r\n")

def sendAction2Chan(message):
    time.sleep(1)
    s.sendall("PRIVMSG "+CHAN+" :"+chr(1)+"ACTION "+message+chr(1)+" \r\n")

for index in range(0,len(sys.argv)):
    if sys.argv[index]=="-N":
        try:
            BOTNAME=sys.argv[index+1]
            print "Je m'appelle : "+BOTNAME
        except Exception as e:
            print "Erreur dans les arguments"
    if sys.argv[index]=="-C":
        try:
            CHAN=sys.argv[index+1]
            regChan = ".*"+CHAN+".*"
            print "Joining : "+CHAN
        except Exception as e:
            print "Erreur dans les arguments"
    if sys.argv[index]=="-s":
        PORT=SSLPORT
        SECURE=True

def boxAction(data):
    send2Chan("booooooox !")

def pingAction(data):
    send2Chan("!pong")

def pongAction(data):
    send2Chan("!ping")

def sucreAction(data):  
    sendAction2Chan("Ajoute du sucre dans le café!")

def ninjaAction(data):
    sendAction2Chan("Se deplace furtivement...")
    time.sleep(10)
    sendAction2Chan("Surgit de l'ombre.")
    send2Chan("NINJA !!!!")
    sendAction2Chan("Lance un shuriken puis disparait dans l'ombre.")

def aperoAction(data):
    sendAction2Chan("Paye sa tournée ! Hips...")

def coffeeAction(data):
    sendAction2Chan("Sert le café !")
    send2Chan("   ((,")
    send2Chan("   ,))")
    send2Chan(" c|_| ")

def helpAction(data):
    send2Chan("-help")
    for act in ACTION:
        send2Chan("|-"+act)

def manAction(data):
    tabData=data.split(":")
    data=string.replace(tabData[len(tabData)-1],"!man ","")
    data=string.replace(data," ","")
    data=string.replace(data,"\r","")
    data=string.replace(data,"\n","")
    resman=subprocess.check_output(["man",data])
    tabRes=resman.split("\n")
    for line in range(0,len(tabRes)):
        if line%5==0:
            time.sleep(2)
        if tabRes[line].__contains__("DESCRIPTION"):
            break
        s.sendall("PRIVMSG "+CHAN+" :"+tabRes[line]+"\r\n")

ACTION = {"!box":boxAction,"!help":helpAction,"!sucre":sucreAction,"!ninja":ninjaAction,"!apero":aperoAction,"!coffee":coffeeAction,"!ping":pingAction,"!pong":pongAction,"!man":manAction}

def action(data):
    for action in ACTION:
        if data.__contains__(action):
            ACTION[action](data)

def ecoute():
    while 1:
        data = s.recv(1024)
        print "'"+data+"'"
        if re.match(regChan,data.lower())!=None:
            action(data)
            tabData=data.split(":")
            pseudo=data.split("!")[0]
            prompt="<"+"".join(pseudo)+"> : "
            tabData.pop(0)
            tabData.pop(0)
            msg=":".join(tabData)

            print(prompt+msg)
        if data.upper().__contains__("PING"):
            s.sendall('PONG\r\n')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if SECURE:
    ss=s
    s=SSLSocket(ss)
s.connect((HOST, PORT))
s.sendall('PASS irc\r\n')
s.sendall('NICK '+BOTNAME+'\r\n')
s.sendall('USER '+BOTNAME+' 127.0.0.1 '+HOST+' '+BOTNAME+'\r\n')
data = s.recv(1024)
print(data)

def join(s):
    s.sendall('JOIN '+CHAN+'\r\n')
join(s)

data = s.recv(1024)
print(data)
tEcoute=threading.Thread(None, ecoute, None, (), {})
tEcoute.start()

while 1:
    try:
        inp=raw_input(": ")
        if inp=="quit":
            break
        toSend="PRIVMSG "+CHAN+" :"+inp+'\r\n'
        s.sendall(toSend)
    except:
        print "\nI Can't read"
tEcoute._Thread__stop()
s.close()


