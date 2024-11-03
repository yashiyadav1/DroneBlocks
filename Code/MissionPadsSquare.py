from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import logging

tello = DroneBlocksTello()
#tello.LOGGER.setLevel(logging.INFO)
tello.connect()
tello.enable_mission_pads()

print("Initialize LED and Display")
tello.display_smile(display_color=tello.PURPLE)
tello.set_top_led(r=255, g=0, b=0)
time.sleep(1)

tello.takeoff()

time.sleep(2)

id = tello.get_mission_pad_id()
tello.display_character(id)
time.sleep(1)

for i in range(4):
    print(f"fly_forward {i+1}")
    tello.clear_display()
    tello.set_top_led(r=0, g=255, b=0)
    tello.fly_forward(30, 'in')
    tello.set_top_led(r=255, g=0, b=0)
    id = tello.get_mission_pad_id()
    tello.display_character(id)

    time.sleep(1)
    tello.rotate_counter_clockwise(90)
    time.sleep(1)

time.sleep(2)

tello.clear_everything()
time.sleep(1)

tello.land()
