import time
import pymavlink.mavutil as mavutil

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
