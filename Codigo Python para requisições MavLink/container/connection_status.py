import requests
from pymavlink import mavutil

# Setando os parametros
url = "https://maps.googleapis.com/maps/api/geocode/json"
params = {'address': '1600 Amphitheatre Parkway, Mountain View, CA'}
response = requests.get(url, params=params)

if response.status_code == 200:
    # Request was successful
    data = response.json()
    print('Works = ', data)
    # Do something with the response data
    is_connected = True
else:
    # Request failed
    print("Error:", response.status_code)
    is_connected = False


#! Código Mavlink

# Create a pymavlink connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

# Send a message to the autopilot to indicate connection status
if is_connected:
    master.mav.heartbeat_send(
        mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
else:
    master.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,
                              mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, mavutil.mavlink.MAV_STATE_CRITICAL)
