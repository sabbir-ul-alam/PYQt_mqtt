
from Components.Services.Config import Config
from PyQt5 import  QtCore as qtc
from Components.Singals.process import on_message
from paho.mqtt.client import Client
from PyQt5.QtCore import QObject, pyqtSlot



class Signals(object):


    def __init__(self,ui,config: dict, message_processor=None, flag=0):
        self.ui=ui
        self.config = config
        self.client = Client(
            client_id=config.mqtt_client,
            clean_session=config.mqtt_clean_session,
            userdata={"client": config.mqtt_client},
        )

        self.client.username_pw_set(config.mqtt_username, config.mqtt_password)

        if self.config.mqtt_debug:
            self.client.on_log = self._on_log

        self.client.on_connect = self._on_connect
        self.client.on_subscribe = self._on_subscribe
        self.client.on_message = self._on_message
        self.client.on_publish = self._on_publish
        self.client.on_disconnect = self._on_disconnect


        self.client.connect(config.mqtt_host, config.mqtt_port, 60)
        if message_processor:
                self.message_processor = message_processor


    def conectionSignal(var:str,ui):
        print("singal called")
        if ui.connect.text()=="Connect":
            ui.connect.setText("Disconnect")
            ui.display_result.clear()
            userName = "server31"
            #userName=ui.inputUserName.text()
            password = "SP5WjUMnt1kF00"
            #password=ui.inputPassword.text()

            clientId = "communicator-admin-03"
            #clientId=ui.inputClientId.text()

            topicName = "communicator/0/9bf5b73e-8f06-499d-bc9a-09fcc52febfc/call_events"
           # topicName=ui.inputTopicName.text()
            ui.inputUserName.setDisabled(True)
            ui.inputPassword.setDisabled(True)
            ui.inputClientId.setDisabled(True)
            ui.inputTopicName.setDisabled(True)
            try:
                # path=Config.saveConfigFile(userName.text(),password.text(),clientId.text(),topicName.text())
                global path
                path= Config.saveConfigFile( userName, password, clientId, topicName)
                global config
                config= Config.load_from(path)
                global client
                client= Signals(ui,config, message_processor=on_message)
                client.listen()
            except:
                pass
        else:
            ui.connect.setText("Connect")
            client.disconnect()


    # def dis_client(self):
    #     self.client.disconnect()
    #     #self.client.loop_stop()






    def _on_log(self, client, userdata, level, buf):
       #qtc.QCoreApplication.processEvents()
       print("on log")
       #self.ui.display_result.append(f"{buf}, origin: {userdata['client']}")
    def _on_connect(self, client, userdata, flags, rc):
        #qtc.QCoreApplication.processEvents()
        print("on connect")
        self.client.subscribe(self.config.mqtt_topics)
        self.ui.display_result.append(f"Connecting.....")

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        #qtc.QCoreApplication.processEvents()
        print("on subscribe")
        self.ui.display_result.append(f"Subscribed")
        self.ui.display_result.append(f'Listening for {self.config.mqtt_topics}...')
    def _on_disconnect(self, client, userdata, rc):
        #qtc.QCoreApplication.processEvents()
        print("on disconnect")
        self.ui.display_result.append(f"Disconnected {userdata['client']}, result code: {str(rc)}")


    def _on_message(self, client, userdata, msg):
        #qtc.QCoreApplication.processEvents()
        print("on message")
        if hasattr(self, "message_processor"):
            self.message_processor(client, userdata, msg,self.ui)
        else:
            self.ui.display_result.append(f"Topic: {msg.topic}, Mid: {msg.mid}, Payload: {msg.payload.decode('utf-8')}")
    def _on_publish(self, client, userdata, mid):
        #qtc.QCoreApplication.processEvents()
        print("on publis")
        self.ui.display_result.append(f"Published by {userdata['client']}, mid: {mid}")


    def disconnect(self):
        self.ui.display_result.append("Disconnected")
        self.ui.inputUserName.setDisabled(False)
        self.ui.inputPassword.setDisabled(False)
        self.ui.inputClientId.setDisabled(False)
        self.ui.inputTopicName.setDisabled(False)
        self.client.loop_stop()

    def listen(self):
        print("on lisn")
        try:
            qtc.QCoreApplication.processEvents()
            self.client.loop_start()
        except KeyboardInterrupt:
           # self.ui.display_result.append(f"Received KeyboardInterrupt, disconnecting {self.config.mqtt_client}")
            self.client.disconnect()