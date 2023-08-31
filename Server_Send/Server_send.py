import asyncio
import websockets

async def send_message(websocket, path):
    message = "Hello from server!"
    await websocket.send(message)

start_server = websockets.serve(send_message, "0.0.0.0", 5000)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
