from pytube import YouTube

# https://python-pytube.readthedocs.io/en/latest/user/quickstart.html


def getVideoThumbnail(video_id):
    """ Get the video thumbnail

    Returns:
    URL of the thumbnail of the video

    """
    return f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'


class YouTubeVideo:

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

    def download_progress(self, stream, chunk, file_handle, bytes_remaining):
        # print("on process callback")
        file_size = stream.filesize
        # print(f"{round((1 - bytes_remaining / file_size) * 100, 3)}%")
        self.progress = round((1 - bytes_remaining / file_size) * 100, 3)
