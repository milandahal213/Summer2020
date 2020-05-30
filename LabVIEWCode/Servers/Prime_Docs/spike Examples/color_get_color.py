from spike import ColorSensor

# Initialize the Color Sensor.
paper_scanner = ColorSensor('E')

# Measure the color.
color = paper_scanner.get_color()

# Print the color name to the console
print('Detected:', color)

# Check if it is a specific color
# Values: 'black','violet','blue','cyan','green','yellow','red','white', None
if color == 'red':
    print('It is red!')
elif color == 'white':
    print('It is white!')