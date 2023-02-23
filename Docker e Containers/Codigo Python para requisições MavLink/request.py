import requests
import time
import pymavlink.mavutil as mavutil


# TODO FIX I!

URL_FAST_API = 'http://localhost:8000/'


try:
    # Replace <API_KEY> with your Google API key
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=<API_KEY>"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:

        #! Use the pymavlink library to move the servo

        # Connect to the drone using a serial connection
        master = mavutil.mavlink_connection('/dev/ttyACM0', baud=57600)

        # Wait for the drone to initialize
        master.wait_heartbeat()

        # Move the servo to position 1000
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,
            1,
            1000,
            0,
            0,
            0,
            0,
            0
        )

        # Wait for the command to complete
        time.sleep(1)

        # Move the servo back to position 2000
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
            0,
            1,
            2000,
            0,
            0,
            0,
            0,
            0
        )

    else:
        # Handle the error
        print("Request failed with status code: ", response.status_code)


except:
    print('Erro na requisição')
