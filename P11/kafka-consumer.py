from confluent_kafka import Consumer
import json
import sqlite3
import datetime


conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (timestamp DATETIME, CO REAL, NO2 REAL, Ethanol REAL, Hydrogen REAL, Ammonia REAL)''')
conn.commit()

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

config = read_config()
config = read_config()
topic = "data"
# sets the consumer group ID and offset  
config["group.id"] = "python-group-1"
config["auto.offset.reset"] = "earliest"
# creates a new consumer and subscribes to your topic
consumer = Consumer(config)
consumer.subscribe([topic])

try:
  while True:
    # consumer polls the topic and prints any incoming messages
    msg = consumer.poll(1.0)
    if msg is not None and msg.error() is None:
        value = msg.value().decode("utf-8")
        print(f"Consumed message from topic {topic} value = {value:12}")
        msg_data = json.loads(value)
        # insert the data into the database
        CO = msg_data['CO']
        NO2 = msg_data['NO2']
        Ethanol = msg_data['Ethanol']
        Hydrogen = msg_data['Hydrogen']
        Ammonia = msg_data['Ammonia']
        # get the current time  
        dateTime = datetime.datetime.now()

        # Use placeholders in the SQL query
        c.execute("INSERT INTO sensor_data (timestamp, CO, NO2, Ethanol, Hydrogen, Ammonia) VALUES (?, ?, ?, ?, ?, ?)",
                  (dateTime, CO, NO2, Ethanol, Hydrogen, Ammonia))
        conn.commit()
        print(c.fetchall())
except KeyboardInterrupt:
  pass
finally:
  # closes the consumer connection
  consumer.close()

