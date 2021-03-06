import pytube
import os

from pytube import YouTube, Playlist
from pytube.exceptions import RegexMatchError, VideoUnavailable

from helpers import DEFAULT_DIRECTORY, logger

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
        self.url = str(url)
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
    def allVideoStreams(self):
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
    """ Container for the YouTube video data."""

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
            logger.info(f"URL: {self.url}")
        except RegexMatchError:
            # Catches a Regex Error from URLs with invalid format
            logger.error("Caught error: RegexMatchError")
            logger.error(f"Inputted link \"{url}\" is not a valid URL")
            self.error = f"{url} is an invalid URL"
        except VideoUnavailable:
            # Catches a VideoUnavailable Error if pytube cannot
            # process the video
            logger.error(f"Caught error: VideoUnavailable")
            logger.error(f"Inputted link \"{url}\" does not exist")
            self.error = f"{url} does not exist"
        except Exception as errorMessage:
            # Catches any other unexpected error
            exceptionName = errorMessage.__class__.__name__
            self.logger.error(f"General Error Caught: {exceptionName}")
            self.logger.error(f"{errorMessage}")
            self.error = f"{exceptionName}:\n{errorMessage}"

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
            logger.info(f"Video Title: {self.yt.title}")
            return self.yt.title

    @property
    def videoThumbnail(self):
        """ Return the video thumbnail.

        Override the correspondent method in the Video class.

        """
        if not self.error:
            logger.info(f"Video Thumbnail: {self.yt.thumbnail_url}")
            return self.yt.thumbnail_url

    @property
    def allVideoStreams(self):
        """ Get all available streams of the video.

        Override the correspondent method in the Video class.

        Returns:
        A list of stream objects consisting of the available stream qualities for the video

        """
        if not self.error:
            return self.yt.streams.all()

    @property
    def audioStreams(self):
        """ Get audio streams of the video.

        Override the correspondent method in the Video class.

        Returns:
        A list of audio stream objects consisting of the available stream qualities for the video

        """
        return self.yt.streams.filter(only_audio=True).all()

    @property
    def adaptiveVideoStreams(self):
        """ Get adaptive streams of the video.

        Override the correspondent method in the Video class.

        Returns:
        A list of adaptive stream objects consisting of the available stream qualities for the video

        """
        return self.yt.streams.filter(adaptive=True).all()

    @property
    def progressiveVideoStreams(self):
        """ Get progressive streams of the video.

        Override the correspondent method in the Video class.

        Returns:
        A list of progressive stream objects consisting of the available stream qualities for the video

        """
        return self.yt.streams.filter(progressive=True)

    def download(self, location=DEFAULT_DIRECTORY, itag=None):
        """ Download the video. Default save location is './downloads'

        Override the same method in the Video class.

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        if not self.error:
            if itag is None:
                # This will often be a progressive stream, which audio is included
                self.yt.streams.first().download(location)
            else:
                # download video stream
                stream = self.yt.streams.get_by_itag(itag)
                video_filename = f"{self.yt.title} ({stream.resolution or stream.abr})"
                stream.download(output_path=location, filename=video_filename)
                # TODO: re-enable for adaptive stream support
                """
                # download audio stream for adaptive streams
                audio_filename = self.yt.streams.filter(
                    only_audio=True).first().download(output_path=location)
                # get absolute path
                os.path.abspath(location)
                """


class YouTubePlaylist():
    def __init__(self, url):
        """ Construct the YouTube playlist object.

        args:
            url: The URL of a YouTube playlist            

        """
        self.error = False
        try:
            self.playlist = Playlist(url)
            self.playlist_urls = [video for video in self.playlist]
            self.playlist_length = len(self.playlist_urls)
            # self.playlist_video_objects = self.gen_youtube_playlist_videos()
        except Exception as errorMessage:
            self.error = True
            # Catches any other unexpected error
            exceptionName = errorMessage.__class__.__name__
            self.logger.error(f"General Error Caught: {exceptionName}")
            self.logger.error(f"{errorMessage}")
            self.error = f"{exceptionName}:\n{errorMessage}"

    @property
    def playlist_size(self):
        """ Returns number of videos in the playlist

        args:
            None            

        """
        return self.playlist_length

    @property
    def get_playlist_urls(self):
        """ Returns list of video urls in the playlist

        args:
            None            

        """
        return self.playlist_urls


'''
    def gen_youtube_playlist_videos(self):
        # return YouTube objects
        n = 1
        for url in self.playlist_urls:
            yield YouTubeVideo(url)
            print(f"{n}/{self.playlist_length}")
            n = n + 1
'''
