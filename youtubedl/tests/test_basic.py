import unittest

from .context import core

# Run tests with python -m unittest tests/test_basic.py


# These are the methods used as interface with the rest of the program.
# To include a method in Video, insert the method name here.
videoBaseMethods = frozenset(['allVideoStreams', 'download', 'videoId',
        'videoThumbnail', 'videoTitle'])

class TestVideo(unittest.TestCase):

    def setUp(self):
        self.video = core.Video(
            'https://A.com')
        self.methods = [m for m in dir(self.video) if not m.startswith('__')
            and m not in self.video.__dict__.keys()]

    def testVideoInit(self):
        self.assertEqual(self.video.url,
            'https://A.com')
        self.assertEqual(self.video.progress_callback, None)

    def testWhichAreTheVideoMethods(self):
        # To include a method in Video, insert the method name in videoBaseMethods
        for m in videoBaseMethods:
            self.assertTrue(m in self.methods)

    def testVideoMethodsRaise(self):
        # All Video methods must raise NotImplementedError.
        with self.assertRaises(NotImplementedError):
            for m in self.methods:
                getattr(self.video, m)


class TestYouTubeVideo(unittest.TestCase):

    def setUp(self):
        self.video = core.Video(
            "https://www.youtube.com/watch?v=9bZkp7q19f0")
        self.methods = [m for m in dir(self.video) if not m.startswith('__')
            and m not in self.video.__dict__.keys()]

    def testYouTubeVideoInit(self):
        self.assertEqual(self.video.url,
            "https://www.youtube.com/watch?v=9bZkp7q19f0")
        self.assertEqual(self.video.progress_callback, None)

    def testYouTubeVideoBaseMethods(self):
        # To include a method in YouTubeVideo, insert the method name in Video
        for m in videoBaseMethods:
            self.assertTrue(m in self.methods)
