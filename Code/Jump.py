from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import logging

image_string = "p000000p0p0000p000pbbp0000bppb0000brrb0000rbbr000r0000r0r000000r"

tello = DroneBlocksTello()

tello.LOGGER.setLevel(logging.INFO)

tello.enable_mission_pads()

print("Initialize LED and Display")
tello.display_smile(display_color=tello.PURPLE)
tello.set_top_led(r=255, g=0, b=0)
time.sleep(3)

tello.takeoff()

time.sleep(2)

mid = tello.get_mission_pad_id()
tello.display_character(mid)
time.sleep(1)

for i in range(1, 3):  
    print(f"GO Trip {i} !!!!!!!!!!!!!!!!!!!!!!!!!")

    # Legs of journey
    for x, mid1, mid2 in [(125, 4, 2), (150, 2, 5), (125, 5, 3), (150, 3, 4)]:
        print(f"GO {mid1} -> {mid2}")
        tello.display_image(image_string)
        tello.set_top_led(r=0, g=255, b=0)
        time.sleep(2)
        tello.go_xyz_speed_yaw_mid(x=x, y=0, z=60, speed=30, yaw=0, mid1=mid1, mid2=mid2)
        print(f"DONE {mid1} -> {mid2}")
        tello.set_top_led(r=255, g=0, b=0)
        mid = tello.get_mission_pad_id()
        tello.display_character(mid)
        time.sleep(1)

time.sleep(1)
tello.land()
