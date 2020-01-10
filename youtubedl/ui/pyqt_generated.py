from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('qt.ui', self)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
