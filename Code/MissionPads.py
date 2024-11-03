from droneblocks.DroneBlocksTello import DroneBlocksTello
import time
import random

found_ids = []  # Array to store the found mission pad IDs

def init(drone, params):
    drone.enable_mission_pads()
    drone.set_mission_pad_detection_direction(0)
    drone.clear_display()
    drone.set_top_led(r=255, g=0, b=0)

def takeoff(drone):
    drone.takeoff()
    time.sleep(2)  # Wait for 2 seconds after takeoff

def handler(drone, frame, params):
    mid = drone.get_mission_pad_id()
    if 1 <= mid <= 8:
        # Then we have detected a mission pad
        drone.set_top_led(r=0, g=255, b=0)
        print(f"Mission Pad ID: {mid}")
        drone.display_character(mid)

        # Store the found ID in the array if not already present
        if mid not in found_ids:
            found_ids.append(mid)

        x = drone.get_mission_pad_distance_x()
        y = drone.get_mission_pad_distance_y()
        z = drone.get_mission_pad_distance_z()
        print(f"Distance: {x},{y},{z}")
        drone.land()  # Land the drone after detecting a mission pad

    else:
        drone.display_character("X")
        drone.set_top_led(r=255, g=0, b=0)

        # Move the drone in a random direction
        random_direction = random.choice(['up', 'down', 'left', 'right', 'rotate_left', 'rotate_right'])
        random_distance = random.randint(20, 50)  # Choose a random distance between 20 and 50 cm
        move_drone(drone, random_direction, random_distance)

def move_drone(drone, direction, distance):
    if direction == 'up':
        drone.move_up(distance)
    elif direction == 'down':
        drone.move_down(distance)
    elif direction == 'left':
        drone.move_left(distance)
    elif direction == 'right':
        drone.move_right(distance)
    elif direction == 'rotate_left':
        drone.rotate_counter_clockwise(45)  # Rotate 45 degrees left
    elif direction == 'rotate_right':
        drone.rotate_clockwise(45)  # Rotate 45 degrees right

    time.sleep(2)  # Pause for 2 seconds after each movement

def stop(drone, params):
    drone.display_smile()
    time.sleep(2)
    drone.clear_everything()

def main():
    drone = DroneBlocksTello()

    try:
        drone.set_speed(30)
        drone.streamon()

        params = None
        init(drone, params)
        takeoff(drone)  # Added drone takeoff

        while True:
            # Run the script handler for each frame received
            frame = drone.get_frame_read().frame
            handler(drone, frame, params)
            time.sleep(1 / 30)  # Sleep to limit the loop's frequency

    except KeyboardInterrupt:
        print("Keyboard Interrupt. Stopping the script...")
        stop(drone, params)
        drone.end()

    except Exception as e:
        print("Error occurred:", str(e))
        stop(drone, params)
        drone.end()

if __name__ == "__main__":
    main()
