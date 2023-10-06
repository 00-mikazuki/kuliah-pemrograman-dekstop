import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QPushButton, QLabel


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator Sederhana")
        self.resize(290, 415)
        self.radioButton = QRadioButton(self)
        self.radioButton.setGeometry(60, 110, 95, 20)
        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setGeometry(60, 150, 95, 20)
        self.radioButton_3 = QRadioButton(self)
        self.radioButton_3.setGeometry(60, 190, 95, 20)
        self.radioButton_4 = QRadioButton(self)
        self.radioButton_4.setGeometry(60, 230, 95, 20)
        self.label = QLabel(self)
        self.label.setGeometry(20, 270, 121, 16)
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(20, 30, 131, 16)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(160, 30, 113, 22)
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(160, 70, 113, 22)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(120, 310, 93, 28)
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(20, 70, 131, 16)
        # self.label_3.setObjectName("label_3")

        self.radioButton.setText("Tambah")
        self.radioButton_2.setText("Kurang")
        self.radioButton_3.setText("Kali")
        self.radioButton_4.setText("Bagi")
        self.label.setText("TextLabel")
        self.label_2.setText("Enter First Number")
        self.pushButton.setText("PushButton")
        self.label_3.setText("Enter Second Number")
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        result = 0
        if len(self.lineEdit.text()) != 0:
            a = int(self.lineEdit.text())
        else:
            a = 0
        if len(self.lineEdit_2.text()) != 0:
            b = int(self.lineEdit_2.text())
        else:
            b = 0
        if self.radioButton.isChecked():
            result = a + b
        if self.radioButton_2.isChecked():
            result = a - b
        if self.radioButton_3.isChecked():
            result = a * b
        if self.radioButton_4.isChecked():
            result = a / b
        self.label.setText("Hasil: " + str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec()