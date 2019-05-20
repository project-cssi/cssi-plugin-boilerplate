#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Copyright 2019 Brion Mario.
# (c) This file is written as a plugin for the CSSI Core library and is made available under MIT license.
# (c) For more information, see https://github.com/brionmario/cssi-plugin-heart-rate/blob/master/LICENSE.txt
# (c) Please forward any queries to the given email address. email: brion@apareciumlabs.com

"""
Brief:   OpenCV based Heart Rate plugin for CSSI Core Library

Author:  Brion Mario
"""

import os
from setuptools import setup


REQUIREMENTS = [line.strip() for line in
                open(os.path.join("requirements.txt")).readlines()]

setup(
    name='cssi-plugin-heart-rate',
    version='0.1.0',
    url='https://github.com/brionmario/cssi-plugin-heart-rate',
    description='A contributor plugin for CSSI to measure heart rate using OpenCV',
    author='Brion Mario',
    author_email='brion@apareciumlabs.com',
    packages=['cssi-plugin-heart-rate'],
    install_requires=REQUIREMENTS,
    license="The MIT License (MIT)"
)
