#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Copyright 2019 CSSI.
# (c) This file is written as a plugin for the CSSI Core library and is made available under MIT license.
# (c) For more information, see https://github.com/project-cssi/cssi-plugin-boilerplate/blob/master/LICENSE.txt
# (c) Please forward any queries to the given email address. email: opensource@apareciumlabs.com

"""
Brief:   Sample plugin for CSSI Core Library

Authors:
    Brion Mario
"""

import os
from setuptools import setup


REQUIREMENTS = [line.strip() for line in
                open(os.path.join("requirements.txt")).readlines()]

setup(
    name='cssi_plugin_sample',
    version='0.1.0',
    url='https://github.com/project-cssi/cssi-plugin-boilerplate',
    description='A sample contributor plugin for CSSI library',
    author='Brion Mario',
    author_email='brion@apareciumlabs.com',
    packages=['cssi_plugin_sample'],
    install_requires=REQUIREMENTS,
    license="The MIT License (MIT)"
)
