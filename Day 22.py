import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("PyQt Application")
        self.setGeometry(100, 100, 300, 200)
        self._createWidgets()

    def _createWidgets(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Hello, World!")
        layout.addWidget(label)

        button = QPushButton("Click me!")
        button.clicked.connect(self._onButtonClick)
        layout.addWidget(button)

    def _onButtonClick(self):
        print("Button clicked!")

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
