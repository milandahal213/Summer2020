from spike import DistanceSensor

# Initialize the Distance Sensor.

wall_detector = DistanceSensor('A')

while True:
    # Measure the distances between the Distance Sensor and and object in centimeters or inches.
    dist_cm = wall_detector.get_distance_cm()
    dist_inches = wall_detector.get_distance_inches()

    # Print both results to the console
    print('cm:', dist_cm, 'Inches:', dist_inches)
