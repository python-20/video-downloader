import unittest

from .context import core

# Run tests with python -m unittest tests/test_basic.py


allMethods = ['download', 'videoId', 'videoStreamQuality',
            'videoThumbnail', 'videoTitle']

class TestVideo(unittest.TestCase):

    def setUp(self):
        self.video = core.Video(
            'https://A.com')

    def testVideoInit(self):
        self.assertEqual(self.video.url,
            'https://A.com')
        self.assertEqual(self.video.progress_callback, None)

    def testWhichAreTheVideoMethods(self):
        # To include a method in Video, insert the method name in allMethods
        methods = [m for m in dir(self.video) if not m.startswith('__')
            and m not in self.video.__dict__.keys()]
        self.assertEqual(methods, allMethods)

    def testVideoMethodsRaise(self):
        # All Video methods must raise NotImplementedError.
        with self.assertRaises(NotImplementedError):
            self.video.videoId
            self.video.videoTitle
            self.video.videoThumbnail
            self.video.videoStreamQuality
            self.video.download()


class TestYouTubeVideo(unittest.TestCase):

    def setUp(self):
        self.video = core.Video(
            "https://www.youtube.com/watch?v=9bZkp7q19f0")

    def testYouTubeVideoInit(self):
        self.assertEqual(self.video.url,
            "https://www.youtube.com/watch?v=9bZkp7q19f0")
        self.assertEqual(self.video.progress_callback, None)

    def testWhichAreYouTubeVideoMethods(self):
        # To include a method in YouTubeVideo, insert the method name in Video
        methods = [m for m in dir(self.video) if not m.startswith('__')
            and m not in self.video.__dict__.keys()]
        self.assertEqual(methods, allMethods)
