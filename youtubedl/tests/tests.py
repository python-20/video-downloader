import unittest

import youtubedl.core as core

# Run tests with python -m unittest path/to/tests.py


class TestVideo(unittest.TestCase):

    def setUp(self):
        self.video = core.Video('https://www.youtube.com/watch?v=9bZkp7q19f0')

    def testVideoInit(self):
        self.assertEqual(self.video.url, 'https://www.youtube.com/watch?v=9bZkp7q19f0')
        self.assertEqual(self.video.progress_callback, None)

    def testVideoMethods(self):
        with self.assertRaises(NotImplementedError) as error:
            self.video.videoId
        self.assertEqual(error.expected, NotImplementedError)
