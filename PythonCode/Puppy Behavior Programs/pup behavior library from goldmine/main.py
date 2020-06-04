#!/usr/bin/env pybricks-micropython

"""
Modified Example LEGO® MINDSTORMS® EV3 Puppy Program
This program includes the eight behaviors in the original program plus two additional walking behaviors:
walk_steps and walk_timed.

-------------------------------------------
This program requires LEGO® EV3 MicroPython
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3
Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-core
"""

"""
Start the puppy sitting down. 
Once the orange light appears, use the up and down buttons to adjust the puppy's head. 
Then, press the center butoon to start the main program. 
"""
from random import randint 

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Button, Color, Direction
from pybricks.media.ev3dev import Image, ImageFile, SoundFile
from pybricks.tools import wait, StopWatch


class Puppy:
    # These constants are used for positioning the legs.
    HALF_UP_ANGLE = 25
    STAND_UP_ANGLE = 65
    STRETCH_ANGLE = 125

    # These constants are for positioning the head.
    HEAD_UP_ANGLE = 0
    HEAD_DOWN_ANGLE = -40

    # These constants are for the eyes.
    #replaced HURT, HEART, SQUINTY with AWAKE,DIZZY,PINCHED_MIDDLE respectively
    NEUTRAL_EYES = Image(ImageFile.NEUTRAL)
    TIRED_EYES = Image(ImageFile.TIRED_MIDDLE)
    TIRED_LEFT_EYES = Image(ImageFile.TIRED_LEFT)
    TIRED_RIGHT_EYES = Image(ImageFile.TIRED_RIGHT)
    SLEEPING_EYES = Image(ImageFile.SLEEPING)
    HURT_EYES = Image(ImageFile.AWAKE)
    ANGRY_EYES = Image(ImageFile.ANGRY)
    HEART_EYES = Image(ImageFile.DIZZY)
    SQUINTY_EYES = Image(ImageFile.PINCHED_MIDDLE)  

    def __init__(self):
        # Initialize the EV3 brick.
        self.ev3 = EV3Brick()

        # Initialize the motors connected to the back legs.
        self.left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

        # Initialize the motor connected to the head.
        # Worm gear moves 1 tooth per rotation. It is interfaced to a 24-tooth
        # gear. The 24-tooth gear is connected to parallel 12-tooth gears via
        # an axle. The 12-tooth gears interface with 36-tooth gears.
        self.head_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE,
                                gears=[[1, 24], [12, 36]])

        # Initialize the Color Sensor. 
        self.color_sensor = ColorSensor(Port.S4)

        # Initialize the touch sensor. 
        self.touch_sensor = TouchSensor(Port.S1)

        # This attribute is used by properties.
        self._eyes = None
        
        # These attributes are used by the playful behavior.
        self.playful_timer = StopWatch()
        self.playful_bark_interval = None


    def adjust_head(self):
        """Use the up and down buttons on the EV3 brick to adjust the puppy's
        head up or down.
        """
        self.ev3.screen.show_image(ImageFile.EV3_ICON)
        self.ev3.light.on(Color.ORANGE)

        while True:
            buttons = self.ev3.buttons.pressed()
            if Button.CENTER in buttons:
                break
            elif Button.UP in buttons:
                self.head_motor.run(20)
            elif Button.DOWN in buttons:
                self.head_motor.run(-20)
            else:
                self.head_motor.stop()
            wait(100)

        self.head_motor.stop()
        self.head_motor.reset_angle(0)
        self.ev3.light.on(Color.GREEN)

    def move_head(self, target):
        """Move the head to the target angle.
        Arguments:
            target (int):
                The target angle in degrees. 0 is the starting position,
                negative values are below this point and positive values
                are above this point.
        """
        self.head_motor.run_target(20, target)

    def reset(self):
        # must be called when puppy is sitting down.
        self.left_leg_motor.reset_angle(0)
        self.right_leg_motor.reset_angle(0)  
        self.behavior = self.idle

    # The next 10 methods define the 10 behaviors of the puppy.

    def idle(self):
        """The puppy is idle."""
        self.stand_up()
        self.eyes = self.NEUTRAL_EYES

    def go_to_sleep(self):
        """Makes the puppy go to sleep. 
        Press the center button and touch sensor at the same time to awaken the puppy."""
        self.eyes = self.TIRED_EYES
        self.sit_down()
        self.move_head(self.HEAD_DOWN_ANGLE)
        self.eyes = self.SLEEPING_EYES
        self.ev3.speaker.play_file(SoundFile.SNORING)
        if self.touch_sensor.pressed() and Button.CENTER in self.ev3.buttons.pressed(): 
            self.behavior = self.wake_up

    def wake_up(self):
        """Makes the puppy wake up."""
        self.eyes = self.TIRED_EYES
        self.ev3.speaker.play_file(SoundFile.DOG_WHINE)
        self.move_head(self.HEAD_UP_ANGLE)
        self.sit_down()
        self.stretch()
        wait(1000)
        self.stand_up()
        self.behavior = self.idle

    def act_playful(self):
        """Makes the puppy act playful."""
        self.eyes = self.NEUTRAL_EYES
        self.stand_up()
        self.playful_bark_interval = 0
        if self.playful_timer.time() > self.playful_bark_interval:
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_2)
            self.playful_timer.reset()
            self.playful_bark_interval = randint(4, 8) * 1000

    def act_angry(self):
        """Makes the puppy act angry."""
        self.eyes = self.ANGRY_EYES
        self.ev3.speaker.play_file(SoundFile.DOG_GROWL)
        self.stand_up()
        wait(1500)
        self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
      
    def act_hungry(self):
        """Makes the puppy act hungry."""
        self.eyes = self.HURT_EYES
        self.sit_down()
        self.ev3.speaker.play_file(SoundFile.DOG_WHINE)

    def go_to_bathroom(self):
        """Makes the puppy go to the bathroom."""
        self.eyes = self.SQUINTY_EYES
        self.stand_up()
        wait(100)
        self.right_leg_motor.run_target(100, self.STRETCH_ANGLE)
        wait(800)
        self.ev3.speaker.play_file(SoundFile.HORN_1)
        wait(1000)
        for _ in range(3):
            self.right_leg_motor.run_angle(100, 20)
            self.right_leg_motor.run_angle(100, -20)
        self.right_leg_motor.run_target(100, self.STAND_UP_ANGLE)
        self.behavior = self.idle

    def act_happy(self):
        """Makes the puppy act happy."""
        self.eyes = self.HEART_EYES
        # self.move_head(self.?)
        self.sit_down()
        for _ in range(3):
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.hop()
        wait(500)
        self.sit_down()
        self.reset()

    def sit_down(self):
        """Makes the puppy sit down."""
        self.left_leg_motor.run(-50)
        self.right_leg_motor.run(-50)
        wait(1000)
        self.left_leg_motor.stop()
        self.right_leg_motor.stop()
        wait(100)

    def walk_steps(self): 
        """Makes the puppy walk a certain number of steps.
        Modify front wheels to roll by removing anchoring pegs and switching pegs through the axle to non-friction pegs.
        Change steps to adjuct the number of steps."""  
        #steps equals number of steps pup takes
        steps = 10
        self.stand_up()
        for value in range(1,steps + 1):  
            self.left_leg_motor.run_target(-100, 25, wait=False)
            self.right_leg_motor.run_target(-100, 25)
            while not self.left_leg_motor.control.target_tolerances():
                wait(300)
            self.left_leg_motor.run_target(100, 65, wait=False)
            self.right_leg_motor.run_target(100, 65)
            while not self.left_leg_motor.control.target_tolerances():
                wait(300)
        self.left_leg_motor.run_target(50, 65, wait=False)
        self.right_leg_motor.run_target(50, 65)
        wait(100)    

    def walk_timed(self): 
        """Makes the puppy walk a certain time in ms.
        Modify front wheels to roll by removing anchoring pegs and switching pegs through the axle to non-friction pegs.
        Change walk_time to adjust the time the puppy walks in ms.""" 
        #walk_time equals desired walk time in ms
        walk_time = 6000
        elapsed_time = StopWatch()
        while elapsed_time.time() < walk_time:
            self.left_leg_motor.run_target(-100, 25, wait=False)
            self.right_leg_motor.run_target(-100, 25)
            while not self.left_leg_motor.control.target_tolerances():
                wait(300)
            self.left_leg_motor.run_target(100, 65, wait=False)
            self.right_leg_motor.run_target(100, 65)
            while not self.left_leg_motor.control.target_tolerances():
                wait(300)
        self.left_leg_motor.run_target(50, 65, wait=False)
        self.right_leg_motor.run_target(50, 65)
        wait(100)
        elapsed_time.reset()          

    # The next 4 methods define actions that are used to make some parts of
    # the behaviors above.

    def stand_up(self):
        """Makes the puppy stand up."""
        self.left_leg_motor.run_target(100, self.HALF_UP_ANGLE, wait=False)
        self.right_leg_motor.run_target(100, self.HALF_UP_ANGLE)
        while not self.left_leg_motor.control.target_tolerances():
                wait(100)
        self.left_leg_motor.run_target(50, self.STAND_UP_ANGLE, wait=False)
        self.right_leg_motor.run_target(50, self.STAND_UP_ANGLE)
        while not self.left_leg_motor.control.target_tolerances():
                wait(100)
        wait(500)
   
    def stretch(self):
        """Makes the puppy stretch its legs backwards."""
        self.stand_up()
        self.left_leg_motor.run_target(100, self.STRETCH_ANGLE, wait=False)
        self.right_leg_motor.run_target(100, self.STRETCH_ANGLE)
        self.ev3.speaker.play_file(SoundFile.DOG_WHINE)
        self.left_leg_motor.run_target(100, self.STAND_UP_ANGLE, wait=False)
        self.right_leg_motor.run_target(100, self.STAND_UP_ANGLE)
        wait(500)

    def hop(self):
        """Makes the puppy hop."""
        self.left_leg_motor.run(500)
        self.right_leg_motor.run(500)
        wait(275)
        self.left_leg_motor.stop()
        self.right_leg_motor.stop()
        wait(275)
        self.left_leg_motor.run(-50)
        self.right_leg_motor.run(-50)
        wait(275)
        self.left_leg_motor.stop()
        self.right_leg_motor.stop()

    @property
    def eyes(self):
        """Gets and sets the eyes."""
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        if value != self._eyes:
            self._eyes = value
            self.ev3.screen.show_image(value)

   
    def run(self):
        """This is the main program run loop."""
        self.sit_down()
        self.adjust_head()
        self.eyes = self.SLEEPING_EYES
        self.reset()
        #self.eyes = self.SLEEPING_EYES
        
        """The following code cycles through all of the behaviors, separated by beeps."""
        self.act_playful()
        wait(1000)
        self.ev3.speaker.beep()
        self.act_happy()
        wait(1000)
        self.ev3.speaker.beep()
        self.act_hungry()
        wait(1000)
        self.ev3.speaker.beep()
        self.act_angry()
        wait(1000)
        self.ev3.speaker.beep()
        self.go_to_bathroom()
        wait(1000)
        self.ev3.speaker.beep()
        self.go_to_sleep()
        wait(1000)
        self.ev3.speaker.beep()
        self.wake_up()
        wait(1000)
        self.ev3.speaker.beep()
        self.walk_steps()
        wait(1000)
        self.ev3.speaker.beep()
        self.walk_timed()
        wait(1000)
        self.ev3.speaker.beep()
        self.idle()
        wait(1000)
        self.ev3.speaker.beep()

if __name__ == '__main__':
    puppy = Puppy()
    puppy.run()
    

   