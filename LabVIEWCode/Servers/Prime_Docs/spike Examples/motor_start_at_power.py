from spike import Motor
from spike import PrimeHub

hub = PrimeHub()
motor = Motor('A')

# Start the motor at 30% power
motor.start_at_power(30)

# Wait until left button is pressed 
hub.left_button.wait_until_pressed()
print("Left button pressed")

# Stop the motor
motor.stop()