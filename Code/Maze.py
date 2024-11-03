from time import sleep
from droneblocks import DroneBlocks

# Connect to the Tello drone
drone = DroneBlocks()

# Function to navigate the drone through the maze
def navigate_maze():
    # Take off
    drone.takeoff()

    # Move the drone forward
    drone.move_forward(100)  # Adjust the distance as needed
    sleep(1)  # Add a delay to allow the drone to complete the movement

    # Turn the drone left
    drone.rotate_counter_clockwise(90)  # Adjust the angle as needed
    sleep(1)  # Add a delay to allow the drone to complete the movement

    # Move the drone forward
    drone.move_forward(100)  # Adjust the distance as needed
    sleep(1)  # Add a delay to allow the drone to complete the movement

    # Turn the drone right
    drone.rotate_clockwise(90)  # Adjust the angle as needed
    sleep(1)  # Add a delay to allow the drone to complete the movement

    # Move the drone forward
    drone.move_forward(100)  # Adjust the distance as needed
    sleep(1)  # Add a delay to allow the drone to complete the movement

    # Land the drone
    drone.land()
    sleep(1)  # Add a delay to allow the drone to land

# Main program
if __name__ == '__main__':
    # Start navigating the maze
    navigate_maze()


#Conditional loop not possible as students will have to import OpenCV library for frame capture

#We can add bonus points whoever completes the maze fastest 5 times does min. 10 flips during the challenge
