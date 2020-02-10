import sys
from PyQt5 import QtWidgets
from gui import Ui
from helpers import logging_setup


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
