import sys
import urllib
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from core import YouTubeVideo


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/qt.ui', self)

        self.btnOK.clicked.connect(self.enterURL)
        # test URL
        self.lineEditURL.setText("https://www.youtube.com/watch?v=9bZkp7q19f0")

        self.show()

    def enterURL(self):

        link = self.lineEditURL.text()
        yt = YouTubeVideo(link)
        self.labelVideoTitle.setText(yt.getYoutubeVideoTitle())

        thumbnail_data = urllib.request.urlopen(yt.getVideoThumbnail()).read()
        pixmap = QPixmap()
        pixmap.loadFromData(thumbnail_data)
        pixmap = pixmap.scaled(
            230, 230, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labelThumbnail.setPixmap(pixmap)

        print(f"URL: {link}")
        print(f"Video Title: {yt.getYoutubeVideoTitle()}")
        print(f"Video Thumbnail: {yt.getVideoThumbnail()}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
