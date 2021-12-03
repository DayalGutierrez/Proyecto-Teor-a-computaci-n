from PySide2.QtWidgets import QApplication
from controllers.mainwindow import MaquinaExpendedoraWindow
import sys

if __name__ == '__main__':
    app = QApplication()
    window = MaquinaExpendedoraWindow()
    window.show()
    app.exec_()
