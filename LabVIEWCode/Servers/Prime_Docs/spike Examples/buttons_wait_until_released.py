from spike import PrimeHub

hub = PrimeHub()

# Is the left button pressed?

while True:
    hub.left_button.wait_until_pressed()
    print("Left Button Pressed")
    hub.right_button.wait_until_released()
    print("Left Button Released")
