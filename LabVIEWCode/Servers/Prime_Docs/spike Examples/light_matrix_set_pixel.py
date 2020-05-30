from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

hub.light_matrix.set_pixel(1, 0, 100)
wait_for_seconds(0.2)
hub.light_matrix.set_pixel(1, 1, 80)
wait_for_seconds(0.2)
hub.light_matrix.set_pixel(1, 2, 60)
wait_for_seconds(0.2)
hub.light_matrix.set_pixel(1, 3, 40)
wait_for_seconds(0.2)
hub.light_matrix.set_pixel(1, 4, 20)
wait_for_seconds(0.2)

# Turn off all pixels
#hub.light_matrix.off()