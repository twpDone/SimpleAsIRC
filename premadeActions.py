#!/usr/bin python
# -*- coding: utf-8 -*-

from Action import Action
from Message import Message

import time

def boxAction(Core,message):
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"booooooox !"))

def pingAction(Core,message):
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"!pong"))

def pongAction(Core,message):
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"!ping"))

def sucreAction(Core,message):
    Core.sendAction2Chan(Message(Core.m_channel,Core.m_name,"Ajoute du sucre dans le café!"))

def ninjaAction(Core,message):
    Core.sendAction2Chan(Message(Core.m_channel,Core.m_name,"Se deplace furtivement..."))
    time.sleep(10)
    Core.sendAction2Chan(Message(Core.m_channel,Core.m_name,"Surgit de l'ombre."))
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"NINJA !!!!"))
    Core.sendAction2Chan(Message(Core.m_channel,Core.m_name,"Lance un shuriken puis disparait dans l'ombre."))

def aperoAction(Core,message):
    Core.sendAction2Chan(Message(Core.m_channel,Core.m_name,"Paye sa tournée ! Hips..."))

def coffeeAction(Core,message):
    Core.sendAction2Chan(Message(Core.m_channel,Core.m_name,"Sert le café !"))
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"   ((,"))
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"   ,))"))
    Core.send2Chan(Message(Core.m_channel,Core.m_name," c|_| "))

def helpAction(Core,message):
    Core.send2Chan(Message(Core.m_channel,Core.m_name,"-help"))
    for act in actionTab:
        Core.send2Chan(Message(Core.m_channel,Core.m_name,"|-"+act.m_triggerText))

def manAction(Core,message):
    try:
        data=message.getText()
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
            Core.send2Chan(Message(Core.m_channel,Core.m_name,tabRes[line]))
    except:
        Core.send2Chan(Message(Core.m_channel,Core.m_name,"Pas de man !"))

actionTab=[]
actionTab.append(Action("!box",boxAction))
actionTab.append(Action("!help",helpAction))
actionTab.append(Action("!sucre",sucreAction))
actionTab.append(Action("!ninja",ninjaAction))
actionTab.append(Action("!apero",aperoAction))
actionTab.append(Action("!coffee",coffeeAction))
actionTab.append(Action("!ping",pingAction))
actionTab.append(Action("!pong",pongAction))
actionTab.append(Action("!man",manAction))

