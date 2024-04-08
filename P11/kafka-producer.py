import paho.mqtt.client as paho
from paho import mqtt
from confluent_kafka import Producer
import json
import os
from dotenv import load_dotenv

# MQTT Configuration
load_dotenv()

# MQTT Broker settings
broker_address = os.getenv("BROKER_ADDRESS")
print(broker_address)
port = 8883
mqtt_topic = "data/sensor1"
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")

def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

# MQTT on_connect callback
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"CONNACK received with code {reason_code}")
    client.subscribe(mqtt_topic, qos=1)

# MQTT on_message callback
def on_message(client, userdata, msg):
    try:
        if msg.payload is None:
            print(f"Received empty message from topic {msg.topic}")
            return
        msg = msg.payload.decode()
        msg = msg.encode('utf-8')
        producer.produce('data', key=None, value=msg)
        print(f"Produced message to topic {topic}: value = {msg.decode('utf-8')}")
        producer.flush()
    except Exception as e:
        print("Error:", e)

# Kafka delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Initialize Kafka Producer
config = read_config()
topic = "data"
producer = Producer(config)

# Initialize MQTT Client
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Subscriber",
                     protocol=paho.MQTTv5)
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)
client.on_message = on_message
client.connect(broker_address, port, 60)

# Subscribe to the topic
client.subscribe(mqtt_topic)

try:
    print(f"Subscribed to topic {mqtt_topic}")
    client.loop_forever()
except KeyboardInterrupt:
    # Gracefully handle interrupt (Ctrl+C) to disconnect from MQTT broker
    client.disconnect()
    print("\nSubscriber stopped.")
