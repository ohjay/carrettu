"""
mixers.py

Classes to wrap motor controllers into a functional drive unit.
"""

class BaseMixer():

    def update_angle(self, angle):
        pass

    def update_throttle(self, throttle):
        pass

    def update(self, throttle=0, angle=0):
        """Convenience function to update
        angle and throttle at the same time"""
        self.update_angle(angle)
        self.update_throttle(throttle)

class AckermannSteeringMixer(BaseMixer):
    """
    Mixer for vehicles steered by changing the angle of the front wheels.
    This is used for RC cars.
    """
    def __init__(self, steering_actuator=None, throttle_actuator=None):
        self.steering_actuator = steering_actuator
        self.throttle_actuator = throttle_actuator

    def update(self, throttle=0, angle=0):
        self.steering_actuator.update(angle)
        self.throttle_actuator.update(throttle)
