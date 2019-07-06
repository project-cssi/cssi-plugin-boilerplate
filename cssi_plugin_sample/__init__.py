#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Copyright 2019 CSSI.
# (c) This file is written as a plugin for the CSSI Core library and is made available under MIT license.
# (c) For more information, see https://github.com/project-cssi/cssi-plugin-boilerplate/blob/master/LICENSE.txt
# (c) Please forward any queries to the given email address. email: opensource@apareciumlabs.com

"""CSSI Plugin Boilerplate

Authors:
    Brion Mario

"""

import logging
from logging import NullHandler

from .plugin import CSSIPluginSample

# Add NullHandler to avoid errors if the host application
# doesn't have logging configured.
default_logger = logging.getLogger("cssi.core")
default_logger.addHandler(NullHandler())

# Set the default level to WARN
if default_logger.level == logging.NOTSET:
    default_logger.setLevel(logging.WARN)


def cssi_init(plugins, options):
    """Register the `CSSIPluginSample` as a contributor plugin."""
    plugins.add_contributor_plugin(CSSIPluginSample())
