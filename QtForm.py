
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.browser=QTextBrowser()
        self.lineedit=QLineEdit("Your message here")
        self.lineedit.selectAll()
        layout=QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineeedit.setFocus()
        self.connect(self.lineeedit, SIGNAL("returnPressed()"), self.sendMessage)
        self.setWindowTitle("SimpleAsIrc")
        self.textToSend=""
    def sendMessage(self):
        text=self.lineeedit.text()
        self.browser.append(str(text))
        self.textToSend=str(text)
    def display(self,message):
        text="["+message.getDest()+"] "+message.getName().replace(":","")+": "+message.getText()
        self.browser.append(str(text))
    def getInput(self):
        try:
            # try to get raw input
            self.textToSend=""
            while self.textToSend=="":
                pass
            return self.textToSend
        except:
            print("\nI Can't read")

