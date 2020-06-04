#!/usr/bin/env pybricks-micropython

"""
This program includes standalone versions of the eight behaviors plus two additional walking behaviors:
walk_steps and walk_timed. It also includes standalone versions of Sit Down, Stand Up, Stretch, and Hop.

-------------------------------------------
This program requires LEGO® EV3 MicroPython
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-core
"""

"""
Start the puppy sitting down. 
Motors are named left_leg_motor, right_leg_motor, and head_motor.
"""
from random import randint 

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Button, Color, Direction
from pybricks.media.ev3dev import Image, ImageFile, SoundFile
from pybricks.tools import wait, StopWatch


ev3 = EV3Brick()
ev3.screen.clear()

left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
head_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[[1, 24], [12, 36]])

# must be called when puppy is sitting down.
left_leg_motor.reset_angle(0)
right_leg_motor.reset_angle(0)


def idle():
    """The puppy is idle."""
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(500)
    ev3.screen.show_image(ImageFile.NEUTRAL)
        

def go_to_sleep():
    """Makes the puppy go to sleep.""" 
    ev3.screen.show_image(ImageFile.TIRED_MIDDLE)
    #puppy sits down
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(1000)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(100)
    head_motor.run_target(20, -40)
    ev3.screen.show_image(ImageFile.SLEEPING)
    ev3.speaker.play_file(SoundFile.SNORING)
        

def wake_up():
    """Makes the puppy wake up."""
    ev3.screen.show_image(ImageFile.TIRED_MIDDLE)
    ev3.speaker.play_file(SoundFile.DOG_WHINE)
    head_motor.run_target(20, 0)
    #puppy sits down
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(1000)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(100)
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(500)
    #puppy stretches
    left_leg_motor.run_target(100, 125, wait=False)
    right_leg_motor.run_target(100, 125)
    ev3.speaker.play_file(SoundFile.DOG_WHINE)
    left_leg_motor.run_target(100, 125, wait=False)
    right_leg_motor.run_target(100, 125)
    wait(1000)
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    ev3.screen.show_image(ImageFile.NEUTRAL)
    

def act_playful():
    """Makes the puppy act playful."""
    playful_timer = StopWatch()
    playful_bark_interval = None
    ev3.screen.show_image(ImageFile.NEUTRAL)
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    playful_bark_interval = 0
    if playful_timer.time() > playful_bark_interval:
        ev3.speaker.play_file(SoundFile.DOG_BARK_2)
        playful_timer.reset()
        playful_bark_interval = randint(4, 8) * 1000


def act_angry():
    """Makes the puppy act angry."""
    ev3.screen.show_image(ImageFile.ANGRY)
    ev3.speaker.play_file(SoundFile.DOG_GROWL)
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(1500)
    ev3.speaker.play_file(SoundFile.DOG_BARK_1)
    

def act_hungry():
    """Makes the puppy act hungry."""
    #Replaced HURT eyes with AWAKE
    ev3.screen.show_image(ImageFile.AWAKE)
    #puppy sits down
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(1000)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(100)
    ev3.speaker.play_file(SoundFile.DOG_WHINE)


def go_to_bathroom():
    """Makes the puppy go to the bathroom."""
    ev3.screen.show_image(ImageFile.PINCHED_MIDDLE)
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(100)
    right_leg_motor.run_target(100, 125)
    wait(800)
    ev3.speaker.play_file(SoundFile.HORN_1)
    wait(1000)
    for _ in range(3):
        right_leg_motor.run_angle(100, 20)
        right_leg_motor.run_angle(100, -20)
    right_leg_motor.run_target(100, 65)
    ev3.screen.show_image(ImageFile.NEUTRAL)


