import sys
import random
from random import randint
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

#Has DLR checking method
CELL_COUNT = 8
CELL_SIZE = 45
GRID_ORIGINX = 70
GRID_ORIGINY = 35
W_WIDTH = 500
W_HEIGHT = 500
SHAPE_XC = GRID_ORIGINX + 3
SHAPE_YC = GRID_ORIGINY + 4
SHAPE_XR = GRID_ORIGINX + 5
SHAPE_YR = GRID_ORIGINY + 6

class TribeBubbles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TribeBubbles')
        self.setGeometry(300, 300, W_WIDTH,W_HEIGHT)
        self.__score = 0
        self.__h = False
        self.__v = False
        self.__counter = 0
        self.__winner = False
        self.__full = False
        self.__board = [[-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1]]
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                qp.setBrush(QColor(255,255,255))
                qp.drawRect(GRID_ORIGINX + CELL_SIZE * col,GRID_ORIGINY + CELL_SIZE * row, CELL_SIZE, CELL_SIZE)
                qp.drawText(70,410,'Score: ' + str(self.__score))
                if self.winner_check(row,col) == True:
                    qp.setPen(QPen(Qt.red, 3))
                if self.__board[row][col] == 1:
                    qp.setPen(QColor(178,255,102))
                    qp.setBrush(QColor(178,255,102))
                    qp.drawEllipse(SHAPE_XC + CELL_SIZE * col,SHAPE_YC + CELL_SIZE * row,39,39)
                elif self.__board[row][col] == 2:
                    qp.setBrush(QColor(255,102,102))
                    qp.setPen(QColor(255,102,102))
                    qp.drawRect(SHAPE_XR + CELL_SIZE * col,SHAPE_YR + CELL_SIZE * row,35,35)
                qp.setPen(QPen(Qt.black,0))
        qp.end()

    def winner_check(self, r, c):
        pass

    def full_check(self):
        pass

    def mousePressEvent(self, event):
        if self.__full == True or self.__winner == True:
            return
        self.__x = event.x()
        self.__y = event.y()
        row = (self.__y - GRID_ORIGINY) // CELL_SIZE
        col = (self.__x - GRID_ORIGINX) // CELL_SIZE
        if 0 <= row <= 7 and 0 <= col <= 7:
            if self.__board[row][col] == -1:
                self.__board[row][col] = 1
                #PLACE HERE
        self.hcheck(row,col)
        self.vcheck(row,col)
        self.counter()
        self.__score +=  self.__counter
        self.__counter = 0
        self.update()


    def hcheck(self,row,col):
        tick = 0
        for b in range(8):
            if self.__board[row][b] == 1:
                tick += 1
            if self.__board[row][b] != 1:
                if tick > 3:
                    break
                else:
                    tick = 0
        if tick > 3:
            self.__counter += tick
            self.__h = True
            while tick > -1:
                self.__board[row][b-tick] = -1
                tick -= 1

    def vcheck(self,row,col):
        if self.__h == True:
            self.__board[row][col] = 1
        tock = 0
        for a in range(8):
            if self.__board[a][col] == 1:
                tock += 1
            if self.__board[a][col] != 1:
                if tock > 3:
                    if self.__h == True:
                        self.__counter -= 1
                    break
                else:
                    tock = 0
        if tock > 3:
            self.__counter += tock
            self.__v = True
            while tock > -1:
                    self.__board[a-tock][col] = -1
                    tock -= 1
        if self.__h == True:
            self.__board[row][col] = -1


    def counter(self):
        multiplier = 0
        if self.__h == True:
            multiplier += 1
        if self.__v == True:
            multiplier += 1
        self.__score = self.__score + (self.__counter*multiplier)
        self.__counter = 0
        self.__h = False
        self.__v = False


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TribeBubbles()
  sys.exit(app.exec_())
