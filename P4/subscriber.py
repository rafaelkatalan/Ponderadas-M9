import paho.mqtt.client as paho
from paho import mqtt
from dotenv import load_dotenv
import os

load_dotenv()

# MQTT Broker settings
broker_address = os.getenv("BROKER_ADDRESS")
port = 8883
topic = "data/sensor1"
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"CONNACK received with code {reason_code}")
    client.subscribe(topic, qos=1)

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# MQTT setup and connection
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Subscriber",
                     protocol=paho.MQTTv5)
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)
client.on_message = on_message
client.connect(broker_address, port, 60)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT loop to receive messages
try:
    print(f"Subscribed to topic {topic}")
    client.loop_forever()
except KeyboardInterrupt:
    # Gracefully handle interrupt (Ctrl+C) to disconnect from MQTT broker
    client.disconnect()
    print("\nSubscriber stopped.")
