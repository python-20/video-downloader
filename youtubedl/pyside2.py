# https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file = QFile("youtubedl/ui/qt.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()

    sys.exit(app.exec_())
