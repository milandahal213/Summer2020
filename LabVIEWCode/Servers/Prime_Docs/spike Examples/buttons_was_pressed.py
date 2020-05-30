from spike import PrimeHub

hub = PrimeHub()

while True:
    if hub.left_button.was_pressed():
        print("Left button was Pressed")
    elif hub.right_button.was_pressed():
        print("Right button was Pressed")
