#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Fredrik Strandin <fredrik@strandin.name>
#
# Licensed under MIT

"""RSS Torrent Download Client"""

from __future__ import print_function

try:
    import ConfigParser as configparser
except ImportError:
    import configparser

import feedparser


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

    def get_hits(self):
        """Get hits from when names in config matches titles in the feed"""
        name_items = self.config.items('names')
        result = []
        for _, name in name_items:
            result.extend([(r.title, r.link) for r in self.find_in_feed(name)])
        return result

    def find_in_feed(self, name):
        """Search for a specific name in the feed"""
        parts = name.lower().split(' ')
        result = []
        for entry in self.feed.entries:
            matches = True
            for part in parts:
                if part not in entry.title:
                    matches = False
            if matches:
                result.append(entry)
        return result
