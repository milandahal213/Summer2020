from spike import PrimeHub

hub = PrimeHub()

hub.light_matrix.write('Hello!')

# Show the number 1 on the Light Matrix
hub.light_matrix.write('1')