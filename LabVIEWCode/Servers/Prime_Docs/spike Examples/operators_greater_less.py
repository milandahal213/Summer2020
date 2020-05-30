from spike import ColorSensor
from spike.control import wait_until

# greater_than, greater_than_or_equal_to, less_than, less_than_of_equal_to, equal_to, not_equal_to
from spike.operator import greater_than

color_sensor = ColorSensor('E')

print("Waiting")

wait_until(color_sensor.get_reflected_light, greater_than, 50)
print("Yay! Enough light!")