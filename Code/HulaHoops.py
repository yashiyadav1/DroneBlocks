from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

# Connect to the Tello drone
drone = DroneBlocksTello()

# Take off
drone.takeoff()
time.sleep(1)  # Add a delay to allow the drone to take off

# Move the drone through the first hula hoop
drone.move_forward(50)  # Adjust the distance as needed
time.sleep(1)  # Add a delay to allow the drone to complete the movement

# Turn the drone around
drone.rotate_clockwise(180)  # Adjust the angle as needed
time.sleep(1)  # Add a delay to allow the drone to complete the movement

# Move the drone through the second hula hoop
drone.move_forward(50)  # Adjust the distance as needed
time.sleep(1)  # Add a delay to allow the drone to complete the movement

# Land the drone
drone.land()
time.sleep(1)  # Add a delay to allow the drone to land

