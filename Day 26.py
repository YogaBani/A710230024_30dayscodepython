import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import Qt

class PuzzleGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("2x2 Sliding Puzzle Game")
        self.setGeometry(300, 300, 200, 200)

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)

        self.tiles = [i for i in range(1, 5)]
        self.emptyTileIndex = 3

        for i in range(4):
            button = QPushButton(str(self.tiles[i]))
            button.clicked.connect(self.moveTile)
            self.gridLayout.addWidget(button, i // 2, i % 2)

        self.show()

    def moveTile(self):
        button = self.sender()
        tileIndex = self.tiles.index(int(button.text()))

        if abs(tileIndex - self.emptyTileIndex) in [1, 2]:
            self.tiles[tileIndex], self.tiles[self.emptyTileIndex] = self.tiles[self.emptyTileIndex], self.tiles[tileIndex]
            self.emptyTileIndex = tileIndex

            for i in range(4):
                button = self.gridLayout.itemAt(i).widget()
                button.setText(str(self.tiles[i]))

            if self.tiles == [i for i in range(1, 5)]:
                self.gameWon()

    def gameWon(self):
        print("Congratulations! You won the game!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = PuzzleGame()
    sys.exit(app.exec_())
