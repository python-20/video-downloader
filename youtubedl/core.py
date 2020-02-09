import pytube
import os

from helpers import Helpers
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

# https://python-pytube3.readthedocs.io/en/latest/user/quickstart.html


class Video:
    """ Base class for the (Service)Video object.

    This is an interface class, it should not be used directly. A new video
    service is registered by subclassing it.
    """

    def __init__(self, url, progress_callback=None):
        """ Initialize the Video object.

        Args:
            url: The URL of the video
            progress_callback: The name of the callback function to be called
        """
        self.url = url
        self.progress_callback = progress_callback
        self.logger = Helpers.logging_setup("logs/", "Video Downloader")

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
    """ Container for the YouTube video data.
    """

    def __init__(self, url, progress_callback=None):
        """ Construct the YouTubeVideo object.

        args:
            url: The URL of a YouTube video
            progress_callback: The name of the callback function to be called
        """
        super().__init__(url, progress_callback)
        self.error = False
        try:
            self.yt = YouTube(
                url, on_progress_callback=progress_callback)
        except RegexMatchError:
            # Catches a Regex Error from URLs with invalid format
            self.logger.error("Caught error: RegexMatchError")
            self.logger.error(f"Inputted link \"{url}\" is not a valid URL")
            self.error = f"{url} is an invalid URL"
        except VideoUnavailable:
            # Catches a VideoUnavailable Error if pytube cannot process the video
            self.logger.error(f"Caught error: VideoUnavailable")
            self.logger.error(f"Inputted link \"{url}\" does not exist")
            self.error = f"{url} does not exist"

    @property
    def videoId(self):
        """ Return the ID of the video.

        Override the correspondent method in the Video class.

        """
        if not self.error:
            return pytube.extract.video_id(self.url)

    @property
    def videoTitle(self):
        """ Return the title of the video.

        Override the correspondent method in the Video class.

        """
        if not self.error:
            return self.yt.title

    @property
    def videoThumbnail(self):
        """ Return the video thumbnail.

        Override the correspondent method in the Video class.

        """
        if not self.error:
            return self.yt.thumbnail_url

    @property
    def allVideoStreams(self):
        """ Get all available streams of the video.

        Override the correspondent method in the Video class.

        Returns:
        A list of stream objects consisting of the available stream qualities for the video

        """
        # TODO: fix this
        if not self.error:
            return self.yt.streams.all()

    @property
    def adaptiveVideoStreams(self):
        """ Get adaptive streams of the video.

        Override the correspondent method in the Video class.

        Returns:
        A list of adaptive stream objects consisting of the available stream qualities for the video

        """
        return self.yt.streams.filter(adaptive=True).all()

    def download(self, location='./downloads', itag=None):
        """ Download the video. Default save location is './downloads'

        Override the same method in the Video class.

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        # TODO: support manual directory entry
        if not self.error:
            if itag is None:
                # This will often be a progressive stream, which audio is included
                self.yt.streams.first().download(location)
            else:
                # download video stream
                stream = self.yt.streams.get_by_itag(itag)
                video_filename = f"{self.yt.title} ({stream.resolution})"
                stream.download(output_path=location, filename=video_filename)
                # download audio stream
                audio_filename = self.yt.streams.filter(
                    only_audio=True).first().download(output_path=location)
            # os.path.abspath(location)
