import os

if os.uname()[4].startswith('arm'):
    print('Detected running on Raspberry Pi. Only importing select modules.')
    from . import (utils, actuators, mixers, sensors, vehicles, config)
else:
    print('Loading default modules.')
    from . import (utils, sensors, actuators, mixers, vehicles, config)
