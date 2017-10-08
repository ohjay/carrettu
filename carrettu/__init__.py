import os
uname = os.uname()
if not uname[4].startswith('arm'):
    print('Loading modules for server.')
    from . import (utils,
                   sensors,
                   actuators,
                   mixers,
                   vehicles,
                   config) 
else:
    print('Detected running on Raspberry Pi. Only importing select modules.')
    from . import (actuators, 
                   mixers, 
                   sensors, 
                   vehicles, 
                   config)
