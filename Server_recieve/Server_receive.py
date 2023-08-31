import asyncio
import websockets

async def receive_message(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send("Message received!")

start_server = websockets.serve(receive_message, "0.0.0.0", 5000)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
