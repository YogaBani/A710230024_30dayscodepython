import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(300, 300, 300, 300)

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(self.onButtonClick)
                self.gridLayout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        self.currentPlayer = "X"

    def onButtonClick(self):
        button = self.sender()
        if button.text() == "":
            button.setText(self.currentPlayer)
            if self.checkWin():
                self.showWinMessage()
            else:
                self.currentPlayer = "O" if self.currentPlayer == "X" else "X"

    def checkWin(self):
        for row in self.buttons:
            if row[0].text() == row[1].text() == row[2].text() != "":
                return True
        for col in range(3):
            if self.buttons[0][col].text() == self.buttons[1][col].text() == self.buttons[2][col].text() != "":
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True
        return False

    def showWinMessage(self):
        QMessageBox.information(self, "Game Over", f"Player {self.currentPlayer} wins!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
