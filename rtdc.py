#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Fredrik Strandin <fredrik@strandin.name>
#
# Licensed under MIT

"""RSS Torrent Download Client"""

import ConfigParser

class RTDC(object):
    """Master-class, combining all the work"""

    def __init__(self, config_file):
        """Initialize with a configuration"""
        self.config = ConfigParser.ConfigParser()
        self.config.read(config_file)
        self.feed = None

    def run(self):
        """Lets do this!"""
        torrent_dir = self.config.get('main', 'TorrentDir')
        print "Wohoo, running"
        print torrent_dir
