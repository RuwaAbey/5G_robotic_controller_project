import asyncio
import websockets

clients = set()

async def relay_video(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message (video frame) to all clients except the sender
            for client in clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        clients.remove(websocket)

async def main():
    # Start the WebSocket server on all interfaces, port 8765
    server = await websockets.serve(relay_video, "0.0.0.0", 8765)
    print("Server is running on port 8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
