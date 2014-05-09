#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Fredrik Strandin <fredrik@strandin.name>
#
# Licensed under MIT

"""RSS Torrent Download Client"""

from __future__ import print_function

import feedparser
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

class RTDC(object):
    """Master-class, combining all the work"""

    def __init__(self, config_file):
        """Initialize with a configuration"""
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.feed = None

    def run(self):
        """Lets do this!"""
        torrent_dir = self.config.get('main', 'TorrentDir')
        print("Wohoo, running")
        print(torrent_dir)

    def get_rss(self, rss_path):
        """Load RSS-feed"""
        self.feed = feedparser.parse(rss_path)
