from spike import ColorSensor
from spike.control import wait_until
from spike.operator import equal_to

color_sensor = ColorSensor('E')

print("Waiting")

# wait for the Color Sensor to detect red
wait_until(color_sensor.get_color, equal_to, 'red')

print("Yay! Found Red")

