import unittest

from .context import core

# Run tests with python -m unittest tests/tests.py


class TestVideo(unittest.TestCase):

    def setUp(self):
        self.video = core.Video(
            'https://www.youtube.com/watch?v=9bZkp7q19f0')

    def testVideoInit(self):
        self.assertEqual(self.video.url,
            'https://www.youtube.com/watch?v=9bZkp7q19f0')
        self.assertEqual(self.video.progress_callback, None)

    def testWhichAreTheVideoMethods(self):
        # To include a method in Video, insert the method name in allMethods.
        allMethods = ['download', 'videoId', 'videoStreamQuality',
            'videoThumbnail', 'videoTitle']
        methods = [x for x in dir(self.video) if not x.startswith('__')
            and x not in self.video.__dict__.keys()]
        self.assertEqual(methods, allMethods)

    def testVideoMethodsRaise(self):
        # All Video methods must raise NotImplementedError.
        with self.assertRaises(NotImplementedError):
            self.video.videoId
            self.video.videoTitle
            self.video.videoThumbnail
            self.video.videoStreamQuality
            self.video.download()
