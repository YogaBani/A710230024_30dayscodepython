import sys
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarm")
        self.setGeometry(100, 100, 200, 100)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(50, 40)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

        self.alarm_time, ok = QInputDialog.getText(self, "Set Alarm", "Enter alarm time (HH:MM):")
        if ok:
            self.alarm_time = QTime.fromString(self.alarm_time, "hh:mm")
            self.show_time()

    def show_time(self):
        current_time = QTime.currentTime()
        self.label.setText(current_time.toString(Qt.DefaultLocaleLongDate))
        if current_time == self.alarm_time:
            self.alarm()

    def alarm(self):
        QMessageBox.information(self, "Alarm", "Wake up!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
