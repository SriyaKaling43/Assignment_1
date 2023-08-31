import asyncio
import websockets
import json

async def send_message():
    async with websockets.connect("ws://68.183.95.2:5000/api/messages") as websocket:
        data = {'message': 'hello'}
        await websocket.send(json.dumps(data))  # Serialize the dictionary to JSON
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(send_message())
