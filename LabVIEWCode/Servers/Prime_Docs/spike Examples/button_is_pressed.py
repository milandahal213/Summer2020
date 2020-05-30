from spike import PrimeHub

hub = PrimeHub()

while True:
    if hub.left_button.is_pressed():
        print("Left button is Pressed")
    elif hub.right_button.is_pressed():
        print("Right button is Pressed")
