import unittest

from .context import core

# Run tests with python -m unittest tests/test_basic.py


# These are the methods used as interface with the rest of the program.
# To include a method in Video, insert the method name here.
videoBaseMethods = frozenset(['allVideoStreams', 'download', 'videoId',
    'videoThumbnail', 'videoTitle'])
videoBaseAttributes = frozenset(['url', 'progress_callback'])


class TestVideo(unittest.TestCase):
    """Tests for the base class Video."""

    def setUp(self):
        self.video = core.Video(
            'https://A.com')
        self.methods = [m for m in dir(self.video) if not m.startswith('__')
            and m not in self.video.__dict__.keys()]
        self.attrs = [a for a in self.video.__dict__.keys()]

    def testVideoInit(self):
        """Test the Video __init__ method."""

        # To include an attribute in Video, insert the attribute
        # name in videoBaseAttributes.
        for a in videoBaseAttributes:
            self.assertTrue(a in self.attrs)

    def testVideoInitAttributes(self):
        """Test the base attributes defined in the Video __init__ method."""
        urlCases = ['https://A.com', '', 2, 1.0]
        for c in urlCases:
            vid = core.Video(c)
            self.assertEqual(vid.url,
                str(c))   # Test if url casts the parameter to str.
        self.assertEqual(vid.progress_callback, None)

    def testWhichAreTheVideoMethods(self):
        """Test if the methods in Video are only those
           specified in the interface.

        To include a method in Video, insert the method name in videoBaseMethods
        """
        for m in videoBaseMethods:
            self.assertTrue(m in self.methods)

    def testVideoMethodsRaise(self):
        """Test if all methods in Video are 'abstract'.

        All Video methods must raise NotImplementedError.
        """
        with self.assertRaises(NotImplementedError):
            for m in self.methods:
                getattr(self.video, m)


class TestYouTubeVideo(unittest.TestCase):
    """Test the YouTubeVideo class."""

    def setUp(self):
        """Create a YouTubeVideo instance and a list of its available methods."""
        self.video = core.Video(
            "https://www.youtube.com/watch?v=9bZkp7q19f0")
        self.methods = [m for m in dir(self.video) if not m.startswith('__')
            and m not in self.video.__dict__.keys()]

    def testYouTubeVideoInit(self):
        """Test the base attributes created with the YouTubeVideo object."""
        self.assertEqual(self.video.url,
            "https://www.youtube.com/watch?v=9bZkp7q19f0")
        self.assertEqual(self.video.progress_callback, None)

    def testYouTubeVideoBaseMethods(self):
        """Test if the YouTubeVideo class implements all the base Video methods.

        To include a method in YouTubeVideo, insert the method name in Video.
        """
        for m in videoBaseMethods:
            self.assertTrue(m in self.methods)
