
import PyQt.Components.UI.MainUI as ui

class Display():
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)


    def showOutput(self,param=None):
        print("output")
        ui.MainUI.display_result.append(param)
