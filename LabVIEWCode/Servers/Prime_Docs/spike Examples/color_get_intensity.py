from spike import ColorSensor
from spike.control import wait_for_seconds

# Initialize the Color Sensor.
paper_scanner = ColorSensor('E')

while True:
    # Measure the intensity.
    red = paper_scanner.get_red()
    green = paper_scanner.get_green()
    blue = paper_scanner.get_blue()
    # Print the color name to the console
    print('Red intensity', red)
    print('Green intensity', green)
    print('Blue intensity', blue)
    wait_for_seconds(2)