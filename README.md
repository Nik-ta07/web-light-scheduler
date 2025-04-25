# web-light-scheduler

# 🌐 Web-Based IoT Light Scheduler

Control your Arduino-powered light using a simple web dashboard!

## 🧠 Tech Stack
- HTML/CSS/JS
- Python (websockets, MQTT, serial)
- Mosquitto MQTT broker
- Arduino UNO

## 📦 Features
- Graphical UI to set light schedule
- WebSocket to MQTT communication
- Real-time light control via Arduino

## 🚀 How to Use
1. Upload Arduino code
2. Start Mosquitto broker
3. Run Python WebSocket server
4. Run MQTT Subscriber
5. Open `index.html` and submit times

## 🛠 Sample Payload
```json
{
  "on": "18:00",
  "off": "22:00"
}
