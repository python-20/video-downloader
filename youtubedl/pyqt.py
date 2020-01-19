import sys
import os
import urllib
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from core import YouTubeVideo
from helpers import Helpers

ytube = None
directory = None

# logging.basicConfig(level=logging.INFO, filename=f'{self.appName}.log', filemode='w')


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.appName = "Video Downloader"
        self.logger = Helpers.logging_setup("logs/", self.appName)
        script_path = (os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(f'{script_path}/ui/qt.ui', self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon(
            f'{script_path}/ui/img/title-bar-icon.png'))

        # connect buttons and functions
        self.btnOK.clicked.connect(self.enterURL)
        self.btnDownload.clicked.connect(self.download)
        self.btnDownloadLocation.clicked.connect(self.getSaveLocation)
        self.lineEditDownloadLocation.returnPressed.connect(
            self.onSaveLocationChange)

        # test URL
        self.lineEditURL.setText("https://www.youtube.com/watch?v=9bZkp7q19f0")

        self.show()

    def enterURL(self):
        """ When OK button is pressed.         
        Retreive information of the video using pytube using the URL entered and process it        

        """

        link = self.lineEditURL.text()
        global ytube
        ytube = YouTubeVideo(link)

        # Display video title
        self.labelVideoTitle.setText(ytube.getYoutubeVideoTitle())

        # Display thumbnail image
        thumbnail_data = urllib.request.urlopen(
            ytube.getVideoThumbnail()).read()
        pixmap = QPixmap()
        pixmap.loadFromData(thumbnail_data)
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labelThumbnail.setPixmap(pixmap)

        # debug information
        self.logger.info(f"URL: {link}")
        self.logger.info(f"Video Title: {ytube.getYoutubeVideoTitle()}")
        self.logger.info(f"Video Thumbnail: {ytube.getVideoThumbnail()}")

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

    def download(self):
        """ When download button is pressed
        """
        if ytube is not None:
            ytube.download(directory)

    def showPopUp(self, message):
        """ Show pop up message

        Args:
            message: The message to display        

        """
        msg = QMessageBox()
        msg.setWindowTitle(self.appName)
        msg.setText(message)
        x = msg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
