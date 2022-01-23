
from PyQt5 import  QtWidgets as qtw


from PyQt5 import  QtCore as qtc
from PyQt5 import  QtGui as qtg

class DisplayBox(qtw.QWidget):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.display= qtw.QTextEdit()
        self.font = qtg.QFont()
        self.scrollBar = qtw.QScrollBar()

    def renderBox(self,param=None):
        self.display.setReadOnly(True)
        self.display.setAcceptRichText(True)

        self.font.setPointSize(14)
        self.display.setFont(self.font)
        self.display.setVerticalScrollBar(self.scrollBar)
        return self.display



