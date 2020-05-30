from spike import MotorPair
import math

# If the left motor is connected to Port B
# And the right motor is connected to Port A.
motor_pair = MotorPair('B', 'A')

# amount, unit, steering (-100,100)), speed (-100 to 100)
motor_pair.move(10, 'cm', speed=50)

motor_pair.move(10, 'cm', speed=50, steering=50)

# turn a Driving Base 180 degrees in place (if wheels are 8.1 cm apart)
#motor_pair.move(8.1 * math.pi / 2, 'cm', steering=100)
