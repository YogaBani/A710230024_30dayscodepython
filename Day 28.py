import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtCore import QTimer

class Snake(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Snake")
        self.setGeometry(300, 300, 400, 400)

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)

        self.buttons = []
        for i in range(20):
            row = []
            for j in range(20):
                button = QPushButton("")
                button.setFixedSize(20, 20)
                button.clicked.connect(self.onButtonClick)
                self.gridLayout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.food = self.generateFood()
        self.direction = (0, 1)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateGame)
        self.timer.start(100)

        self.updateUI()

    def onButtonClick(self):
        pass  # ignore button clicks

    def generateFood(self):
        while True:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            if (x, y) not in self.snake:
                return (x, y)

    def updateGame(self):
        head = self.snake[0]
        newHead = (head[0] + self.direction[0], head[1] + self.direction[1])

        if newHead in self.snake:
            self.gameOver()
        elif newHead[0] < 0 or newHead[0] >= 20 or newHead[1] < 0 or newHead[1] >= 20:
            self.gameOver()
        elif newHead == self.food:
            self.snake.insert(0, newHead)
            self.food = self.generateFood()
        else:
            self.snake.insert(0, newHead)
            self.snake.pop()

        self.updateUI()

    def gameOver(self):
        self.timer.stop()
        QMessageBox.information(self, "Game Over", "You lost! Press OK to restart.")
        self.snake = [(10, 10), (10, 11), (10, 12)]
        self.food = self.generateFood()
        self.direction = (0, 1)
        self.timer.start(100)
        self.updateUI()

    def updateUI(self):
        for i in range(20):
            for j in range(20):
                button = self.buttons[i][j]
                if (i, j) in self.snake:
                    button.setStyleSheet("background-color: green")
                elif (i, j) == self.food:
                    button.setStyleSheet("background-color: red")
                else:
                    button.setStyleSheet("background-color: white")

    def keyPressEvent(self, event):
        if event.key() == 16777234:  # left arrow
            self.direction = (-1, 0)
        elif event.key() == 16777236:  # right arrow
            self.direction = (1, 0)
        elif event.key() == 16777235:  # up arrow
            self.direction = (0, -1)
        elif event.key() == 16777237:  # down arrow
            self.direction = (0, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Snake()
    game.show()
    sys.exit(app.exec_())
