import sys
from PyQt5 import QtWidgets, uic
from core import YouTubeVideo


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/qt.ui', self)

        self.btnOK.clicked.connect(self.enterURL)

        self.show()

    def enterURL(self):
        link = self.lineEditURL.text()
        title = YouTubeVideo(link).getYoutubeVideoTitle()
        print(f"URL: {link}")

        print(f"Video Title: {title}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
