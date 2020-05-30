from spike import Motor

motor = Motor('A')

# Run clockwise for half a second at 75% speed
motor.run_for_seconds(0.5, 75)

# Run counterclockwise for 6 seconds at 30% speed
motor.run_for_seconds(6, -30)

# Run the motor 90 degrees clockwise:
#motor.run_for_rotations(0.25)

# Run the motor 90 degrees counterclockwise:
#motor.run_for_rotations(-0.25)

# Set the motor to position 0, aligning the markers
#motor.run_to_position(0)

# Run the motor 90 degrees clockwise
#motor.run_for_degrees(90)

# Run the motor 90 degrees counterclockwise
#motor.run_for_degrees(-90)

# Run the motor 360 degrees clockwise, at maximum speed (100%)
#motor.run_for_degrees(360, 100)
