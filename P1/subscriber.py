import paho.mqtt.client as mqtt

# MQTT Broker settings
broker_address = "localhost"
port = 1891
topic = "data/sensor1"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# MQTT setup and connection
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
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
