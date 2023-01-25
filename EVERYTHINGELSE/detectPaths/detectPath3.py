
from dronekit import connect, VehicleMode
from time import sleep
from pymavlink import mavutil

point1Second = (1130, 1413)
point2Second = (537, 1297)
height, width = 2160, 3840


def sendCommand(velocity_x, velocity_y, velocity_z, duration):
    global vehicle
    msg = vehicle.message_factory.set_position_target_global_int_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, # lat_int - X Position in WGS84 frame in 1e7 * meters
        0, # lon_int - Y Position in WGS84 frame in 1e7 * meters
        0, # alt - Altitude in meters in AMSL altitude(not WGS84 if absolute or relative)
        # altitude above terrain if GLOBAL_TERRAIN_ALT_INT
        velocity_x, # X velocity in NED frame in m/s
        velocity_y, # Y velocity in NED frame in m/s
        velocity_z, # Z velocity in NED frame in m/s
        0, 0, 0, # afx, afy, afz acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)

    for x in range(0, duration):
        vehicle.send_mavlink(msg)
        sleep(0.001)
def takeOff(altitude = 5):
    while not vehicle.is_armable:
        sleep(0.5)
    vehicle.mode = VehicleMode("STABILIZE")
    vehicle.armed = True
    while not vehicle.armed:
        sleep(0.5)
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.simple_takeOff(altitude)
    while True:
        if vehicle.location.global_relative_frame.alt >= altitude * 0.95:
            break
        sleep(0.5)
