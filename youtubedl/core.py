import pytube

from pytube import YouTube

# https://python-pytube3.readthedocs.io/en/latest/user/quickstart.html


class Video:
    """ Base class for the (Service)Video object.

    This is an interface class, should not be used directly. A new video service
    is registered by subclassing it.
    """

    def __init__(self, url, progress_callback=None):
        """ Initialize the Video object.

        Args:
            url: The URL of the video
            progress_callback: The name of the callback function to be called
        """
        self.url = url
        self.progress_callback = progress_callback

    @property
    def videoId(self):
        """ Return the ID of the video.

        This method should be overriden in the (Service)Video class.
        """
        raise NotImplementedError

    @property
    def videoTitle(self):
        """ Return the title of the video.

        This method should be overriden in the (Service)Video class.
        """
        raise NotImplementedError

    @property
    def videoThumbnail(self):
        """ Return the video thumbnail.

        This method should be overriden in the (Service)Video class.
        """
        raise NotImplementedError

    @property
    def videoStreamQuality(self):
        """ Return the available stream qualities of the video.

        This method should be overriden in the (Service)Video class.
        """
        raise NotImplementedError

    def download(self, defaultQuality=None):
        """ Download the video.

        This method should be overriden in the (Service)Video class.
        """
        raise NotImplementedError


class YouTubeVideo(Video):

    def __init__(self, url, progress_callback=None):
        super().__init__(url, progress_callback)
        self.yt = YouTube(self.url, on_progress_callback=self.progress_callback)

    @property
    def videoId(self):
        return pytube.extract.video_id(self.url)

    @property
    def videoTitle(self):
        return self.yt.title

    @property
    def videoThumbnail(self):
        return self.yt.thumbnail_url

    @property
    def videoStreamQuality(self):
        """ Get the available stream qualities of the video.

        Override the same method in the Video class.

        Returns:
        A list of stream object consisting of the available stream qualities for the video

        """
        return self.yt.streams.all()

    def download(self, folder='./downloads', quality=None):
        """ Download the video. Default save location is './downloads'

        Override the same method in the Video class.

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        # TODO: support manual directory entry
        if quality is None:
            self.yt.streams.first().download(folder)
