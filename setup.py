from setuptools import setup, find_packages

setup(name='carrettu',
      version='0.01',
      description='A library for small scale DIY self driving cars',
      url='https//github.com/ohjay/carrettu',
      author='the Floxx crew',
      author_email='owenjow@berkeley.edu',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars drive',
      install_requires=['numpy', 'pillow', 'docopt', 'requests', 'envoy'],
      extras_require={
          'server': ['h5py', 'scikit-image', 'opencv-python', 'pandas'],
          'pi': ['picamera', 'Adafruit_PCA9685']
      },
      packages=find_packages(exclude=(['tests', 'docs', 'env'])))
