import asyncio
import websockets

async def receive_message():
    async with websockets.connect("ws://68.183.95.2:5000/api/messages") as websocket:
        response = await websocket.recv()
        print(f"Received message from server: {response}")

asyncio.get_event_loop().run_until_complete(receive_message())
