from spike import ForceSensor

# Initialize the Force Sensor.
door_bell = ForceSensor('E')

while True:
    # Check if the Force Sensor is pressed
    if door_bell.is_pressed():
        print('Hello!')
    else: 
        print('Waiting')
