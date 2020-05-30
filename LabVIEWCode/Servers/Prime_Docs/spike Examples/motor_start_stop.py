from spike import Motor
from spike import PrimeHub

hub = PrimeHub()
motor = Motor('A')

# Start the motor
motor.start()

# Wait until left button is pressed 
hub.left_button.wait_until_pressed()
print("Left button pressed")

# Stop the motor
motor.stop()