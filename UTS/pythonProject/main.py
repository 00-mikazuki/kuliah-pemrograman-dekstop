import os
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
    QTabWidget,
)

from PyQt6 import QtCore, QtGui, QtWidgets

from layout_colorwidget import Color

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.resize(250, 300)

        # Menu
        self.button_penjumlahan = QAction(
            QIcon(os.path.join(basedir, "img/plus.png")),
            "&Penjumlahan",
            self,
        )
        self.button_penjumlahan.setStatusTip("Penjumlahan")
        self.button_penjumlahan.setCheckable(True)
        self.button_penjumlahan.setChecked(True)
        self.button_penjumlahan.triggered.connect(self.buttonPenjumlahanClicked)

        self.button_pengurangan = QAction(
            QIcon(os.path.join(basedir, "img/minus.png")),
            "&Pengurangan",
            self,
        )
        self.button_pengurangan.setStatusTip("Pengurangan")
        self.button_pengurangan.setCheckable(True)
        self.button_pengurangan.triggered.connect(self.buttonPenguranganClicked)

        self.button_perkalian = QAction(
            QIcon(os.path.join(basedir, "img/times.png")),
            "&Perkalian",
            self,
        )
        self.button_perkalian.setStatusTip("Perkalian")
        self.button_perkalian.setCheckable(True)
        self.button_perkalian.triggered.connect(self.buttonPerkalianClicked)

        self.button_pembagian = QAction(
            QIcon(os.path.join(basedir, "img/divide.png")),
            "&Pembagian",
            self,
        )
        self.button_pembagian.setStatusTip("Pembagian")
        self.button_pembagian.setCheckable(True)
        self.button_pembagian.triggered.connect(self.buttonPembagianClicked)

        self.setStatusBar(QStatusBar(self))
        self.menu = self.menuBar()

        self.operation_menu = self.menu.addMenu("&Operasi Matematika")
        self.operation_menu.addAction(self.button_penjumlahan)
        self.operation_menu.addAction(self.button_pengurangan)
        self.operation_menu.addAction(self.button_perkalian)
        self.operation_menu.addAction(self.button_pembagian)

        # Grid Items
        self.labelNum1 = QLabel("num1 :")
        self.dispAngka1 = QLineEdit(self)
        self.dispAngka1.setText("0")
        self.dispAngka1.setEnabled(False)
        self.fontDispAngka1 = self.dispAngka1.font()
        self.fontDispAngka1.setBold(True)
        self.dispAngka1.setFont(self.fontDispAngka1)
        self.labelNum2 = QLabel("num2 :")
        self.dispAngka2 = QLineEdit(self)
        self.dispAngka2.setText("0")
        self.dispAngka2.setEnabled(False)
        self.fontDispAngka2 = self.dispAngka2.font()
        self.fontDispAngka2.setBold(False)
        self.dispAngka2.setFont(self.fontDispAngka2)
        self.labelOp = QLabel("+")
        self.labelEq = QLabel("=")
        self.labelHasil = QLabel("result :")
        self.dispHasil = QLineEdit(self)
        self.dispHasil.setText("0")
        self.dispHasil.setEnabled(False)
        self.fontDispHasil = self.dispHasil.font()
        self.fontDispHasil.setBold(False)
        self.dispHasil.setFont(self.fontDispHasil)
        self.button0 = QPushButton("0")
        self.button0.clicked.connect(self.buttonClick0)
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton("3")
        self.button3.clicked.connect(self.buttonClick3)
        self.button4 = QPushButton("4")
        self.button4.clicked.connect(self.buttonClick4)
        self.button5 = QPushButton("5")
        self.button5.clicked.connect(self.buttonClick5)
        self.button6 = QPushButton("6")
        self.button6.clicked.connect(self.buttonClick6)
        self.button7 = QPushButton("7")
        self.button8 = QPushButton(self)
        self.button9 = QPushButton(self)
        self.button7.clicked.connect(self.buttonClick7)
        self.buttonDel = QPushButton("clear")
        self.buttonDel.clicked.connect(self.clear)
        self.buttonNext = QPushButton("next")
        self.buttonNext.clicked.connect(self.endLine)
        self.buttonNext.clicked.connect(self.calculate)

        # VH Items
        self.labelNum1VH = QLabel("num1 :")
        self.dispAngka1VH = QLineEdit(self)
        self.dispAngka1VH.setText("0")
        self.dispAngka1VH.setEnabled(False)
        self.fontDispAngka1VH = self.dispAngka1VH.font()
        self.fontDispAngka1VH.setBold(True)
        self.dispAngka1VH.setFont(self.fontDispAngka1VH)
        self.labelNum2VH = QLabel("num2 :")
        self.dispAngka2VH = QLineEdit(self)
        self.dispAngka2VH.setText("0")
        self.dispAngka2VH.setEnabled(False)
        self.fontDispAngka2VH = self.dispAngka2.font()
        self.fontDispAngka2VH.setBold(False)
        self.dispAngka2VH.setFont(self.fontDispAngka2VH)
        self.labelOpVH = QLabel("+")
        self.labelEqVH = QLabel("=")
        self.labelHasilVH = QLabel("result :")
        self.dispHasilVH = QLineEdit(self)
        self.dispHasilVH.setText("0")
        self.dispHasilVH.setEnabled(False)
        self.fontDispHasilVH = self.dispHasilVH.font()
        self.fontDispHasilVH.setBold(False)
        self.dispHasilVH.setFont(self.fontDispHasilVH)
        self.button0VH = QPushButton("0")
        self.button0VH.clicked.connect(self.buttonClick0)
        self.button3VH = QPushButton("3")
        self.button3VH.clicked.connect(self.buttonClick3)
        self.button4VH = QPushButton("4")
        self.button4VH.clicked.connect(self.buttonClick4)
        self.button5VH = QPushButton("5")
        self.button5VH.clicked.connect(self.buttonClick5)
        self.button6VH = QPushButton("6")
        self.button6VH.clicked.connect(self.buttonClick6)
        self.button7VH = QPushButton("7")
        self.button7VH.clicked.connect(self.buttonClick7)
        self.buttonDelVH = QPushButton("clear")
        self.buttonDelVH.clicked.connect(self.clear)
        self.buttonNextVH = QPushButton("next")
        self.buttonNextVH.clicked.connect(self.endLine)
        self.buttonNextVH.clicked.connect(self.calculate)

        # Layout Grid
        self.containerGrid = QGridLayout()

        self.containerGrid.addWidget(self.labelNum1, 0, 0)
        self.containerGrid.addWidget(self.dispAngka1, 0, 1, 1, 2)
        self.containerGrid.addWidget(self.labelOp, 1, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.containerGrid.addWidget(self.labelNum2, 2, 0)
        self.containerGrid.addWidget(self.dispAngka2, 2, 1, 1, 2)
        self.containerGrid.addWidget(self.labelEq, 3, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)
        self.containerGrid.addWidget(self.labelHasil, 4, 0)
        self.containerGrid.addWidget(self.dispHasil, 4, 1, 1, 2)
        self.containerGrid.addWidget(self.button1, 5, 0)
        self.containerGrid.addWidget(self.button2, 5, 1)
        self.containerGrid.addWidget(self.button3, 5, 2)
        self.containerGrid.addWidget(self.button4, 6, 0)
        self.containerGrid.addWidget(self.button5, 6, 1)
        self.containerGrid.addWidget(self.button6, 6, 2)
        self.containerGrid.addWidget(self.button7, 7, 0)
        self.containerGrid.addWidget(self.button8, 7, 1)
        self.containerGrid.addWidget(self.button9, 7, 2)
        self.containerGrid.addWidget(self.button0, 8, 1)
        self.containerGrid.addWidget(self.buttonDel, 8, 0)
        self.containerGrid.addWidget(self.buttonNext, 8, 2)

        # Layout VH
        self.containerVH = QVBoxLayout()
        self.layout1VH = QHBoxLayout()
        self.layout2VH = QHBoxLayout()
        self.layout3VH = QHBoxLayout()
        self.layout4VH = QHBoxLayout()
        self.layout5VH = QHBoxLayout()

        self.layout1VH.addWidget(self.dispAngka1VH)
        self.layout1VH.addWidget(self.labelOpVH)
        self.layout1VH.addWidget(self.dispAngka2VH)
        self.layout1VH.addWidget(self.labelEqVH)
        self.layout1VH.addWidget(self.dispHasilVH)
        self.layout2VH.addWidget(self.button0VH)
        self.layout2VH.addWidget(self.button3VH)
        self.layout3VH.addWidget(self.button4VH)
        self.layout3VH.addWidget(self.button5VH)
        self.layout4VH.addWidget(self.button6VH)
        self.layout4VH.addWidget(self.button7VH)
        self.layout5VH.addWidget(self.buttonDelVH)
        self.layout5VH.addWidget(self.buttonNextVH)
        
        self.containerVH.addLayout(self.layout1VH)
        self.containerVH.addLayout(self.layout2VH)
        self.containerVH.addLayout(self.layout3VH)
        self.containerVH.addLayout(self.layout4VH)
        self.containerVH.addLayout(self.layout5VH)

        # Widget
        self.widgetGrid = QWidget()
        self.widgetGrid.setLayout(self.containerGrid)
        self.widgetVH = QWidget()
        self.widgetVH.setLayout(self.containerVH)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.tabs.addTab(self.widgetVH, "VH")
        self.tabs.addTab(self.widgetGrid, "Grid")
        
        self.setCentralWidget(self.tabs)

        self.inputedButton1 = ""
        self.inputedButton2 = ""
        self.angka1Inputed = False
        self.angka2Inputed = False
        self.angka1 = 0
        self.angka2 = 0
        self.operasi = "+"


    def buttonPenjumlahanClicked(self):
        self.button_pengurangan.setChecked(False)
        self.button_perkalian.setChecked(False)
        self.button_pembagian.setChecked(False)
        self.operasi = "+"
        self.labelOp.setText(self.operasi)
        self.labelOpVH.setText(self.operasi)

    def buttonPenguranganClicked(self):
        self.button_penjumlahan.setChecked(False)
        self.button_perkalian.setChecked(False)
        self.button_pembagian.setChecked(False)
        self.operasi = "-"
        self.labelOp.setText(self.operasi)
        self.labelOpVH.setText(self.operasi)
    
    def buttonPerkalianClicked(self):
        self.button_penjumlahan.setChecked(False)
        self.button_pengurangan.setChecked(False)
        self.button_pembagian.setChecked(False)
        self.operasi = "x"
        self.labelOp.setText(self.operasi)
        self.labelOpVH.setText(self.operasi)

    def buttonPembagianClicked(self):
        self.button_penjumlahan.setChecked(False)
        self.button_pengurangan.setChecked(False)
        self.button_perkalian.setChecked(False)
        self.operasi = ":"
        self.labelOp.setText(self.operasi)
        self.labelOpVH.setText(self.operasi)
    
    def buttonClick0(self):
        if(not(self.angka1Inputed)):
            self.inputedButton1 += "0"
            self.dispAngka1.setText(str(int(self.inputedButton1)))
            self.dispAngka1VH.setText(str(int(self.inputedButton1)))
        elif(not(self.angka2Inputed)):
            self.inputedButton2 += "0"
            self.dispAngka2.setText(str(int(self.inputedButton2)))
            self.dispAngka2VH.setText(str(int(self.inputedButton2)))

    def buttonClick3(self):
        if(not(self.angka1Inputed)):
            self.inputedButton1 += "3"
            self.dispAngka1.setText(str(int(self.inputedButton1)))
            self.dispAngka1VH.setText(str(int(self.inputedButton1)))
        elif(not(self.angka2Inputed)):
            self.inputedButton2 += "3"
            self.dispAngka2.setText(str(int(self.inputedButton2)))
            self.dispAngka2VH.setText(str(int(self.inputedButton2)))

    def buttonClick4(self):
        if(not(self.angka1Inputed)):
            self.inputedButton1 += "4"
            self.dispAngka1.setText(str(int(self.inputedButton1)))
            self.dispAngka1VH.setText(str(int(self.inputedButton1)))
        elif(not(self.angka2Inputed)):
            self.inputedButton2 += "4"
            self.dispAngka2.setText(str(int(self.inputedButton2)))
            self.dispAngka2VH.setText(str(int(self.inputedButton2)))

    def buttonClick5(self):
        if(not(self.angka1Inputed)):
            self.inputedButton1 += "5"
            self.dispAngka1.setText(str(int(self.inputedButton1)))
            self.dispAngka1VH.setText(str(int(self.inputedButton1)))
        elif(not(self.angka2Inputed)):
            self.inputedButton2 += "5"
            self.dispAngka2.setText(str(int(self.inputedButton2)))
            self.dispAngka2VH.setText(str(int(self.inputedButton2)))

    def buttonClick6(self):
        if(not(self.angka1Inputed)):
            self.inputedButton1 += "6"
            self.dispAngka1.setText(str(int(self.inputedButton1)))
            self.dispAngka1VH.setText(str(int(self.inputedButton1)))
        elif(not(self.angka2Inputed)):
            self.inputedButton2 += "6"
            self.dispAngka2.setText(str(int(self.inputedButton2)))
            self.dispAngka2VH.setText(str(int(self.inputedButton2)))

    def buttonClick7(self):
        if(not(self.angka1Inputed)):
            self.inputedButton1 += "7"
            self.dispAngka1.setText(str(int(self.inputedButton1)))
            self.dispAngka1VH.setText(str(int(self.inputedButton1)))
        elif(not(self.angka2Inputed)):
            self.inputedButton2 += "7"
            self.dispAngka2.setText(str(int(self.inputedButton2)))
            self.dispAngka2VH.setText(str(int(self.inputedButton2)))

    def endLine(self):
        if(not(self.angka1Inputed)):
            if(self.inputedButton1 == ""): 
                self.inputedButton1 = "0"
            self.angka1 = int(self.inputedButton1)
            self.angka1Inputed = True
            self.fontDispAngka1.setBold(False)
            self.dispAngka1.setFont(self.fontDispAngka1)
            self.fontDispAngka2.setBold(True)
            self.dispAngka2.setFont(self.fontDispAngka2)
            self.fontDispAngka1VH.setBold(False)
            self.dispAngka1VH.setFont(self.fontDispAngka1VH)
            self.fontDispAngka2VH.setBold(True)
            self.dispAngka2VH.setFont(self.fontDispAngka2VH)
            self.buttonNext.setText("=")
            self.buttonNextVH.setText("=")
        elif(not(self.angka2Inputed)):
            if(self.inputedButton2 == ""): 
                self.inputedButton2 = "0"
            self.angka2 = int(self.inputedButton2)
            self.angka2Inputed = True
            self.fontDispAngka2.setBold(False)
            self.dispAngka2.setFont(self.fontDispAngka1)
            self.fontDispHasil.setBold(True)
            self.dispHasil.setFont(self.fontDispHasil)
            self.fontDispAngka2VH.setBold(False)
            self.dispAngka2VH.setFont(self.fontDispAngka1VH)
            self.fontDispHasilVH.setBold(True)
            self.dispHasilVH.setFont(self.fontDispHasilVH)
            self.buttonNext.setText("clear")
            self.buttonNextVH.setText("clear")
        elif(self.angka1Inputed and self.angka2Inputed): 
            self.inputedButton1 = ""
            self.inputedButton2 = ""
            self.angka1Inputed = False
            self.angka2Inputed = False
            self.angka1 = 0
            self.angka2 = 0
            self.dispAngka1.setText("0")
            self.dispAngka2.setText("0")
            self.dispHasil.setText("0")
            self.fontDispHasil.setBold(False)
            self.dispHasil.setFont(self.fontDispHasil)
            self.fontDispAngka1.setBold(True)
            self.dispAngka1.setFont(self.fontDispAngka1)
            self.dispAngka1VH.setText("0")
            self.dispAngka2VH.setText("0")
            self.dispHasilVH.setText("0")
            self.fontDispHasilVH.setBold(False)
            self.dispHasilVH.setFont(self.fontDispHasilVH)
            self.fontDispAngka1VH.setBold(True)
            self.dispAngka1VH.setFont(self.fontDispAngka1VH)
            self.buttonNext.setText("next")
            self.buttonNextVH.setText("next")

    def calculate(self):
        result = 0
        if(self.operasi == "+"):
            result = self.angka1 + self.angka2
        elif(self.operasi == "-"):
            result = self.angka1 - self.angka2
        elif(self.operasi == "x"):
            result = self.angka1 * self.angka2
        elif(self.operasi == ":"):
            if(self.angka1 == 0 or self.angka2 == 0):
                result = "undefined"
            else:
                result = self.angka1 / self.angka2
        self.dispHasil.setText(str(result))
        self.dispHasilVH.setText(str(result))

    def clear(self):
        self.inputedButton1 = ""
        self.inputedButton2 = ""
        self.angka1Inputed = False
        self.angka2Inputed = False
        self.hasilInputed = False
        self.angka1 = 0
        self.angka2 = 0
        self.dispAngka1.setText("0")
        self.dispAngka2.setText("0")
        self.dispHasil.setText("0")
        self.dispAngka1VH.setText("0")
        self.dispAngka2VH.setText("0")
        self.dispHasilVH.setText("0")
        self.fontDispAngka1.setBold(True)
        self.dispAngka1.setFont(self.fontDispAngka1)
        self.fontDispHasil.setBold(False)
        self.dispHasil.setFont(self.fontDispHasil)
        self.fontDispAngka2.setBold(False)
        self.dispAngka2.setFont(self.fontDispAngka2)
        self.fontDispAngka1VH.setBold(True)
        self.dispAngka1VH.setFont(self.fontDispAngka1)
        self.fontDispHasilVH.setBold(False)
        self.dispHasilVH.setFont(self.fontDispHasil)
        self.fontDispAngka2VH.setBold(False)
        self.dispAngka2VH.setFont(self.fontDispAngka2)
    








app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()