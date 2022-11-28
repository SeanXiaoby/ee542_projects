from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json
import os

deploy = False


class MQTT:
    cwd = os.path.dirname(__file__)
    ENDPOINT = "a3v69j4ddfmor2-ats.iot.us-west-2.amazonaws.com"
    CLIENT_ID = "iotconsole-1668997266468-1"
    PATH_TO_CERTIFICATE = "/home/ubuntu/final/certificate.pem.crt" if deploy else cwd+"/certificate.pem.crt"
    PATH_TO_PRIVATE_KEY = "/home/ubuntu/final/private.pem.key" if deploy else cwd+"/private.pem.key"
    PATH_TO_AMAZON_ROOT_CA_1 = "/home/ubuntu/final/AmazonRootCA1.pem" if deploy else cwd+"/AmazonRootCA1.pem"
    TOPIC = "toMQTT"

    # Spin up resources
    def __init__(self):
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        self.mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=self.ENDPOINT,
            cert_filepath=self.PATH_TO_CERTIFICATE,
            pri_key_filepath=self.PATH_TO_PRIVATE_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=self.PATH_TO_AMAZON_ROOT_CA_1,
            client_id=self.CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
        )

        print("Connecting to {} with client ID '{}'...".format(self.ENDPOINT, self.CLIENT_ID))
        # Make the connect() call
        connect_future = self.mqtt_connection.connect()
        # Future.result() waits until a result is available
        connect_future.result()
        print("Connected!")

    def push_message(self, info):
        # Publish message to server desired number of times.
        print('Begin Publish')
        data = "{}".format(info)
        message = {"message": data}
        self.mqtt_connection.publish(topic=self.TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
        print("Published: '" + json.dumps(message) + "' to the topic: " + self.TOPIC)
        t.sleep(0.1)
        print('Publish End')

    def disconnect(self):
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()
