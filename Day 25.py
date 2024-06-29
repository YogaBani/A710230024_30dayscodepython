import sys
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 200, 100)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(50, 40)

        self.seconds = 0
        self.running = False

        self.button = QPushButton("Start", self)
        self.button.move(50, 70)
        self.button.clicked.connect(self.start_stop)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.increment_time)

        self.show_time()

    def show_time(self):
        time_string = "{:02d}:{:02d}.{:02d}".format(self.seconds // 3600, (self.seconds // 60) % 60, self.seconds % 60)
        self.label.setText(time_string)

    def start_stop(self):
        if not self.running:
            self.running = True
            self.button.setText("Stop")
            self.timer.start(1000)
        else:
            self.running = False
            self.button.setText("Start")
            self.timer.stop()

    def increment_time(self):
        self.seconds += 1
        self.show_time()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
