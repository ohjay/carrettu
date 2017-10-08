"""
actuators.py

Classes to control the motors and servos. These classes 
are wrapped in a mixer class before being used in the drive loop.
"""

import time
from . import utils
        
class PCA9685_Controller:
    """
    Adafruit PWM controller.
    This is used for most RC cars.
    """
    def __init__(self, channel, frequency=60):
        # Initialize the PCA9685 using the default address (0x40).
        import Adafruit_PCA9685
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(frequency)
        self.channel = channel

    def set_pulse(self, pulse):
        self.pwm.set_pwm(self.channel, 0, pulse) 

class PWMSteering:
    """
    Wrapper over a PWM motor controller to convert angles to PWM pulses.
    """
    LEFT_ANGLE = -1
    RIGHT_ANGLE = 1

    def __init__(self, controller=None, left_pulse=290, right_pulse=490):
        self.controller = controller
        self.left_pulse = left_pulse
        self.right_pulse = right_pulse

    def update(self, angle):
        # Map absolute angle to an angle that vehicle can implement
        pulse = utils.map_range(angle,
                                self.LEFT_ANGLE, self.RIGHT_ANGLE,
                                self.left_pulse, self.right_pulse)
        self.controller.set_pulse(pulse)

    def shutdown(self):
        self.update(0)  # straighten the wheels

class PWMThrottle:
    """
    Wrapper over a PWM motor controller to convert -1 to 1 throttle values to PWM pulses.
    """
    MIN_THROTTLE = -1
    MAX_THROTTLE = 1

    def __init__(self, controller=None, max_pulse=300, min_pulse=490, zero_pulse=350):
        self.controller = controller
        self.max_pulse = max_pulse
        self.min_pulse = min_pulse
        self.zero_pulse = zero_pulse

        # Send zero pulse to calibrate ESC
        self.controller.set_pulse(self.zero_pulse)
        time.sleep(1)

    def update(self, throttle):
        if throttle > 0:
            pulse = utils.map_range(throttle, 0, self.MAX_THROTTLE, self.zero_pulse, self.max_pulse)
        else:
            pulse = utils.map_range(throttle, self.MIN_THROTTLE, 0, self.min_pulse, self.zero_pulse)
        self.controller.set_pulse(pulse)

    def shutdown(self):
        self.update(0)  # stop vehicle
