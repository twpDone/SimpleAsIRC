#!/usr/bin/python

from Core import *
from Control import *
from Display import *

import threading
import re
import sys
import time

secure=False
bot=False
#botname="Hell0x"
botname="twp_bot"
chan="#dut.info"


for index in range(0,len(sys.argv)):
    if sys.argv[index]=="-B":
        bot=True
    if sys.argv[index]=="-N":
        try:
            botname=sys.argv[index+1]
            print("Je m'appelle : "+botname)
        except Exception as e:
            print("Erreur dans les arguments")
    if sys.argv[index]=="-C":
        try:
            chan=sys.argv[index+1]
            print("Joining : "+chan)
        except Exception as e:
            print("Erreur dans les arguments")
    if sys.argv[index]=="-s":
        print("IRC over SSL selected !")
        secure=True



if secure==False:
    core=Core(channel=chan, name=botname, port=6667, host='irc.freenode.net')
    print("SSL Disabled !!! Use -s for using SSL.")
else:
    core=secureCore(channel=chan, name=botname, port=6697, host='irc.freenode.net')
    print("SSL enabled !")

display=ConsoleDisplay()

if bot==False:
    control=Control(core,display)
else:
    print("Bot mode Activated !")
    control=BotControl(core,display)

control.start()
