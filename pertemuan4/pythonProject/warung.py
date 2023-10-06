import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QCheckBox

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warung")
        self.resize(310, 360)
        self.checkBox = QCheckBox(self)
        self.checkBox.setGeometry(90, 70, 141, 20)
        self.checkBox_2 = QCheckBox(self)
        self.checkBox_2.setGeometry(90, 110, 121, 20)
        self.checkBox_3 = QCheckBox(self)
        self.checkBox_3.setGeometry(90, 150, 111, 20)
        self.checkBox_4 = QCheckBox(self)
        self.checkBox_4.setGeometry(90, 190, 111, 20)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(110, 240, 93, 28)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(120, 300, 113, 22)
        self.label = QLabel(self)
        self.label.setGeometry(40, 300, 81, 16)
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(90, 10, 201, 41)
        self.checkBox.setText("Pecel 10.000")
        self.checkBox_2.setText("Nasgor 12.000")
        self.checkBox_3.setText("Sop 12.000")
        self.checkBox_4.setText("Lodeh 13.000")
        self.pushButton.setText("Hitung")
        self.lineEdit.setText("0")
        self.label.setText("Total Harga:")
        self.label_2.setText("Warung Kita")

        font = self.label_2.font()
        font.setPointSize(19)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        res = 0
        if self.checkBox.isChecked():
            res = res + 10000
        if self.checkBox_2.isChecked():
            res = res + 12000
        if self.checkBox_3.isChecked():
            res = res + 12000
        if self.checkBox_4.isChecked():
            res = res + 13000
        self.lineEdit.setText(str(res))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec()