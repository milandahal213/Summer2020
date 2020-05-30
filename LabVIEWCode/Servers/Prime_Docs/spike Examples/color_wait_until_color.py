from spike import ColorSensor
from spike.control import wait_for_seconds

# Initialize the Color Sensor.
color_sensor = ColorSensor('E')

while True:
    color_sensor.wait_until_color('red')
    print("Red object found")
