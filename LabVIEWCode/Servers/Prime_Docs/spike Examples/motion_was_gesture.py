from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

while True:
    wait_for_seconds(1)
    # Values: 'shaken','tapped','doubletapped','falling','None'
    if hub.motion_sensor.was_gesture('shaken'):
        print("Stop shaking me!")
    elif hub.motion_sensor.was_gesture('falling'):
        print("Free falling, free falling")
    elif hub.motion_sensor.was_gesture('tapped'):
        print("What do you want?")
    else:
        print("Zzzz")