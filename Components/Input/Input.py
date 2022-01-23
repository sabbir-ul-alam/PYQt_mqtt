
from PyQt5 import  QtWidgets as qtw


from PyQt5 import  QtCore as qtc
from PyQt5 import  QtGui as qtg

class Input(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lineInput=qtw.QLineEdit()


    def renderBox(self,param=None):
        self.lineInput.setPlaceholderText(param)
        return self.lineInput