
import sys
import os
import urllib
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from core import YouTubeVideo

ytube = None
directory = None


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        script_path = (os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(f'{script_path}/ui/qt.ui', self)

        # connect buttons and functions
        self.btnOK.clicked.connect(self.enterURL)
        self.btnDownload.clicked.connect(self.download)
        self.btnDownloadLocation.clicked.connect(self.getSaveLocation)

        # test URL
        self.lineEditURL.setText("https://www.youtube.com/watch?v=9bZkp7q19f0")

        self.show()

    def enterURL(self):

        link = self.lineEditURL.text()
        global ytube
        ytube = YouTubeVideo(link)
        self.labelVideoTitle.setText(ytube.getYoutubeVideoTitle())

        thumbnail_data = urllib.request.urlopen(
            ytube.getVideoThumbnail()).read()
        pixmap = QPixmap()
        pixmap.loadFromData(thumbnail_data)
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labelThumbnail.setPixmap(pixmap)

        print(f"URL: {link}")
        print(f"Video Title: {ytube.getYoutubeVideoTitle()}")
        print(f"Video Thumbnail: {ytube.getVideoThumbnail()}")
        print(f"Video Streams: {ytube.getStreamQuality()}")

    def getSaveLocation(self):
        global directory
        directory = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        print(directory)

    def download(self):
        if ytube is not None:
            ytube.download(directory)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
