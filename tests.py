import os
import shutil
import tempfile

import unittest

from rtdc import RTDC


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

    def test_get_rss(self):
        rss_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'test.rss'
        )
        self.rtdc.get_rss(rss_path)
        self.assertEqual(len(self.rtdc.feed.entries), 2)

    def tearDown(self):
        shutil.rmtree(self.torrent_dir)
        os.remove(self.config_file)
