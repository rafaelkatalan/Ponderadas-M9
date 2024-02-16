import time
import random
import paho.mqtt.client as mqtt

# MQTT Broker settings
broker_address = "localhost"
port = 1891
topic = "data/sensor1"

# Function to simulate sensor readings
def generate_sensor_data():
    co_reading = random.uniform(1, 1000)
    no2_reading = random.uniform(0.05, 10)
    ethanol_reading = random.uniform(10, 500)
    hydrogen_reading = random.uniform(1, 1000)
    ammonia_reading = random.uniform(1, 500)

    return {
        "CO": co_reading,
        "NO2": no2_reading,
        "Ethanol": ethanol_reading,
        "Hydrogen": hydrogen_reading,
        "Ammonia": ammonia_reading
    }

# Function to publish sensor data to MQTT
def publish_sensor_data(client):
    while True:
        sensor_data = generate_sensor_data()
        client.publish(topic, str(sensor_data))
        print(f"Published: {sensor_data}")
        time.sleep(5)  # Adjust the interval as needed

# MQTT setup and connection
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker_address, port, 60)

try:
    # Start the simulation
    publish_sensor_data(client)
except KeyboardInterrupt:
    # Gracefully handle interrupt (Ctrl+C) to disconnect from MQTT broker
    client.disconnect()
    print("Simulation stopped.")
