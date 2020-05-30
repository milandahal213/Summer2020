from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
wait_for_seconds(5)
hub.light_matrix.show_image('ASLEEP')
wait_for_seconds(5)
