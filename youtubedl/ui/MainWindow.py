# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtubedl/ui/qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(535, 383)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelURL = QtWidgets.QLabel(self.centralwidget)
        self.labelURL.setGeometry(QtCore.QRect(10, 0, 91, 41))
        self.labelURL.setTextFormat(QtCore.Qt.PlainText)
        self.labelURL.setWordWrap(True)
        self.labelURL.setObjectName("labelURL")
        self.labelFileType = QtWidgets.QLabel(self.centralwidget)
        self.labelFileType.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.labelFileType.setObjectName("labelFileType")
        self.lineEditURL = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditURL.setGeometry(QtCore.QRect(110, 10, 361, 20))
        self.lineEditURL.setObjectName("lineEditURL")
        self.btnDownloadLocation = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownloadLocation.setGeometry(QtCore.QRect(470, 100, 28, 24))
        self.btnDownloadLocation.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("youtubedl/ui\\img/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDownloadLocation.setIcon(icon)
        self.btnDownloadLocation.setObjectName("btnDownloadLocation")
        self.btnDownload = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownload.setGeometry(QtCore.QRect(420, 160, 75, 20))
        self.btnDownload.setObjectName("btnDownload")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(420, 190, 75, 20))
        self.btnClear.setObjectName("btnClear")
        self.lineEditDownloadLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDownloadLocation.setGeometry(QtCore.QRect(10, 100, 451, 20))
        self.lineEditDownloadLocation.setObjectName("lineEditDownloadLocation")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 310, 511, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(480, 10, 41, 23))
        self.btnOK.setObjectName("btnOK")
        self.labelThumbnail = QtWidgets.QLabel(self.centralwidget)
        self.labelThumbnail.setGeometry(QtCore.QRect(20, 170, 231, 121))
        self.labelThumbnail.setObjectName("labelThumbnail")
        self.labelVideoTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelVideoTitle.setGeometry(QtCore.QRect(20, 130, 211, 21))
        self.labelVideoTitle.setObjectName("labelVideoTitle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label.setObjectName("label")
        self.comboBoxQuality = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxQuality.setGeometry(QtCore.QRect(110, 50, 141, 20))
        self.comboBoxQuality.setObjectName("comboBoxQuality")
        self.checkBoxAudio = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAudio.setGeometry(QtCore.QRect(310, 50, 70, 17))
        self.checkBoxAudio.setObjectName("checkBoxAudio")
        self.checkBoxVideo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxVideo.setGeometry(QtCore.QRect(260, 50, 51, 17))
        self.checkBoxVideo.setObjectName("checkBoxVideo")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Video Downloader"))
        self.labelURL.setText(_translate("mainWindow", "Video/Playlist URL:"))
        self.labelFileType.setText(_translate("mainWindow", "File type / quality: "))
        self.btnDownload.setText(_translate("mainWindow", "Download"))
        self.btnClear.setText(_translate("mainWindow", "Clear"))
        self.btnOK.setText(_translate("mainWindow", "OK"))
        self.labelThumbnail.setText(_translate("mainWindow", "<Thumbnail>"))
        self.labelVideoTitle.setText(_translate("mainWindow", "<Video Title> "))
        self.label.setText(_translate("mainWindow", "Download Location:"))
        self.checkBoxAudio.setText(_translate("mainWindow", "Audio"))
        self.checkBoxVideo.setText(_translate("mainWindow", "Video"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
