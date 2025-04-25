import asyncio
import websockets

async def handle_client(websocket, path):
    print("Client connected")
    async for message in websocket:
        print("Received from client:", message)
        # Now publish to MQTT
        import os
        os.system(f'mosquitto_pub -t "light/schedule" -m "{message}"')

async def main():
    async with websockets.serve(handle_client, "localhost", 6789):
        print("WebSocket server started on ws://localhost:6789")
        await asyncio.Future()  # Keeps it running forever

if __name__ == "__main__":
    asyncio.run(main())