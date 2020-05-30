from spike import PrimeHub

hub = PrimeHub()

hub.left_button.wait_until_pressed()
print("Left button pressed")
hub.speaker.beep()

hub.right_button.wait_until_pressed()
print("Right button pressed")
hub.status_light.on('blue')