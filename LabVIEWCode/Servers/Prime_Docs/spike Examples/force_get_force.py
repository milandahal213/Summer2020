from spike import ForceSensor

# Initialize the Force Sensor.
door_bell = ForceSensor('E')

while True:
    # Measure the force in newtons or as a percentage.
    newtons = door_bell.get_force_newton()
    percentage = door_bell.get_force_percentage()

    # Print both results
    print('N:', newtons, '=', percentage, '%')
