import asyncio
import websockets
import cv2
import numpy as np
import base64

async def receive_video():
    uri = "ws://13.60.222.225:8765"
    
    print(f"Connecting to WebSocket server at {uri}...")
    
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server.")
        
        while True:
            try:
                # Receive base64-encoded frame from the server
                print("Waiting for frame data...")
                base64_frame = await websocket.recv()
                
                print("Frame data received, decoding...")
                
                # Decode the base64 frame to raw data
                frame_data = base64.b64decode(base64_frame)
                
                # Convert the data to a numpy array and decode it to an image
                np_data = np.frombuffer(frame_data, np.uint8)
                frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
                
                # Display the video frame
                if frame is not None:
                    print("Displaying video frame...")
                    cv2.imshow("Received Video", frame)
                else:
                    print("Error: Frame is None")
                
                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("Exit command received. Closing video.")
                    break
                
            except websockets.exceptions.ConnectionClosedError:
                print("Connection to server closed.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break
    
    cv2.destroyAllWindows()
    print("WebSocket connection closed. Exiting program.")

if __name__ == "__main__":
    print("Starting video receiver...")
    asyncio.run(receive_video())
