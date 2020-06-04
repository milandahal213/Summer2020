from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
​
class PuppyTraining:
    def __init__(self):
        self.hub = PrimeHub()
        self.colorsensor = ColorSensor('B')
        self.force = ForceSensor('A')
        self.boundary = None# Initial Decision boundary
        self.ATraining = []# Initial A examples
        self.BTraining = []# Initial B examples
        self.averageA = None# Initial average for the A training
        self.averageB = None# Initial average for the B training
​
        # +++ If you want to add more commands, initialize a Training array
        #        and average for the new command here.
​
    def observation(self):
        """Adds one training observation to the training data"""
        print('Press up or down button to tell the puppy which command you are\
            demonstrating.\n Press the center to stop training')
        while True:# Waits for button press to record an observation
            print(self.colorsensor.get_ambient_light())
            if self.hub.left_button.was_pressed():
                # Record an A command observation
                force = self.force.get_force_newton()
                dog_command = 'A'
                print('Puppy learns that this means command A')
                # Adds the observation to the recorded data
                self.ATraining.append(force)
                wait_for_seconds(0.5)
                return force, dog_command
​
            elif self.hub.right_button.was_pressed():
                # Record a B command observation
                force = self.force.get_force_newton()
                dog_command = 'B'
                print('Puppy learns that this means command B')
                # Adds the observation to the recorded data
                self.BTraining.append(force)
                wait_for_seconds(0.5)
                return force, dog_command
​
            elif self.colorsensor.get_ambient_light() > 30:
                # Stop training
                angle = 0
                dog_command = 'Exit'
                print('Puppy is done training for now.')
                return angle, dog_command
​
    def watch(self):
        """Adds multiple training observations to the training data
        Puppy watches for commands until the center button is pressed"""
        command = ''
        print('Puppy is ready to start learning!')
        while command != "Exit":
            # Repeat observations until the center button is pressed
            angle, command = self.observation()
        print('Training Over.')
​
    def train(self):
        """Calculate the means and decision boundary
        between two labelled clusters"""
        sumA = 0
        sumB = 0
        # Calculate totals
        for observation in self.ATraining:
            sumA += observation# Totals all A Training examples
        for observation in self.BTraining:
            sumB += observation# Totals all B Training examples
        # Calculate averages
        self.averageA = sumA/len(self.ATraining)# Finds mean of A commands
        self.averageB = sumB/len(self.BTraining)# Finds mean of B commands
        # +++ If you are creating additional commands, be sure to calculate
        #    the new totals and averages too!
​
        # The decision boundary is halfway between the A and B means.
        self.boundary = (self.averageA + self.averageB)/2
        return self.boundary
​
    def distance(self, angle, command):
        """Calculates the one dimensional distance between
        the current angle and given command average"""
        if command == 'A':
            return abs(angle - self.averageA)
        elif command == 'B':
            return abs(angle - self.averageB)
        else:
            # +++ You can add distance calculations for more commands here.
            return 1000
​
    def prediction(self, showresult=True):
        """Calculate the current prediction of the current Gyro angle based on
        the training and classifies based on the minimum-distance-to-mean"""
        force = self.force.get_force_newton()
        if self.distance(force, 'B') >= self.distance(force, 'A'):
            # If the current angle is closer to A, predict it is A.
            prediction = 'A'
            self.hub.light_matrix.show_image('HAPPY')
        elif self.distance(force, 'B') < self.distance(force, 'A'):
            # If the current angle is closer to B, predict it is B.
            prediction = 'B'
            self.hub.light_matrix.show_image('ANGRY')
        else:
            pass# +++ You can add additional commands here.
​
        if showresult:# Optionally print the prediction result.
            print('The puppy thinks that is a ' + prediction + ' command!')
        return prediction
​
    def report(self):
        """Prints out the current state of the model"""
        tablewidth = 20# Adjust this constant to change table width
        print("The Puppy Training Report")
        print("*"*tablewidth)
        print("These are the examples of command A: \n", self.ATraining)
        print("The average is %.2f" % self.averageA)
        print("*"*tablewidth)
        print("These are the examples of command B: \n", self.BTraining)
        print("The average is %.2f" % self.averageB)
        print("*"*tablewidth)
        print('The decision boundary is: ', self.boundary)
        print("*"*tablewidth)
​
    def forget(self):
        """Reset the training data and the model"""
        self.boundary = None# Reset Decision boundary
        self.angledata = []# Reset observation measurements
        self.commanddata = []# Reset observation labels
        self.averageA = None# Reset average for the A training
        self.averageB = None# Reset average for the B training
        # +++ If you added an extra command, be sure to reset it here too!
        print('The puppy has forgotten the training!')
​
a=PuppyTraining()
a.watch()
a.train()
while True:
    a.prediction()
    wait_for_seconds(1)
