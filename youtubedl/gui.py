import sys
import os
import urllib

from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence

from PyQt5.QtCore import Qt, QThread


from core import YouTubeVideo, YouTubePlaylist
from helpers import APP_NAME, DEFAULT_DIRECTORY, DEFAULT_URL, logger


class VideoThread(QThread):

    signalStatus = QtCore.pyqtSignal(str)

    def __init__(self, url):
        QThread.__init__(self)
        print("Thread Initialized")
        self.url = url

    def run(self):
        print("Thread Started")
        self.getVideoObject()
        self.signalStatus.emit('Idle')

    def getVideoObject(self):
        return YouTubeVideo(self.url)


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()

        self._initializeAndSetup()
        self._connectSignals()
        self.show()

    def _connectSignals(self):
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
        self.btnPlaylistDownload.clicked.connect(self.playlistDownloadSelected)
        self.checkBoxPlaylistSelectAll.stateChanged.connect(
            self.playlistSelectAllChanged)

    def _initializeAndSetup(self):
        # define paths
        self.appName = APP_NAME
        self.appPath = (os.path.dirname(os.path.realpath(__file__)))

        # load ui file
        uic.loadUi(f'{self.appPath}/ui/qt.ui', self)

        # set window icon
        self.setWindowIcon(QtGui.QIcon(
            f'{self.appPath}/ui/img/title-bar-icon.png'))

        # initialize controls
        self.progressBar.setValue(0)  # progress bar value to 0
        self.checkBoxVideo.setChecked(True)
        self.btnDownload.setEnabled(False)

        # test URL
        self.lineEditPlaylistURL.setText(
            "https://www.youtube.com/playlist?list=PLE-H3cfY2nKOgX-bjk_5ObFYtgHw9BI8j")

        shortcut = QShortcut(QKeySequence("Ctrl+Shift+U"), self.lineEditURL)
        shortcut.activated.connect(
            lambda: self.lineEditURL.setText(DEFAULT_URL))
        shortcut.setEnabled(True)

        # user directory (chosen for the download)
        self.user_directory = DEFAULT_DIRECTORY

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
        # first clear what is in the listwidget
        self.listWidgetPlaylistVideos.clear()

        self.youtube_pl = YouTubePlaylist(self.lineEditPlaylistURL.text())
        if self.youtube_pl.error:
            self.showPopUp(self.youtube_pl.error)
            return
        self.playlist_video_objects = []
        n = 1
        for video_url in self.youtube_pl.get_playlist_urls:

            self.worker = VideoThread(video_url)
            # self.worker = QtCore.QThread(parent=self)
            # self.worker.moveToThread(self.worker_thread)
            self.worker.start()

            video_stream_object = self.worker.getVideoObject()
            self.playlist_video_objects.append(video_stream_object)

            item = QtWidgets.QListWidgetItem()
            item.setText(video_stream_object.videoTitle)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Checked)
            self.listWidgetPlaylistVideos.addItem(item)

            self.labelPlayListProgress.setText(
                f"{n}/{self.youtube_pl.playlist_length}")

            self.labelPlayListProgress.setText(print(
                f"{n}/{self.youtube_pl.playlist_length}"))
            n = n + 1

    def playlistDownloadSelected(self):
        """ Execute when Download Selected button is pressed in the youtube playlist tab.
        Downloads all selected videos to the default directory
        """
        print("==== Starting download ===")
        for index in range(self.listWidgetPlaylistVideos.count()):
            if self.listWidgetPlaylistVideos.item(index).checkState() == Qt.Checked:
                self.playlist_video_objects[index].download()
        print("==== Download completed ====")

    def playlistSelectAllChanged(self):
        """ Execute when Select All button is pressed in the youtube playlist tab.
        Selects and Deselects all the videos in the list widget
        """
        if self.checkBoxPlaylistSelectAll.isChecked():
            for index in range(self.listWidgetPlaylistVideos.count()):
                self.listWidgetPlaylistVideos.item(
                    index).setCheckState(QtCore.Qt.Checked)
        else:
            for index in range(self.listWidgetPlaylistVideos.count()):
                self.listWidgetPlaylistVideos.item(
                    index).setCheckState(QtCore.Qt.Unchecked)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
