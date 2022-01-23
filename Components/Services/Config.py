import re
import json
from configparser import SafeConfigParser

class Config():
    def __init__(
            self,
            mqtt_host: str,
            mqtt_port: int,
            mqtt_username: str,
            mqtt_password: str,
            mqtt_client: str,
            mqtt_topics: list,
            mqtt_clean_session: bool,
            mqtt_debug: bool,
    ):
        print("config initialized")
        self.mqtt_host = mqtt_host
        self.mqtt_port = mqtt_port
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.mqtt_client = mqtt_client
        self.mqtt_topics = [(tt[0].strip(), int(tt[1].strip())) for tt in mqtt_topics]
        self.mqtt_clean_session = mqtt_clean_session
        self.mqtt_debug = mqtt_debug

    @classmethod
    def load_from(cls, filename: str):
        parser = SafeConfigParser()
        try:
            with open(filename, 'r',encoding="utf-8") as config_file:
                #print(config_file.readlines())
                parser.read_file(config_file)
                return cls(
                    parser["mqtt"]["mqtt_host"],
                    int(parser["mqtt"]["mqtt_port"]),
                    parser["mqtt"]["mqtt_username"],
                    parser["mqtt"]["mqtt_password"],
                    parser["mqtt"]["mqtt_client"],
                    [
                        tuple(tt.split(","))
                        for tt in re.findall(r"\(([^\)]+)\)", parser["mqtt"]["mqtt_topics"])
                        if tt and len(tt) > 0
                    ],
                    parser["mqtt"]["mqtt_clean_session"].lower() == "true",
                    parser["mqtt"]["mqtt_debug"].lower() == "true",
                )
        except KeyError as err:
            print("Missing configuration key")
            #displayResult.append(f"Missing configuration key: {str(err)}")
        except (IOError, OSError) as err:
            print("Error reading configuration file")
            #displayResult.append(f"Error reading configuration file. {str(err)}")

    def __repr__(self):
        return json.dumps(self.__dict__, indent=2, sort_keys=True)


    def saveConfigFile(userName: str,password, clientId, topicName):
        try:
            furl="config.cfg"
            with open(furl,"w") as file:

               line= ["[mqtt] \n",
                "mqtt_host = chat.onudaan.com \n",
                "mqtt_port = 1883 \n",
                "mqtt_username = {}\n".format(userName),
                "mqtt_password = {} \n".format(password),
                "mqtt_client = {} \n".format(clientId),
                "mqtt_topics = ({}, 1), \n".format(topicName),
                "mqtt_clean_session = false \n",
                "mqtt_debug = true" ]
               file.writelines(line)
               print("path")
               return furl
        except FileNotFoundError:
           print("File not found")
        except IOError:
            print("Erro while writing")
        except Exception as e:
            print(repr(e))



