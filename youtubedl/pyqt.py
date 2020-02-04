import sys
import time
import os
import urllib
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from pytube import YouTube

from core import getVideoThumbnail
from helpers import Helpers


ytube = None
directory = None


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

        self.show()

    def enterURL(self):
        """ When OK button is pressed.         
        Retreive information of the video using pytube using the URL entered and process it        

        """

        link = self.lineEditURL.text()
        global ytube
        ytube = YouTube(link, on_progress_callback=self.download_progress)

        # Display video title
        self.labelVideoTitle.setText(ytube.title)

        # Display thumbnail image
        thumbnail_data = urllib.request.urlopen(
            getVideoThumbnail(ytube.video_id)).read()
        pixmap = QPixmap()
        pixmap.loadFromData(thumbnail_data)
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labelThumbnail.setPixmap(pixmap)

        # debug information
        self.logger.info(f"URL: {link}")
        self.logger.info(f"Video Title: {ytube.title}")
        self.logger.info(
            f"Video Thumbnail: {getVideoThumbnail(ytube.video_id)}")

    def getSaveLocation(self):
        """ Get user selected directory when the get location button is clicked.
        """
        global directory
        directory = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.lineEditDownloadLocation.setText(directory)
        self.logger.info(f"function: getSaveLocation - directory: {directory}")

    def onSaveLocationChange(self):
        """ Get save location by user text input
        """
        global directory
        entered_directory = self.lineEditDownloadLocation.text()
        # check if directory exist
        if not os.path.isdir(entered_directory):
            self.lineEditDownloadLocation.setText("")
            self.showPopUp("Directory is not valid. Please re select")
        else:
            directory = entered_directory
        self.logger.info(
            f"function: onSaveLocationChange - directory: {directory}")

    def download_button(self):
        """ When download button is pressed
        """
        global ytube
        global directory

        if ytube is not None:
            self.download(directory)

    def showPopUp(self, message):
        """ Show pop up message

        Args:
            message: The message to display        

        """
        msg = QMessageBox()
        msg.setWindowTitle(self.appName)
        msg.setText(message)
        x = msg.exec_()

    def download_progress(self, stream, chunk, file_handle, bytes_remaining):
        """
        Updates progress bar on download_progress callback
        """
        # print("on process callback")
        file_size = stream.filesize
        # print(f"{round((1 - bytes_remaining / file_size) * 100, 3)}%")
        self.progressBar.setValue(
            round((1 - bytes_remaining / file_size) * 100, 3))

    def download(self, location=None, quality=None):
        """ Download the video. Default save location is './downloads'

        Args:
            location: The location to save the video
            quality: The stream quality of the video to be downloaded

        """
        # TODO: support manual directory entry

        global ytube

        print(f"location: {location}")
        print(f"quality: {quality}")

        if location is None:
            location = './downloads'
        if quality is None:
            ytube.streams.first().download(location)

        self.showPopUp(
            f"{ytube.title} - has been downloaded successfully to {os.path.abspath(location)}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
