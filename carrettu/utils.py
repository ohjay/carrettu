import os
import glob
import zipfile
import numpy as np
from io import BytesIO

# ------
# IMAGES
# ------

def img_to_binary(img):
    """
    accepts: PIL image
    returns: binary stream (used to save to database)
    """
    f = BytesIO()
    img.save(f, format='jpeg')
    return f.getvalue()

def normalize_img(img):
    return (img - img.mean() / np.std(img)) / 255.0

# -----
# FILES
# -----

def most_recent_file(dir_path, ext=''):
    """
    Return the most recent file given a directory path and extension.
    """
    query = dir_path + '/*' + ext
    newest = min(glob.iglob(query), key=os.path.getctime)
    return newest

def make_dir(path):
    real_path = os.path.expanduser(path)
    if not os.path.exists(real_path):
        os.makedirs(real_path)
    return real_path

def zip_dir(dir_path, zip_path):
    """
    Create and save a ZIP file of a single-level directory.
    """
    file_paths = glob.glob(dir_path + "/*")  # create path to search for files

    zf = zipfile.ZipFile(zip_path, 'w')
    dir_name = os.path.basename(dir_path)
    for p in file_paths:
        file_name = os.path.basename(p)
        zf.write(p, arcname=os.path.join(dir_name, file_name))
    zf.close()
    return zip_path

# -------
# BINNING
# -------

def map_range(x, x_min, x_max, y_min, y_max):
    """
    Linear mapping between two ranges of values.
    """
    x_range = x_max - x_min
    y_range = y_max - y_min
    xy_ratio = x_range / y_range

    y = ((x - x_min) / xy_ratio + y_min) // 1
    return int(y)
