# -*- coding: utf-8 -*-
"""
Sample processing method. You can, for example, add a process pool to handle them concurrently.
"""


def on_message(client, userdata, message,ui):
    # print(f"Message Topic: {message.topic}")
    # print(f"Message ID: {message.mid}")
    # print(f"Message Payload: {message.payload.decode('utf-8')}")

    ui.display_result.append(f"\nMessage Topic: {message.topic}")
    ui.display_result.append(f"Message ID: {message.mid}")
    ui.display_result.append(f"Message Payload: {message.payload.decode('utf-8')}\n")
