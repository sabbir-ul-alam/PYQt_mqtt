
from Components.Services.Config import Config
from PyQt5 import  QtCore as qtc
from Components.Singals.process import on_message
from paho.mqtt.client import Client

class Signals(object):


    def __init__(self,ui,config: dict, message_processor=None):
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
        # displayResult.clear()
        # self.warning_label.clear()
        userName = "server31"
        password = "SP5WjUMnt1kF"
        clientId = "communicator-admin-03"
        topicName = "communicator/0/9bf5b73e-8f06-499d-bc9a-09fcc52febfc/call_events"
        try:
            # path=Config.saveConfigFile(userName.text(),password.text(),clientId.text(),topicName.text())
            path = Config.saveConfigFile( userName, password, clientId, topicName)
            config = Config.load_from(path)
            print(config)
            client = Signals(ui,config, message_processor=on_message)
            #ui.display_result.append("test print")
            client.listen()
        except:
            pass
    # def dis_client(self):
    #     self.client.disconnect()
    #     #self.client.loop_stop()
    #
    # def clearAndDisconnectSignal(*args):
    #     print("cear all")
    #     try:
    #      qtc.QCoreApplication.processEvents()
    #      ok=Signals.dis_client
    #

         # self.display_result.blockSignals(True)
         # self.display_result.blockSignals(False)

         # for arg in args:
         #    arg.clear()
         #self.enable_input()
        # except Exception as e:
        #     print(e)
           # self.enable_input()

    def _on_log(self, client, userdata, level, buf):
       #qtc.QCoreApplication.processEvents()
       print("on log")
       #self.ui.display_result.append(f"{buf}, origin: {userdata['client']}")
    def _on_connect(self, client, userdata, flags, rc):
        #qtc.QCoreApplication.processEvents()
        print("on connect")
        self.client.subscribe(self.config.mqtt_topics)
        self.ui.display_result.append(f"Connected {userdata['client']}, result code: {str(rc)} {str(flags)}")
        self.ui.display_result.append(f"Connected {userdata['client']}, result code: {str(rc)} {str(flags)}")
        self.ui.display_result.append(f"Subscribing to all topics...")

    def _on_subscribe(self, client, userdata, mid, granted_qos):
        #qtc.QCoreApplication.processEvents()
        print("on subscribe")
        self.ui.display_result.append(f"Subscribed {userdata['client']}, mid: {mid}, granted qos: {granted_qos}")
        self.ui.display_result.append(f"Listening for {userdata['client']} messages...")
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
    def listen(self):

        print("on listen")
        try:
            qtc.QCoreApplication.processEvents()
            self.client.loop_start()
        except KeyboardInterrupt:
           # self.ui.display_result.append(f"Received KeyboardInterrupt, disconnecting {self.config.mqtt_client}")
            self.client.disconnect()