def act_happy():
    """Makes the puppy act happy."""
    #Replaced HEART eyes with DIZZY
    ev3.screen.show_image(ImageFile.DIZZY)
    #puppy sits down
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(1000)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(100)
    for _ in range(3):
        ev3.speaker.play_file(SoundFile.DOG_BARK_1)
        #puppy hops
        left_leg_motor.run(500)
        right_leg_motor.run(500)
        wait(275)
        left_leg_motor.stop()
        right_leg_motor.stop()
        wait(275)
        left_leg_motor.run(-50)
        right_leg_motor.run(-50)
        wait(275)
        left_leg_motor.stop()
        right_leg_motor.stop()
        wait(500)
    #puppy sits down
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(1000)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(100)
    left_leg_motor.reset_angle(0)
    right_leg_motor.reset_angle(0)
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    

def sit_down():
    """Makes the puppy sit down."""
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(1000)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(100)


def walk_steps(): 
    """Makes the puppy walk a certain number of steps.
    Modify front wheels to roll by removing anchoring pegs and switching pegs through the axle to non-friction pegs.
    Change steps to adjust the number of steps."""  

    #steps equals number of steps pup takes
    steps = 10
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(500)
    #puppy walks specified number of steps
    for value in range(1,steps + 1):  
        left_leg_motor.run_target(-100, 25, wait=False)
        right_leg_motor.run_target(-100, 25)
        while not left_leg_motor.control.target_tolerances():
            wait(300)
        left_leg_motor.run_target(100, 65, wait=False)
        right_leg_motor.run_target(100, 65)
        while not left_leg_motor.control.target_tolerances():
            wait(300)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    wait(100)    


def walk_timed(): 
    """Makes the puppy walk a certain time in ms.
    Modify front wheels to roll by removing anchoring pegs and switching pegs through the axle to non-friction pegs.
    Change walk_time to adjust the time the puppy walks in ms.""" 
    #walk_time equals desired walk time in ms
    walk_time = 6000
    elapsed_time = StopWatch()
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(500)
    #puppy walks for specified time in ms
    while elapsed_time.time() < walk_time:
        left_leg_motor.run_target(-100, 25, wait=False)
        right_leg_motor.run_target(-100, 25)
        while not left_leg_motor.control.target_tolerances():
            wait(300)
        left_leg_motor.run_target(100, 65, wait=False)
        right_leg_motor.run_target(100, 65)
        while not left_leg_motor.control.target_tolerances():
            wait(300)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    wait(100)
    elapsed_time.reset()          


def stand_up():
    """Makes the puppy stand up."""
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    self.right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    wait(500)


def stretch():
    """Makes the puppy stretch its legs backwards."""
    #puppy stands up
    left_leg_motor.run_target(100, 25, wait=False)
    right_leg_motor.run_target(100, 25)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    left_leg_motor.run_target(50, 65, wait=False)
    right_leg_motor.run_target(50, 65)
    while not left_leg_motor.control.target_tolerances():
            wait(100)
    #puppy stretches
    left_leg_motor.run_target(100, 125, wait=False)
    right_leg_motor.run_target(100, 125)
    ev3.speaker.play_file(SoundFile.DOG_WHINE)
    left_leg_motor.run_target(100, 125, wait=False)
    right_leg_motor.run_target(100, 125)
    wait(500)


def hop():
    """Makes the puppy hop."""
    left_leg_motor.run(500)
    right_leg_motor.run(500)
    wait(275)
    left_leg_motor.stop()
    right_leg_motor.stop()
    wait(275)
    left_leg_motor.run(-50)
    right_leg_motor.run(-50)
    wait(275)
    left_leg_motor.stop()
    right_leg_motor.stop()

    
"""The following code cycles through all of the behaviors, separated by beeps."""
act_playful()
wait(1000)
ev3.speaker.beep()
act_happy()
wait(1000)
ev3.speaker.beep()
act_hungry()
wait(1000)
ev3.speaker.beep()
act_angry()
wait(1000)
ev3.speaker.beep()
go_to_bathroom()
wait(1000)
ev3.speaker.beep()
go_to_sleep()
wait(1000)
ev3.speaker.beep()
wake_up()
wait(1000)
ev3.speaker.beep()
walk_steps()
wait(1000)
ev3.speaker.beep()
walk_timed()
wait(1000)
ev3.speaker.beep()
idle()
wait(1000)
ev3.speaker.beep()
