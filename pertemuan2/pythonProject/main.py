from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class DemoWind(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Demo window')
        self.button = QPushButton('Close', self)
        self.button.setCheckable(True)
        self.button.setGeometry(10, 10, 70, 40)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_toggled)

    def button_clicked(self):
        print("Button clicked")
        self.setWindowTitle("My Button App")

    def button_toggled(self, checked):
        print("Checked?", checked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWind() # Create a QWidget, which will be our window.
    window.show() # IMPORTANT!!!!! Windows are hidden by default.
    app.exec() # Start the event loop.
