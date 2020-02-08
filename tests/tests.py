import unittest

from ..core import Video


class TestVideo(unittest.TestCase):

    video = Video('https://www.youtube.com/watch?v=9bZkp7q19f0')

    def testURL(self, video):
        v = video
        self.assertEqual(v, 'https://www.youtube.com/watch?v=9bZkp7q19f0')


if __name__=='__main__':
    unittest.main()
