import random
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        f = self.label.font()
        f.setPointSize(25)
        self.label.setAlignment( Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter )
        self.label.setFont(f)
        self.pushButton.pressed.connect(self.update_label)
    def update_label(self):
        n = random.randint(1, 6)
        self.label.setText("%d" % n)

app = QApplication(sys.argv)
w = MainWindow()
app.exec()
