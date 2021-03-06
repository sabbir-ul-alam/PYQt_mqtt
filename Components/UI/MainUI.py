
from PyQt5 import  QtWidgets as qtw

from Components.UI.Display.DisplayBox import DisplayBox
from Components.UI.Buttons.Buttons import  Buttons

from Components.Input.Input import Input
from PyQt5 import  QtCore as qtc
from PyQt5 import  QtGui as qtg

from PyQt5.QtGui import QKeySequence



class MainUI(qtw.QWidget):

    output=qtc.pyqtSignal(str)
    #display_result= None

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("MQTT Subscriber")
        self.resize(800,1200)
        self.setWindowIcon(qtg.QIcon("logger.ico"))
        self.setMaximumWidth(800)
        self.setMinimumHeight(1200)
        self.setMaximumHeight(1200)
        self.setMinimumWidth(800)
        self.layout = qtw.QGridLayout()

        self.display_result = qtw.QTextEdit()
        self.display_result.setReadOnly(True)
        self.display_result.setAcceptRichText(True)
        self.font = qtg.QFont()
        self.font.setPointSize(14)
        self.display_result.setFont(self.font)
        self.scrollBar = qtw.QScrollBar()
        self.display_result.setVerticalScrollBar(self.scrollBar)


        #self.inputUserName= Input().renderBox("Username")
        self.inputUserName = qtw.QLineEdit()
        self.inputUserName.setPlaceholderText("Username")


        #self.inputPassword=Input().renderBox("Password")
        self.inputPassword = qtw.QLineEdit()
        self.inputPassword.setPlaceholderText("Password")

        #self.inputClientId = Input().renderBox("Client ID")
        self.inputClientId = qtw.QLineEdit()
        self.inputClientId.setPlaceholderText("Client ID")



        #self.inputTopicName = Input().renderBox("Topic Name")
        self.inputTopicName = qtw.QLineEdit()
        self.inputTopicName.setPlaceholderText("Topic Name")

        self.connect = qtw.QPushButton("Connect")
        self.shortcut = qtw.QShortcut(QKeySequence("Ctrl+f"), self)










        # self.old_cursor = qtg.QTextCursor()
        # self.old_scrollbar_value=self.scrollBar.value()
        # self.is_scrolled_down = False
        # if self.old_scrollbar_value==self.scrollBar.maximum():
        #     self.is_scrolled_down = True
        # else:
        #     self.is_scrolled_down = False





        #self.clear.renderBox("Clear & Disconnect")











        # self.clipArt=qtw.QLabel()
        # pixmap = qtg.QPixmap('drop1.png')
        # lol=pixmap.scaled(400,400,qtc.Qt.KeepAspectRatio)
        # self.clipArt.setPixmap(lol)
        # self.clipArt.setMaximumWidth(500)
        # self.clipArt.setMaximumHeight(800)

        #self.display_result.ensureCursorVisible()
        #self.warning_label=qtw.QLabel()
       # self.warning_label.setFont(self.font)
        #self.layout.setColumnMinimumWidth(0,500)


        self.layout.addWidget(self.display_result,0,0,4,3)
        self.layout.addWidget(self.inputUserName, 5, 0,1,1)
        self.layout.addWidget(self.inputPassword ,5, 1,1,1)
        self.layout.addWidget(self.inputClientId, 6, 0,1,2)
        self.layout.addWidget(self.inputTopicName, 7, 0,1,2)

        self.layout.addWidget(self.connect ,8, 0,1,3)

        #self.layout.addWidget(self.warning_label, 4,4,1,2)




        self.setLayout(self.layout)
        # self.search_text_input.returnPressed.connect(self.search_words)
        # self.line_number_after_input.returnPressed.connect(self.search_words)
        # self.search_button.clicked.connect(self.search_words)
        # self.clear_button.clicked.connect(self.clear_all)
         #self.scrollBar.sliderPressed.connect(self.sliderPressed)

        """Signal Connections"""
        # self.search_text_input.returnPressed.connect(self.search_words)
        # self.line_number_after_input.returnPressed.connect(self.search_words)
        #self.connect.clicked.connect(self.conectionSignal)
        # self.clear.clicked.connect(
        #     lambda: Signals.clearAndDisconnectSignal(self,self.inputUserName, self.inputPassword, self.inputClientId,self.inputTopicName))
        # self.scrollBar.sliderPressed.connect(self.sliderPressed)

        self.show()


    # def dragEnterEvent(self, event):
    #     print("enter")
    #     self.disable_input()
    #     self.clear_button.setDisabled(True)
    #     event.acceptProposedAction()
    #
    #
    # def dragLeaveEvent(self, event):
    #     print("leave")
    #     self.enable_input()
    #     self.clear_button.setDisabled(False)
    #
    #
    # def dropEvent(self, event):
    #     self.enable_input()
    #     self.clear_button.setDisabled(False)
    #     self.fileText = []
    #     self.display_result.clear()
    #     path=event.mimeData().urls()
    #     path=path[0].path()
    #     path=path[1:]
    #     print(path)
    #     if path.endswith('.txt') or path.endswith('.log'):
    #         self.fileHandle(path)
    #     else:
    #         self.show_warning("File extension should be .txt or .log")
    #
    # def disable_input(self):
    #     self.upload_file_button.setDisabled(True)
    #     self.search_text_input.setDisabled(True)
    #     self.line_number_after_input.setDisabled(True)
    #     self.search_button.setDisabled(True)
    #
    # def enable_input(self):
    #     self.upload_file_button.setDisabled(False)
    #     self.search_text_input.setDisabled(False)
    #     self.line_number_after_input.setDisabled(False)
    #     self.search_button.setDisabled(False)
    #
    # def clear_all(self,):
    #     self.clipArt.show()
    #
    #     try:
    #      qtc.QCoreApplication.processEvents()
    #      self.upload_file_button.blockSignals(True)
    #      self.display_result.blockSignals(True)
    #      self.display_result.blockSignals(False)
    #      self.upload_file_button.blockSignals(False)
    #      print("cear all")
    #      if self.file:
    #         self.file.close()
    #      self.search_text_input.clear()
    #      self.line_number_after_input.clear()
    #      self.display_result.clear()
    #      self.warning_label.clear()
    #      self.fileText=[]
    #      print("all cleared")
    #      self.enable_input()
    #     except Exception as e:
    #         print(e)
    #         self.enable_input()
    #
    #
    #
    #
    # def show_warning(self,warning):
    #     print("show_warning")
    #
    #     self.warning_label.clear()
    #     self.warning_label.setText(warning)
    #     self.warning_label.setWordWrap(True)
    #     self.warning_label.setStyleSheet('color: red')
    #     self.enable_input()
    #     self.warning_label.setVisible(True)


    # def search_words(self):
    #     print("search_words")
    #     self.warning_label.clear()
    #     try:
    #         keyword=self.search_text_input.text()
    #         line_number=int(self.line_number_after_input.text())
    #
    #         if line_number >0 and len(keyword.strip())>0:
    #             self.match_words(keyword, line_number)
    #         else:
    #             self.show_warning("Line number cant be zero. And keyword cant be empty")
    #
    #     except:
    #         self.show_warning("Insert both search word and line number please")



    #
    # def match_words(self,keyword,line_number):
    #    # self.clear_all(clear_display_only=True)
    #
    #     print("match_words")
    #     list_of_block=[]
    #     len_of_file=len(self.fileText)
    #     if len_of_file<=0:
    #         self.show_warning("No file Found")
    #     else:
    #      cursor=0
    #      while(cursor<len_of_file):
    #          if self.fileText[cursor].find(keyword) !=-1:
    #              try:
    #                  tmp_sliced_list=self.fileText[cursor:(cursor+line_number)]
    #              except:
    #                  tmp_sliced_list = self.fileText[cursor:]
    #              cursor=cursor+line_number
    #              tmp_line="<br>".join(tmp_sliced_list)
    #              #<p style="color:red;">I am red</p>
    #              tmp_line=tmp_line.replace(keyword, '<b style="color:green;">{}</b>'.format(keyword))
    #              print(tmp_line)
    #              list_of_block.append(tmp_line)
    #          else:
    #              cursor=cursor+1
    #     self.show_block(list_of_block)


    # def show_block(self,block_list):
    #     try:
    #         self.disable_input()
    #         print("show_block")
    #
    #         if len(block_list)<=0:
    #             self.show_warning("No match found")
    #             self.display_result.clear()
    #         else:
    #             self.display_result.clear()
    #             for i in block_list:
    #                i=i+'<br>'+'<br>'+'<br>'
    #                self.display_file(txt=i)
    #             self.enable_input()
    #     except :
    #         self.enable_input()




    # def  display_file(self,txt=None):
    #
    #     if len(txt)>0:
    #         self.clipArt.hide()
    #         self.display_result.append(txt)
    #         #self.display_result.moveCursor( qtg.QTextCursor.End)
    #         qtc.QCoreApplication.processEvents()
    #         #print(txt)
    #
    #     else:
    #         self.show_warning("Nothing to show")


    # def fileHandle(self,path):
    #     self.clipArt.hide()
    #     try:
    #         self.file = open(path, 'r', encoding="utf8")
    #         self.disable_input()
    #         for line in self.file:
    #             self.display_file(txt=line)
    #             self.fileText.append(line)
    #         print("after clear")
    #         self.file.close()
    #         self.enable_input()
    #     except:
    #         print("no file found")
    #         self.enable_input()
    #
    # def open(self):
    #
    #
    #     self.fileText=[]
    #     self.display_result.clear()
    #     path = qtw.QFileDialog.getOpenFileName(self, '', '',
    #                                        'Text files (*.txt;*.log)')
    #     print(self.path)
    #     self.path=path[0]
    #     if path[0]:
    #         try:
    #             self.fileHandle(path[0])
    #
    #         except Exception as e:
    #             print(e)
    #             self.enable_input()



