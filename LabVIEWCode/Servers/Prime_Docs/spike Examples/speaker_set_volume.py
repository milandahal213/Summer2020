from spike import PrimeHub

hub = PrimeHub()

# set the volume of the Hub speaker to 50%
hub.speaker.set_volume(50)

# MIDI C D E F G A B C
# 60 62 64 65 67 69 71 72
hub.speaker.beep(60, 0.5)
hub.speaker.beep(62, 0.5)
hub.speaker.beep(64, 0.5)
hub.speaker.beep(65, 0.5)
hub.speaker.beep(67, 0.5)
hub.speaker.beep(69, 0.5)
hub.speaker.beep(71, 0.5)
hub.speaker.beep(72, 0.5)