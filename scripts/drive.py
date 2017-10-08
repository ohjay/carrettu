"""
drive.py

Script to run on the Raspberry Pi in order to start your vehicle's drive loop.

Usage:
    drive.py
"""

from docopt import docopt
import carrettu as ctu

args = docopt(__doc__)

if __name__ == '__main__':
    # Load config file
    cfg = ctu.config.parse_config('~/mydonkey/vehicle.ini')

    # Load the actuators (default is the Adafruit servo hat)
    throttle_controller = ctu.actuators.PCA9685_Controller(cfg['throttle_actuator_channel'])
    steering_controller = ctu.actuators.PCA9685_Controller(cfg['steering_actuator_channel'])

    # Set the PWM ranges
    throttle = ctu.actuators.PWMThrottle(controller=throttle_controller,
                                         min_pulse=cfg['throttle_actuator_min_pulse'],
                                         max_pulse=cfg['throttle_actuator_max_pulse'],
                                         zero_pulse=cfg['throttle_actuator_zero_pulse'])

    steering = ctu.actuators.PWMSteering(controller=steering_controller,
                                         left_pulse=cfg['steering_actuator_min_pulse'],
                                         right_pulse=cfg['steering_actuator_max_pulse'])

    # Abstract class to combine actuators
    mixer = ctu.mixers.AckermannSteeringMixer(steering, throttle)

    # Asynchronous image capture from Pi camera
    camera = ctu.sensors.PiVideoStream()

    # Create the car
    car = ctu.vehicles.TestVehicle(drive_loop_delay=cfg['vehicle_loop_delay'],
                                   camera=camera,
                                   actuator_mixer=mixer)
    
    # Start the drive loop
    car.start()
