from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import random

found_ids = []  # Array to store the found mission pad IDs

tello = DroneBlocksTello()

tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)
tello.clear_display()
tello.set_top_led(r=255, g=0, b=0)

tello.takeoff()
time.sleep(2)  # Wait for 2 seconds after takeoff

dist = 250

while True:
    tello.flip_forward(10,'cm')
    id = tello.get_mission_pad_id()
    if 1 <= id <= 8:
        print(f"Mission Pad {id} found!" )
        break
    if tello.get_distance_tof() > dist:
        break