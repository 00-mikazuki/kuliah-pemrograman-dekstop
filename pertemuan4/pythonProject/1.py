import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show Input")
        self.resize(280, 220)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(85, 27, 113, 22)
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(85, 68, 113, 22)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(90, 110, 93, 28)
        self.label = QLabel(self)
        self.label.setGeometry(90, 161, 125, 16)
        # self.label.setObjectName("label")
        self.pushButton.setText("PushButton")
        self.label.setText("TextLabel")
        self.pushButton.clicked.connect(self.displayMessage)

    def displayMessage(self):
        self.label.setText("Hello " + self.lineEdit.text() + " dan " + self.lineEdit_2.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec()