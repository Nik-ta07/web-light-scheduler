import serial
import paho.mqtt.client as mqtt

arduino = serial.Serial('COM4', 9600, timeout=1)  

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received from MQTT: {message}")
    if message in ['1', '0']:
        arduino.write(message.encode())

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("light/schedule")
client.on_message = on_message
print("Subscribed to MQTT topic: light/schedule")

client.loop_forever()
