"""
vehicles.py

Class to pull together all parts that operate the vehicle (e.g. sensors and actuators).
"""

import time

class BaseVehicle:
    def __init__(self, drive_loop_delay=0.5, camera=None, actuator_mixer=None):
        self.drive_loop_delay = drive_loop_delay # how long to wait between loops

        # these need to be updated when vehicle is defined
        self.camera = camera
        self.actuator_mixer = actuator_mixer

    def start(self):
        start_time = time.time()

        # drive loop
        while True:
            now = time.time()
            start = now

            milliseconds = int((now - start_time) * 1000)

            # get image array image from camera (threaded)
            img_arr = self.camera.capture_arr()

            angle, throttle, drive_mode = 0, 0, 'user'
            # angle, throttle, drive_mode = self.remote.decide_threaded(img_arr, angle, throttle, milliseconds)

            self.actuator_mixer.update(throttle, angle)

            # print current car state
            end = time.time()
            lag = end - start
            print('\r CAR: angle: {:+04.2f}   throttle: {:+04.2f}   drive_mode: {}  lag: {:+04.2f}'.format(angle, throttle, drive_mode, lag), end='')           
            
            time.sleep(self.drive_loop_delay)

class TestVehicle(BaseVehicle):

    def start(self):
        start_time = time.time()

        # Wait two seconds before starting the script
        time.sleep(2)

        # drive loop
        while True:
            print('next loop iteration')
            now = time.time()

            # Stop the loop if it has run for 60 sec
            if (now - start_time) >= 40:
                print('[o] Done.')
                break

            start = now

            # get image array image from camera (threaded)
            # img_arr = self.camera.capture_arr()

            # Set angle, throttle, and drive_mode depending on img_arr
            angle = 0
            throttle = 0.2

            self.actuator_mixer.update(throttle, angle)

            # print current car state
            end = time.time()
            lag = end - start
            print('\r CAR: angle: {:+04.2f}   throttle: {:+04.2f}  lag: {:+04.2f}'.format(angle, throttle, lag))
            
            time.sleep(self.drive_loop_delay)
