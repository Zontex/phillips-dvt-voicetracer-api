# phillips-dvt-voicetracer-api

The DVT6110 has a WiFi mode integration built in that allows the "VoiceTracer" app to connect to it over the same network.
By enabling the wifi mode and knowing the IP of the device, you can also find out the IP using the hostname "dvt.local" that is normally assigned to the DVT6110 device.

The API uses websockets to communicate with the DVT device, no encryption or secret keys are needed.

## Features

The API currently supports:
- [x] Find IP by hostname
- [x] Download file
- [x] Get files list
- [x] Get device state
- [x] Get Settings
- [x] Get meta data
- [x] Start recording
- [x] Stop recording

This to be added
- [x] Delete file
- [x] Others...

## Purpose of the API

The VoiceTracer app is great but it lacks a lot of features and integrations. For example, when using the App I want to get current coordinates where the recording was made.
Also, I don't want to save it on the phone only but to upload the recording to the cloud for analysis. 
Another feature is to annotate in real time (voice to text).
All those are currently not supported by the app and need to be externally added which is why I created this API.

## Security concerns

It's not recommended to connect the DVT to public WiFi or any other access point than your own. 
It's recommended to create a hotspot on your mobile phone and connect it directly to it.
By connecting the device to public network, anyone with the right tools can pull the recordings, record voice remotely and delete your pre-existing files.
