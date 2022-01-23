import sys
from PyQt5 import  QtWidgets as qtw

from Components.UI.MainUI import MainUI
from Components.Singals.Signals import Signals

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    lol=MainUI()
    lol.connect.clicked.connect(
        lambda: Signals.conectionSignal("1",lol))
    sys.exit(app.exec_())
