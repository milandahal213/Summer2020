from spike import DistanceSensor

distance_sensor = DistanceSensor('A')

while True:
    distance_sensor.wait_for_distance_farther_than(20, 'cm')
    print("It's too far")
    distance_sensor.wait_for_distance_closer_than(20, 'cm')
    print("It's near me")
