# Racing Game with Countdown Timer - DroneBlocks

from time import sleep
from droneblocks import DroneBlocks

# Define variables
lap_count = int(input("Enter the number of laps for the race: "))
altitude = float(input("Enter the desired altitude (in meters): "))
speed = float(input("Enter the desired speed (in meters per second): "))

# Connect to the drone
drone = DroneBlocks()

# Takeoff
drone.takeoff()

# Ascend to the defined altitude
drone.ascend(altitude)

# Start the race loop
for lap in range(1, lap_count + 1):
    print("Lap", lap)

    # Countdown timer
    for countdown in range(3, 0, -1):
        print(countdown)
        sleep(1)

    # Fly forward for a lap
    drone.fly_forward(speed, 30)  # Assuming 30 seconds per lap

    # Perform a flip
    drone.flip_forward()

# Descend back to the ground
drone.descend(altitude)

# Land
drone.land()

