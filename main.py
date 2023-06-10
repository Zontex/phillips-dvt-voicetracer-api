import asyncio
import websockets
import json

#######################################
#
# Philips VoiceTracer DVT6110 API  
#
# Workng on WFi mode, device and script
# Need to work on the same network.
#                                  
# Currently Avalable features:     
#                                  
# [+] Download file
# [+] Get files list
# [+] Get device state
# [+] Get Settings
# [+] Get meta data
# [+] Start recording
# [+] Stop recording
#
######################################

class VoiceTracer():

    def __init__(self, address="0.0.0.0", port=81):
        self.address = "%s:%s" % (address,port)

    async def download_file(self,file_name="/C/VOICE/A/230523_232451_00.mp3"):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
            
                # Prepare the request message
                payload = {
                    "DownloadFile": {
                        "path": file_name,
                        "buffersize": "1024"
                    }
                }

                # Send a WebSocket message
                await websocket.send(json.dumps(payload))

                # Receive a chunk of data from the WebSocket
                data = await websocket.recv()
                if("42" in data):
                    # handshake, good sign
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        # Open a file to write the downloaded data
                        with open(file_name.replace("/C/VOICE/A/",""), 'wb') as file:
                            while True:
                                # Receive a chunk of data from the WebSocket
                                data = await websocket.recv()
                                # Check if the data is the end of the file
                                if data == "P":
                                    break
                                # Write the received data to the file
                                file.write(data)
                        return True
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()
                exit()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')

    async def get_files_list(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('GetFileList')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None
        
    async def get_device_state(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('GetDeviceState')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None
        
    async def get_settings(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('GetSettings')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None
        
    async def get_serial_number(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('GetSerialNumber')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None

    async def get_meta_data(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('GetMetaData')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None
        
    async def start_recording(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('StartRec')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None
        
    async def stop_recording(self):
        try:
            async with websockets.connect('ws://%s/' % self.address) as websocket:
                # Send a WebSocket message
                await websocket.send('StopRec')
                # Receive a WebSocket message
                response = await websocket.recv()
                if("42" in response):
                    # handshake successful
                    data = await websocket.recv()
                    if("timeFromPVT" in data):
                        # we can proceed now
                        response = json.loads(await websocket.recv())
                        return json.dumps(response)
                else:
                    print("[-] Handshake failed....")
                    return None
                # Close the WebSocket connection
                await websocket.close()

        except websockets.exceptions.ConnectionClosedError:
            print('WebSocket connection closed unexpectedly.')
            return None

if __name__ == "__main__":
    # Run the WebSocket request
    recorder = VoiceTracer()
    response = asyncio.get_event_loop().run_until_complete(recorder.get_files_list())
    print(response)
