from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

# Values: 'azure', 'black','blue','cyan','green','orange','pink','red','violet','yellow','white'
hub.status_light.on('azure')
wait_for_seconds(1)
hub.status_light.on('cyan')
wait_for_seconds(1)
hub.status_light.on('orange')
wait_for_seconds(1)

hub.status_light.off()