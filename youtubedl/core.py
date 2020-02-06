import pytube

from pytube import YouTube

# https://python-pytube3.readthedocs.io/en/latest/user/quickstart.html


class Video:

    @property
    def videoId(self):
        pass

    @property
    def videoTitle(self):
        pass

    @property
    def videoThumbnail(self):
        pass

    @property
    def videoStreamQuality(self):
        pass

    def download(self, defaultQuality=None):
        pass

    def download_progress(self):
        pass


class YouTubeVideo(Video):

    def __init__(self, url):
        self.url = url
        self.yt = YouTube(self.url)

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
        """ Get the available stream qualties of the video

        Returns:
        A list of stream object consist of the available stream qualities for the video

        """
        return self.yt.streams.all()

    def download(self, folder='./downloads', quality=None):
        """ Download the video. Default save location is './downloads'

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        # TODO: support manual directory entry
        if quality is None:
            self.yt.streams.first().download(folder)

    def download_progress(self, stream, chunk, file_handle, bytes_remaining):
        # print("on process callback")
        file_size = stream.filesize
        # print(f"{round((1 - bytes_remaining / file_size) * 100, 3)}%")
        self.progress = round((1 - bytes_remaining / file_size) * 100, 3)
