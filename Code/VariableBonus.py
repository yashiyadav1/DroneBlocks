# Variable Challenge - DroneBlocks

from time import sleep
from droneblocks.DroneBlocksTello import DroneBlocks

# Prompt user for input
altitude = float(input("Enter desired altitude (in meters): "))
speed = float(input("Enter desired speed (in meters per second): "))
duration = float(input("Enter desired duration (in seconds): "))

# Connect to the drone
drone = DroneBlocks()

# Takeoff
drone.takeoff()

# Ascend to the defined altitude
drone.ascend(altitude)

# Fly forward at the defined speed for the defined duration
drone.fly_forward(speed, duration)

# Perform a left turn
drone.turn_left()

# Descend back to the ground
drone.descend(altitude)

# Land
drone.land()

