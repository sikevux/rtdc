from rtdc import RTDC

import os
import shutil
import tempfile
import unittest

class RTDCTests(unittest.TestCase):

    def setUp(self):
        self.torrent_dir = tempfile.mkdtemp(prefix='torrents_')
        (_, self.config_file) = \
            tempfile.mkstemp(suffix='_config.ini', prefix='rtdc_')

        fake_config = "[main]\n" \
            "TorrentDir: " + self.torrent_dir + "\n" \
            "RSSFeed: http://example.com/feed\n"


        with open(self.config_file, 'w+') as config:
            config.write(fake_config)

        self.rtdc = RTDC(self.config_file)

    def test_config_load(self):
        self.assertEqual(self.rtdc.config.get('main', 'TorrentDir'),
            self.torrent_dir)

    def test_main_run(self):
        self.rtdc.run()

    def tearDown(self):
        shutil.rmtree(self.torrent_dir)
        os.remove(self.config_file)
