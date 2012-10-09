#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name="bs12_discovery",
      author="Joel Cross",
      url="http://github.com/ukch/bs12_discovery",
      version='0.1',
      packages=['bs12_discovery'],
      package_dir={'': 'src'},
      package_data={},
      zip_safe=True,
)
