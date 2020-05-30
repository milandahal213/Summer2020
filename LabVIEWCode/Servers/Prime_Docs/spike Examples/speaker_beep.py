from spike import PrimeHub

hub = PrimeHub()

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

# Mission Impossible!
# MIDI G = 67
# G G Bb C G G F F# 
for i in range(3):
    hub.speaker.beep(67, 0.5)
    hub.speaker.beep(67, 0.5)
    hub.speaker.beep(70, 0.25)
    hub.speaker.beep(72, 0.25)
    hub.speaker.beep(67, 0.5)
    hub.speaker.beep(67, 0.5)
    hub.speaker.beep(65, 0.25)
    hub.speaker.beep(66, 0.25)
