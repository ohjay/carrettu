"""
setup.py 

Run this once before doing anything to create a default 
folder structure and config files.

Usage:
    setup.py
"""

import os
import shutil
from docopt import docopt

import carrettu as ctu

if __name__ == "__main__":
    args = docopt(__doc__)

    print('Setting up carrettu folders.')
    ctu.config.setup_paths()

    config_path = os.path.join(ctu.config.ctu_path, 'vehicle.ini')
    print(config_path)

    shutil.copyfile('./config/vehicle.ini', config_path)
