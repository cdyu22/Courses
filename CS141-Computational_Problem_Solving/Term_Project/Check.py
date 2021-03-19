import sys
import random
from random import randint
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

# if you change CELL_COUNT, be sure that initial
# patterns in constructor are still valid
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
        self.__counter = 0
        self.__drow2list = []
        self.__dcol2list = []
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
        self.drlcheck(row,col)
        self.counterclear(row,col)
        self.__score += self.__counter
        self.__counter = 0
        self.update()



    def drlcheck(self,row,col):
        tack = 0
        a = row
        b = col
        while self.__board[a][b] == 1:
            self.__drow2list.append(a)
            self.__dcol2list.append(b)
            a -= 1
            b += 1
            tack += 1
            if (a < 0) or (a > 7) or (b < 0) or (b > 7):
                break
        if row < 7:
            a = row + 1
        if col > 0:
            b = col - 1
        while self.__board[a][b] == 1:
            self.__drow2list.append(a)
            self.__dcol2list.append(b)
            a += 1
            b -= 1
            tack += 1
            if (a < 0) or (a > 7) or (b < 0) or (b > 7):
                break
        if tack > 3:
            self.__counter += tack
            tack = 0
        else:
            self.__drow2list.clear()
            self.__dcol2list.clear()

    def counterclear(self,row,col):
        if len(self.__drow2list) > 3:
            for r,c in zip(self.__drow2list,self.__dcol2list):
                self.__board[r][c] = -1
            self.__drow2list.clear()
            self.__dcol2list.clear()




if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TribeBubbles()
  sys.exit(app.exec_())
