#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) Copyright 2019 Brion Mario.
# (c) This file is written as a plugin for the CSSI Core library and is made available under MIT license.
# (c) For more information, see https://github.com/brionmario/cssi-plugin-heart-rate/blob/master/LICENSE.txt
# (c) Please forward any queries to the given email address. email: brion@apareciumlabs.com

"""CSSI Heart Rate Contributor Plugin

Authors:
    Brion Mario

"""

from .plugin import CSSIPluginHeartRate


def cssi_init(plugins, options):
    """Register the `CSSIPluginHeartRate` as a contributor plugin."""
    plugins.add_contributor_plugin(CSSIPluginHeartRate())
