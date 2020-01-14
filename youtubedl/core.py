from pytube import YouTube

# https://python-pytube.readthedocs.io/en/latest/user/quickstart.html


class YouTubeVideo:
    def __init__(self, link):
        self.yt = YouTube(link)

    def getYoutubeVideoTitle(self):
        return self.yt.title

    def getVideoThumbnail(self):
        return f'https://img.youtube.com/vi/{self.yt.video_id}/maxresdefault.jpg'

    def getStreamQuality(self):
        return self.yt.streams.all()