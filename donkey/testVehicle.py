import time

class TestVehicle(BaseVehicle):

    def __init__(self,
                 drive_loop_delay = .5,
                 camera=None,
                 actuator_mixer=None,
                 pilot=None,
                 remote=None):
        BaseVehicle.__init__(self, drive_loop_delay, camera, actuator_mixer, pilot, remote)

    def start(self):
        start_time = time.time()
        angle = 0.
        throttle = 0.

        # Wait 30 sec before starting the script
        time.sleep(30)

        #drive loop
        while True:
            now = time.time()

            # Stop the loop if it has run for 60 sec
            if (now - start_time) >= 40:
                break

            start = now

            milliseconds = int( (now - start_time) * 1000)

            #get image array image from camera (threaded)
            img_arr = self.camera.capture_arr()

            # Set angle, throttle, and drive_mode depending on img_arr
            angle = 0
            throttle = 0.1

            if drive_mode == 'local':
                angle, throttle = self.pilot.decide(img_arr)

            if drive_mode == 'local_angle':
                #only update angle from local pilot
                angle, _ = self.pilot.decide(img_arr)

            self.actuator_mixer.update(throttle, angle)

            #print current car state
            end = time.time()
            lag = end - start
            print('\r CAR: angle: {:+04.2f}   throttle: {:+04.2f}   drive_mode: {}  lag: {:+04.2f}'.format(angle, throttle, drive_mode, lag), end='')           
            
            time.sleep(self.drive_loop_delay)
