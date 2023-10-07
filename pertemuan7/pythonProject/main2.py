import os
import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
basedir = os.path.dirname(__file__)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join(basedir, "window.ui"), self)
        self.pushButton.clicked.connect(self.btn_clicked)
    def btn_clicked(self):
        self.label_2.setText(self.lineEdit.text())

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
