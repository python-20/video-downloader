import sys
import os
import urllib
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pytube import YouTube

# from core import getVideoThumbnail
from core import YouTubeVideo
from helpers import Helpers

#
from pytube import exceptions as pytubeExceptions

DEFAULT_DIRECTORY = './downloads'


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.appName = "Video Downloader"
        self.logger = Helpers.logging_setup("logs/", self.appName)
        appPath = (os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(f'{appPath}/ui/qt.ui', self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon(
            f'{appPath}/ui/img/title-bar-icon.png'))

        # connect buttons and functions
        self.btnOK.clicked.connect(self.enterURL)
        self.btnDownload.clicked.connect(self.download_button)
        self.btnDownloadLocation.clicked.connect(self.getSaveLocation)
        self.lineEditDownloadLocation.returnPressed.connect(
            self.onSaveLocationChange)

        # initialize progressbar
        self.progressBar.setValue(0)

        # test URL
        self.lineEditURL.setText("https://www.youtube.com/watch?v=9bZkp7q19f0")

        # user directory (chosen for the download)
        self.user_directory = DEFAULT_DIRECTORY

        self.show()

    def enterURL(self):
        """ When OK button is pressed.
        Use the given URL to retrieve video information and process it
        """

        link = self.lineEditURL.text()

        try:
            self.ytube = YouTubeVideo(
                link, progress_callback=self.download_progress)
        except pytubeExceptions.RegexMatchError:
            # Catches a Regex Error from URLs with invalid format
            self.showPopUp(f"{link} is an invalid URL")
            self.logger.error("Caught error: RegexMatchError")
            self.logger.error(f"Inputted link \"{link}\" is not a valid URL")
            return
        except pytubeExceptions.VideoUnavailable:
            # Catches a VideoUnavailable Error if pytube cannot process the video
            self.showPopUp(f"{link} does not exist")
            self.logger.error(f"Caught error: VideoUnavailable")
            self.logger.error(f"Inputted link \"{link}\" does not exist")
            return

        # Display video title
        self.labelVideoTitle.setText(self.ytube.videoTitle)

        # Display thumbnail image
        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(
            self.ytube.videoThumbnail).read())
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labelThumbnail.setPixmap(pixmap)

        # debug information
        self.logger.info(f"URL: {self.ytube.url}")
        self.logger.info(f"Video Title: {self.ytube.videoTitle}")
        self.logger.info(
            f"Video Thumbnail: {self.ytube.videoThumbnail}")

    def getSaveLocation(self):
        """ Get user selected directory when the get location button is clicked.
        """
        self.user_directory = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.lineEditDownloadLocation.setText(self.user_directory)
        self.logger.info(
            f"function: getSaveLocation - directory: {self.user_directory}")

    def onSaveLocationChange(self):
        """ Get save location by user text input
        """
        entered_directory = self.lineEditDownloadLocation.text()
        # check if directory exist
        if not os.path.isdir(entered_directory):
            self.lineEditDownloadLocation.setText("")
            self.showPopUp("Directory is not valid. Please re select")
        else:
            self.user_directory = entered_directory
        self.logger.info(
            f"function: onSaveLocationChange - directory: {self.user_directory}")

    def download_button(self):
        """ When download button is pressed
        """
        if self.ytube is not None:
            self.download(location=self.user_directory)

    def showPopUp(self, message):
        """ Show pop up message

        Args:
            message: The message to display

        """
        msg = QMessageBox()
        msg.setWindowTitle(self.appName)
        msg.setText(message)
        x = msg.exec_()

    def download_progress(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):
        """
        Updates progress bar on download_progress callback
        """
        file_size = stream.filesize
        self.progressBar.setValue(
            round((1 - bytes_remaining / file_size) * 100, 3))

    def download(self, location=DEFAULT_DIRECTORY, quality=None):
        """ Download the video. Default save location is './downloads'

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        # TODO: support manual directory entry

        self.logger.info(f"location: {location}")
        self.logger.info(f"quality: {quality}")

        if quality is None:
            self.ytube.download(location=location)

        self.showPopUp(
            f"{self.ytube.videoTitle} - has been downloaded successfully to:\
            \n{os.path.abspath(location)}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
