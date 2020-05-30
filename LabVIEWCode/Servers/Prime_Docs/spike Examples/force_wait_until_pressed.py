from spike import ForceSensor

force_sensor = ForceSensor('E')

while True:
    force_sensor.wait_until_pressed()
    print("Pressed")
    force_sensor.wait_until_released()
    print("Released")
