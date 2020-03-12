import sys
import os
import urllib
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from core import YouTubeVideo, YouTubePlaylist
from helpers import APP_NAME, DEFAULT_DIRECTORY, logger


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.appName = APP_NAME
        appPath = (os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(f'{appPath}/ui/qt.ui', self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon(
            f'{appPath}/ui/img/title-bar-icon.png'))

        # connect buttons and functions - youtube single video
        self.btnOK.clicked.connect(self.enterURL)
        self.lineEditURL.returnPressed.connect(self.enterURL)
        self.btnDownload.clicked.connect(self.download_button)
        self.btnDownloadLocation.clicked.connect(self.getSaveLocation)
        self.lineEditDownloadLocation.returnPressed.connect(
            self.onSaveLocationChange)
        self.checkBoxVideo.stateChanged.connect(self.populateComboBox)
        self.checkBoxAudio.stateChanged.connect(self.populateComboBox)

        # connect buttons and functions - youtube playlist
        self.btnOK_playlist.clicked.connect(self.enterPlaylistURL)

        # initialize controls
        self.progressBar.setValue(0)  # progress bar value to 0
        self.checkBoxVideo.setChecked(True)
        self.btnDownload.setEnabled(False)

        # test URL
        self.lineEditURL.setText("https://www.youtube.com/watch?v=7BgcG_l9J0A")
        self.lineEditPlaylistURL.setText(
            "https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p")

        # user directory (chosen for the download)
        self.user_directory = DEFAULT_DIRECTORY

        self.show()

    ########## youtube single video tab ###################

    def enterURL(self):
        """ When OK button is pressed.
        Use the given URL to retrieve video information and process it
        """

        link = self.lineEditURL.text()
        self.ytube = YouTubeVideo(
            link, progress_callback=self.download_progress)
        if self.ytube.error:
            self.showPopUp(self.ytube.error)
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

        # Populate combo box
        self.populateComboBox()

        # enable download button
        self.btnDownload.setEnabled(True)

    def populateComboBox(self):
        """ Populate stream quality combobox (comboBoxQuality)

        linked to video (checkBoxVideo) and audio (checkBoxAudio) checkbox state change

        Args:
            None

        """
        try:
            self.comboBoxQuality.clear()

            # show video streams if video check box is checked
            if self.checkBoxVideo.isChecked():
                streams = self.ytube.progressiveVideoStreams
                for stream in streams:
                    if stream.resolution is not None:
                        self.comboBoxQuality.addItem(
                            f"{stream.resolution} - {stream.mime_type}", stream.itag)

            # show audio streams if audio check box is checked
            if self.checkBoxAudio.isChecked():
                streams = self.ytube.audioStreams
                for stream in streams:
                    self.comboBoxQuality.addItem(
                        f"{stream.abr} - {stream.mime_type}", stream.itag)

            # nothing is selected
            if not self.checkBoxVideo.isChecked() and not self.checkBoxAudio.isChecked():
                self.comboBoxQuality.addItem("== No Selection ==", None)

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
            f"{self.comboBoxQuality.itemData(self.comboBoxQuality.currentIndex())}")

        itag = self.comboBoxQuality.itemData(
            self.comboBoxQuality.currentIndex())

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

    def download_progress(self, stream=None, chunk=None, bytes_remaining=None):
        """
        Updates progress bar on download_progress callback
        """
        file_size = stream.filesize
        self.progressBar.setValue(
            round((1 - bytes_remaining / file_size) * 100, 3))

    ########## youtube playlist tab ###################

    def enterPlaylistURL(self):
        """ Execute when OK button is pressed in the youtube playlist tab.
        Use the given URL to retrieve video information and process it
        """
        self.youtube_pl = YouTubePlaylist(self.lineEditPlaylistURL.text())
        if self.youtube_pl.error:
            self.showPopUp(self.youtube_pl.error)
            return

        for video in self.youtube_pl.get_youtube_playlist_videos():
            item = QtWidgets.QListWidgetItem()
            item.setText(video.videoTitle)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidgetPlaylistVideos.addItem(item)
        # self.listWidgetPlaylistVideos.addItems(
        #    self.youtube_pl.get_youtube_playlist_videos())


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
