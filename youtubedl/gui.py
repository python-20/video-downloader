import sys
import os
import urllib
import PyQt5
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pytube import YouTube

from core import YouTubeVideo
from helpers import APP_NAME, DEFAULT_DIRECTORY, logger
from ui.MainWindow import Ui_mainWindow

import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.appName = APP_NAME
        appPath = (os.path.dirname(os.path.realpath(__file__)))

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon(
            f'{appPath}/ui/img/title-bar-icon.png'))

        # for pyinstaller
        # self.setWindowIcon(QtGui.QIcon(
        #    resource_path('img/title-bar-icon.png')))

        # connect buttons and functions
        self.ui.btnOK.clicked.connect(self.enterURL)
        self.ui.lineEditURL.returnPressed.connect(self.enterURL)
        self.ui.btnDownload.clicked.connect(self.download_button)
        self.ui.btnDownloadLocation.clicked.connect(self.getSaveLocation)
        self.ui.lineEditDownloadLocation.returnPressed.connect(
            self.onSaveLocationChange)
        self.ui.checkBoxVideo.stateChanged.connect(self.populateComboBox)
        self.ui.checkBoxAudio.stateChanged.connect(self.populateComboBox)

        # initialize controls
        self.ui.progressBar.setValue(0)  # progress bar value to 0
        self.ui.checkBoxVideo.setChecked(True)
        self.ui.btnDownload.setEnabled(False)

        # test URL
        self.ui.lineEditURL.setText(
            "https://www.youtube.com/watch?v=7BgcG_l9J0A")

        # user directory (chosen for the download)
        self.user_directory = DEFAULT_DIRECTORY

        self.show()

    def enterURL(self):
        """ When OK button is pressed.
        Use the given URL to retrieve video information and process it
        """

        link = self.ui.lineEditURL.text()
        self.ytube = YouTubeVideo(
            link, progress_callback=self.download_progress)
        if self.ytube.error:
            self.showPopUp(self.ytube.error)
            return

        # Display video title
        self.ui.labelVideoTitle.setText(self.ytube.videoTitle)

        # Display thumbnail image
        pixmap = QPixmap()
        pixmap.loadFromData(urllib.request.urlopen(
            self.ytube.videoThumbnail).read())
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.labelThumbnail.setPixmap(pixmap)

        # Populate combo box
        self.populateComboBox()

        # enable download button
        self.ui.btnDownload.setEnabled(True)

    def populateComboBox(self):
        """ Populate stream quality combobox (comboBoxQuality)

        linked to video (checkBoxVideo) and audio (checkBoxAudio) checkbox state change

        Args:
            None

        """
        try:
            self.ui.comboBoxQuality.clear()

            # show video streams if video check box is checked
            if self.ui.checkBoxVideo.isChecked():
                streams = self.ytube.progressiveVideoStreams
                for stream in streams:
                    if stream.resolution is not None:
                        self.ui.comboBoxQuality.addItem(
                            f"{stream.resolution} - {stream.mime_type}", stream.itag)

            # show audio streams if audio check box is checked
            if self.ui.checkBoxAudio.isChecked():
                streams = self.ytube.audioStreams
                for stream in streams:
                    self.ui.comboBoxQuality.addItem(
                        f"{stream.abr} - {stream.mime_type}", stream.itag)

            # nothing is selected
            if not self.ui.checkBoxVideo.isChecked() and not self.ui.checkBoxAudio.isChecked():
                self.ui.comboBoxQuality.addItem("== No Selection ==", None)

        # ytube (YouTubeVideo Class) not defined
        except AttributeError:
            pass

    def getSaveLocation(self):
        """ Get user selected directory when the download button is clicked.
        """
        self.user_directory = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        self.lineEditDownloadLocation.setText(self.user_directory)
        logger.info(
            f"function: getSaveLocation - directory: {self.user_directory}")

    def onSaveLocationChange(self):
        """ Get save location by user text input (manual location input)
        """
        entered_directory = self.lineEditDownloadLocation.text()
        # check if directory exist
        if not os.path.isdir(entered_directory):
            self.lineEditDownloadLocation.setText("")
            self.showPopUp("Directory is not valid. Please re select")
        else:
            self.user_directory = entered_directory
        logger.info(
            f"function: onSaveLocationChange - directory: {self.user_directory}")

    def download_button(self):
        """
        When download button is pressed
        """
        # get selected stream quality (itag)

        logger.info(
            f"itag of quality selected is "
            f"{self.ui.comboBoxQuality.itemData(self.ui.comboBoxQuality.currentIndex())}")

        itag = self.ui.comboBoxQuality.itemData(
            self.ui.comboBoxQuality.currentIndex())

        if self.ytube is not None:
            self.ytube.download(location=self.user_directory, itag=itag)

        self.showPopUp(
            f"{self.ytube.videoTitle} - has been downloaded successfully to:\
        \n{os.path.abspath(self.user_directory)}")

    def showPopUp(self, message):
        """ Show pop up message

        Args:
            message: The message to display

        """
        msg = QMessageBox()
        msg.setWindowTitle(self.appName)
        msg.setText(message)
        msg.exec_()

    def download_progress(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):
        """
        Updates progress bar on download_progress callback
        """
        file_size = stream.filesize
        self.ui.progressBar.setValue(
            round((1 - bytes_remaining / file_size) * 100, 3))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
