# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\-PracticeProjects\Python\video-downloader\youtubedl\ui\qt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 233)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelURL = QtWidgets.QLabel(self.centralwidget)
        self.labelURL.setGeometry(QtCore.QRect(10, 0, 91, 41))
        self.labelURL.setTextFormat(QtCore.Qt.PlainText)
        self.labelURL.setWordWrap(True)
        self.labelURL.setObjectName("labelURL")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditURL.setGeometry(QtCore.QRect(110, 10, 411, 20))
        self.lineEditURL.setObjectName("lineEditURL")
        self.toolButtonQuality = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonQuality.setGeometry(QtCore.QRect(110, 50, 25, 19))
        self.toolButtonQuality.setObjectName("toolButtonQuality")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.btnDownloadLocation = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownloadLocation.setGeometry(QtCore.QRect(10, 110, 111, 23))
        self.btnDownloadLocation.setObjectName("btnDownloadLocation")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(450, 110, 75, 23))
        self.btnDownload.setObjectName("btnDownload")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.btnClear.setObjectName("btnClear")
        self.lineEditDownloadLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDownloadLocation.setGeometry(QtCore.QRect(130, 110, 221, 20))
        self.lineEditDownloadLocation.setObjectName("lineEditDownloadLocation")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 160, 511, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelURL.setText(_translate("MainWindow", "Video/Playlist URL:"))
        self.label_2.setText(_translate("MainWindow", "File type / quality: "))
        self.toolButtonQuality.setText(_translate("MainWindow", "..."))
        self.checkBox.setText(_translate("MainWindow", "Playlist"))
        self.btnDownloadLocation.setText(_translate("MainWindow", "Download Location:"))
        self.btnDownload.setText(_translate("MainWindow", "Download"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
