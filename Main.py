import sys
from PyQt5 import  QtWidgets as qtw

from Components.UI.MainUI import MainUI
from Components.Singals.Signals import Signals
from PyQt5.QtCore import pyqtSlot
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    lol=MainUI()
    lol.connect.clicked.connect(
        lambda: Signals.conectionSignal("1",lol))
    lol.shortcut.activated.connect(
        lambda: Signals.on_search("1", lol))

    sys.exit(app.exec_())
