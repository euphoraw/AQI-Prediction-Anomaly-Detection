import serial
import time
from azure.iot.device import IoTHubDeviceClient, Message


CONNECTION_STRING = "HostName=iotc-05a4a17e-e76d-41f2-96fe-bfe6865dbff8.azure-devices.net;DeviceId=240fmqjcgdr;SharedAccessKey=3V2P1KCrTJOYhtRVLga4spAgOMY9ftw6QJAxDSHo48I="

# Setup serial communication with Arduino
ser = serial.Serial('COM5', 9600)  

# Create IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("Connected to Azure IoT Central. Sending data...")

while True:
    try:
        if ser.in_waiting > 0:
            sensor_data = ser.readline().decode().strip()
            print(f"Read from Arduino: {sensor_data}")

            # Remove label text and extract just the numeric value
            clean_value = sensor_data.replace("Sensor Value: ", "")
            telemetry = {"airquality": int(clean_value)}

            # Send the telemetry to IoT Central
            message = Message(str(telemetry))
            client.send_message(message)
            print("Telemetry sent to Azure:", telemetry)

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        break
