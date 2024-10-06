import paho.mqtt.client as mqtt

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        # Subscribe to a topic once connected
        client.subscribe("topic1")
    else:
        print("Connection failed with code ", rc)

def on_message(client, userdata, msg):
    # Callback for when a message is received
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to HiveMQ public broker
hivemq_broker = "broker.hivemq.com"
client.connect(hivemq_broker, 1883, 60)

# Start the network loop
client.loop_forever()
