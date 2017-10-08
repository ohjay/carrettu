"""
drive.py

Script to run on the Raspberry PI to start your vehicle's drive loop. The drive loop
will use post requests to the server specified in the remote argument. Run the 
serve.py script on a different computer to start the remote server.

Usage:
    drive.py [--remote=<name>] [--config=<name>]

Options:
  --config=<name>   vehicle configuration file name (without extension)  [default: vehicle]
"""

import os
from docopt import docopt

import donkey as dk

# Get args.
args = docopt(__doc__)

if __name__ == '__main__':
    # load config file
    cfg = dk.config.parse_config('~/mydonkey/vehicle.ini')

    # load the actuators (default is the adafruit servo hat)
    throttle_controller = dk.actuators.PCA9685_Controller(cfg['throttle_actuator_channel'])
    steering_controller = dk.actuators.PCA9685_Controller(cfg['steering_actuator_channel'])

    # set the PWM ranges
    throttle = dk.actuators.PWMThrottleActuator(controller=throttle_controller,
                                                  min_pulse=cfg['throttle_actuator_min_pulse'],
                                                  max_pulse=cfg['throttle_actuator_max_pulse'],
                                                  zero_pulse=cfg['throttle_actuator_zero_pulse'])

    steering = dk.actuators.PWMSteeringActuator(controller=steering_controller,
                                                  left_pulse=cfg['steering_actuator_min_pulse'],
                                                  right_pulse=cfg['steering_actuator_max_pulse'])

    # abstract class to combine actuators
    mixer = dk.mixers.AckermannSteeringMixer(steering, throttle)

    # asynch img capture from pi camera
    camera = dk.sensors.PiVideoStream()

    # Create your car
    car = dk.vehicles.BaseVehicle(drive_loop_delay=cfg['vehicle_loop_delay'],
                                  camera=camera,
                                  actuator_mixer=mixer)
    
    # Start the drive loop
    car.start()
