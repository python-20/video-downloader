

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        script_path = (os.path.dirname(os.path.realpath(__file__)))
        uic.loadUi(f'{script_path}/ui/qt.ui', self)

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
        print(f"Video Streams: {yt.getStreamQuality()}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()