# -*- coding: utf-8 -*-
"""
Sample processing method. You can, for example, add a process pool to handle them concurrently.
"""
import json

from json import dumps
from json import JSONEncoder
import re
from PyQt5 import  QtGui as qtg

def on_message(client, userdata, message,ui):
    # print(f"Message Topic: {message.topic}")
    # print(f"Message ID: {message.mid}")
    # print(f"Message Payload: {message.payload.decode('utf-8')}")
    try:
        # ui.display_result.append(f"Message Topic: {message.topic}")
        # ui.display_result.append(f"Message ID: {message.mid}")
        text=str({message.payload.decode('utf-8')})
        text=  re.sub("status",'<b style="color:green;">{}</b>'.format("status"),text)
        text = re.sub("sequence", '<b style="color:blue;">{}</b>'.format("sequence"),text)
        text = re.sub("room_type", '<b style="color:red;">{}</b>'.format("room_type"),text)

        ui.display_result.append(f"Message Topic: {message.topic} <br/> Message ID: {message.mid} <br/> Message Payload:{text} <br/>.<br/>.<br/>")

        ui.display_result.moveCursor(qtg.QTextCursor.End)
    except Exception as e:
        print(e)
