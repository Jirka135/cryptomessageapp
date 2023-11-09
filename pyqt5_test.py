from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QMainWindow
from PyQt5 import QtWidgets
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,720,1080)
    win.setWindowTitle("Crypto MessageGram")

    win.show()
    sys.exit(app.exec_())

window()