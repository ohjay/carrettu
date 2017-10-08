"""
vehicles.py

Class to pull together all parts that operate the vehicle (e.g. sensors and actuators).
"""

import time
from . import vision

class BaseVehicle:
    def __init__(self, drive_loop_delay=0.5, camera=None, actuator_mixer=None):
        self.drive_loop_delay = drive_loop_delay  # how long to wait between loops

        # These need to be updated when the vehicle is defined
        self.camera = camera
        self.actuator_mixer = actuator_mixer

    def start(self):
        start_time = time.time()

        # Drive loop
        while True:
            now = time.time()
            start = now

            milliseconds = int((now - start_time) * 1000)

            # Get image from camera (threaded)
            img = self.camera.capture_arr()

            angle, throttle, drive_mode = 0, 0, 'user'
            # angle, throttle, drive_mode = self.remote.decide_threaded(img, angle, throttle, milliseconds)

            self.actuator_mixer.update(throttle, angle)

            end = time.time()
            lag = end - start
            print('\r CAR: angle: {:+04.2f}   throttle: {:+04.2f}   drive_mode: {}  lag: {:+04.2f}'.format(angle, throttle, drive_mode, lag), end='')           
            
            time.sleep(self.drive_loop_delay)

class TestVehicle(BaseVehicle):

    def start(self):
        print('[+] Starting the car.')
        start_time = time.time()

        # Wait two seconds before starting the script
        time.sleep(2)

        # Drive loop
        while True:
            now = time.time()

            # Stop the loop if it has run for 60 sec
            if (now - start_time) >= 40:
                break

            start = now

            # Get image from camera (threaded)
            img = self.camera.capture_arr()

            """
            TODO: USE `img` TO DECIDE ON ANGLE AND THROTTLE
            """

            print(type(img))
            print(img.shape)  # for debugging
            print('Dominant colors: %r' % vision.dominant_colors(img))

            angle = 0
            throttle = 0.2

            self.actuator_mixer.update(throttle, angle)

            end = time.time()
            lag = end - start
            print('\r CAR: angle: {:+04.2f}   throttle: {:+04.2f}  lag: {:+04.2f}'.format(angle, throttle, lag))
            
            time.sleep(self.drive_loop_delay)
