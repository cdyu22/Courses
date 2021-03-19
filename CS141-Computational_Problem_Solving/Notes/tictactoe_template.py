import sys
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

# if you change CELL_COUNT, be sure that initial
# patterns in constructor are still valid
CELL_COUNT = 3
CELL_SIZE = 50
GRID_ORIGINX = 175
GRID_ORIGINY = 175
W_WIDTH = 500
W_HEIGHT = 500

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TicTacToe')
        self.setGeometry(300, 300, W_WIDTH,W_HEIGHT)
        self.__turn = 0
        self.__winner = False
        self.__full = False
        self.__board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                qp.drawRect(GRID_ORIGINX + CELL_SIZE * col,GRID_ORIGINY + CELL_SIZE * row, CELL_SIZE, CELL_SIZE)
                if self.winner_check(row,col) == True:
                    qp.setPen(QPen(Qt.red, 3))
                if self.__board[row][col] == 0:
                    #PlayerX
                    qp.drawLine(GRID_ORIGINX + CELL_SIZE * col, GRID_ORIGINY + CELL_SIZE * row,
                                GRID_ORIGINX + CELL_SIZE * (col + 1), GRID_ORIGINY + CELL_SIZE * (row + 1))
                    qp.drawLine(GRID_ORIGINX + CELL_SIZE * (col + 1), GRID_ORIGINY + CELL_SIZE * row,
                                GRID_ORIGINX + CELL_SIZE * col, GRID_ORIGINY + CELL_SIZE * (row + 1))
                elif self.__board[row][col] == 1:
                    #PlayerO
                    qp.drawEllipse(GRID_ORIGINX + CELL_SIZE * col,GRID_ORIGINY + CELL_SIZE * row,
                                    CELL_SIZE,CELL_SIZE)
                qp.setPen(QPen(Qt.black,0))
        qp.end()

    def winner_check(self, r, c):
        for i in range(3):
            if self.__board[i][0] == self.__board[i][1] == self.__board[1][2] != -1:
                self.__winner = True
                return r == i
        for j in range(3):
            if self.__board[0][j] == self.__board[1][j] == self.__board[2][j] != -1:
                self.__winner = True
                return c == j
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] != -1:
            self.__winner = True
            return (r == 0 and c == 0) or (r==1 and c == 1) or (r == 2 and c == 2)
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0] != -1:
            self.__winner = True
            return (r == 0 and c == 2) or (r==1 and c == 1) or (r == 2 and c == 0)

    def full_check(self):#-1 is the initial value to represent an empty square
        if self.__board[0][0] != -1 and self.__board[0][1] != -1 and self.__board[0][2]\
        and self.__board[1][0] != -1 and self.__board[1][1] != -1 and self.__board[1][2]\
        and self.__board[2][0] != -1 and self.__board[2][1] != -1 and self.__board[2][2]:
            self.__full = True


    def mousePressEvent(self, event):
        if self.__full == True or self.__winner == True:
            return
        self.__x = event.x()
        self.__y = event.y()
        row = (self.__y - GRID_ORIGINY) // CELL_SIZE
        col = (self.__x - GRID_ORIGINX) // CELL_SIZE
        print(row,col)
        if 0 <= row <= 2 and 0 <= col <= 2:
            if self.__board[row][col] == -1:
                self.__board[row][col] = self.__turn
                self.__turn = (self.__turn + 1) % 2#implicitly ignores whatever doesn't fall within the range.
                self.full_check()
        self.update()




if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TicTacToe()
  sys.exit(app.exec_())
