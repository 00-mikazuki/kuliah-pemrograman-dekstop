import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QSpinBox, QLineEdit, QDoubleSpinBox

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spin Box")
        self.resize(378, 178)
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(140, 130, 93, 28)
        self.spinBox = QSpinBox(self)
        self.spinBox.setGeometry(120, 30, 81, 22)
        self.label = QLabel(self)
        self.label.setGeometry(20, 30, 111, 16)
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(20, 70, 91, 16)
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(140, 100, 151, 16)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(240, 30, 113, 22)
        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(240, 60, 113, 22)
        self.doubleSpinBox = QDoubleSpinBox(self)
        self.doubleSpinBox.setGeometry(120, 70, 81, 22)
        self.doubleSpinBox.setSingleStep(0.1)
        self.pushButton.setText("Jumlahkan")
        self.label.setText("Angka pertama")
        self.label_2.setText("Angka kedua")
        self.label_3.setText("TextLabel")

        self.spinBox.editingFinished.connect(self.tampil1)
        self.doubleSpinBox.editingFinished.connect(self.tampil2)
        self.pushButton.clicked.connect(self.calculate)

    def tampil1(self):
        self.lineEdit.setText(str(self.spinBox.value()))

    def tampil2(self):
        self.lineEdit_2.setText(str(self.doubleSpinBox.value()))

    def calculate(self):
        jumlah = self.spinBox.value() + self.doubleSpinBox.value()
        self.label_3.setText('Sum is: ' + str(jumlah))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec()