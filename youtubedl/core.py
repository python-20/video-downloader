from pytube import YouTube

# https://python-pytube.readthedocs.io/en/latest/user/quickstart.html


class YouTubeVideo:
    def __init__(self, link):
        self.yt = YouTube(link)

    # fetch new link

    def getYoutubeVideoTitle(self):
        """ Get the video title

        Returns:
        Title of the video

        """
        return self.yt.title

    def getVideoThumbnail(self):
        """ Get the video thumbnail

        Returns:
        URL of the thumbnail of the video

        """
        return f'https://img.youtube.com/vi/{self.yt.video_id}/maxresdefault.jpg'

    def getStreamQuality(self):
        """ Get the available stream qualties of the video

        Returns:
        A list of stream object consist of the available stream qualities for the video

        """
        return self.yt.streams.all()

    def download(self, location=None, quality=None):
        """ Download the video. Default save location is './downloads'

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        # TODO: support manual directory entry
        if location is None:
            location = './downloads'
        if quality is None:
            self.yt.streams.first().download(location)
