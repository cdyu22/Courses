import sys
import random
from random import randint
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

CELL_COUNT = 4
CELL_SIZE = 60
CELL_SIZE_HALF = CELL_SIZE/2
GRID_ORIGINX = 130
GRID_ORIGINY = 100
UNDER_BOX = GRID_ORIGINY + (CELL_COUNT * CELL_SIZE)+15
W_WIDTH = 500
W_HEIGHT = 500
CONGRATULATIONSX = GRID_ORIGINX + 25
CONGRATULATIONSY = GRID_ORIGINY - 10

class Fifteen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Fifteen')
        self.setGeometry(300, 300, W_WIDTH,W_HEIGHT)
        self.__winner = False
        self.__hint1 = False
        self.__board = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        inversions = 0
        self.__moves = 0
        #Make List
        for i in range(15):
            x = randint(0,14)
            while self.__board[x] != -1:
                x = randint(0,14)
            self.__board[x] = i+1
        for i in range(15):
            for r in range(14-i):
                if self.__board[i] > self.__board[r+i+1]:
                    inversions += 1
        if inversions % 2 == 0:
            q = randint(1,2)
            if q == 1:
                w = randint(4,7)
            if q == 2:
                w = randint(12,15)
        if inversions % 2 == 1:
            q = randint(1,2)
            if q == 1:
                w = randint(0,3)
            if q == 2:
                w = randint(8,11)
        self.__board.insert(w,-1)
        self.__col0 = [self.__board[0],self.__board[4],self.__board[8],self.__board[12]]
        self.__col1 = [self.__board[1],self.__board[5],self.__board[9],self.__board[13]]
        self.__col2 = [self.__board[2],self.__board[6],self.__board[10],self.__board[14]]
        self.__col3 = [self.__board[3],self.__board[7],self.__board[11],self.__board[15]]
        self.__row0 = [self.__col0[0],self.__col1[0],self.__col2[0],self.__col3[0]]
        self.__row1 = [self.__col0[1],self.__col1[1],self.__col2[1],self.__col3[1]]
        self.__row2 = [self.__col0[2],self.__col1[2],self.__col2[2],self.__col3[2]]
        self.__row3 = [self.__col0[3],self.__col1[3],self.__col2[3],self.__col3[3]]
        self.__board = [self.__row0,self.__row1,self.__row2,self.__row3]
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for row in range(CELL_COUNT):
            for col in range(CELL_COUNT):
                self.winner_check()
                qp.setPen(QPen(Qt.black,0))
                qp.drawRect(GRID_ORIGINX,400,240,30)
                qp.drawText(220,420,'NEW GAME')
                qp.drawRect(GRID_ORIGINX,360,240,30)
                qp.drawText(238,380,'HINT')
                qp.drawText(GRID_ORIGINX,UNDER_BOX,'Moves: ' + str(self.__moves))
                if self.__hint1 == True:
                    qp.drawText(90,443, str(self.__hint))
                if self.__winner == True:
                    qp.setPen(QPen(Qt.red, 3))
                    qp.drawText(CONGRATULATIONSX,CONGRATULATIONSY,'CONGRATULATIONS, YOU WON!')
                qp.drawRect(GRID_ORIGINX + CELL_SIZE * col,GRID_ORIGINY + CELL_SIZE * row, CELL_SIZE, CELL_SIZE)
                if self.__board[row][col] == -1:
                    self.__r1 = row
                    self.__c1 = col
                else:
                    qp.drawText(GRID_ORIGINX + (CELL_SIZE * col) + CELL_SIZE_HALF,GRID_ORIGINY + (CELL_SIZE * row) + CELL_SIZE_HALF,str(self.__board[row][col]))
        qp.end()

    def mousePressEvent(self, event):
        self.__x = event.x()
        self.__y = event.y()
        if (130 <= self.__x <= 370) and (400 <= self.__y <= 430):
            self.restart()
        if self.__winner == True:
            return
        if (130 <= self.__x <= 370) and (360 <= self.__y <= 390):
            self.__hint1 = True
            self.hint()
        row = (self.__y - GRID_ORIGINY) // CELL_SIZE
        col = (self.__x - GRID_ORIGINX) // CELL_SIZE
        if 0 <= row <= 3 and 0 <= col <= 3:
            if self.__board[row][col] == -1:
                pass
            elif -1 in self.__board[row]:#c1 is the position within the row
                if row == 0:
                    self.__row0.remove(-1)
                    self.__row0.insert(col,-1)
                    self.update1()
                if row == 1:
                    self.__row1.remove(-1)
                    self.__row1.insert(col,-1)
                    self.update1()
                if row == 2:
                    self.__row2.remove(-1)
                    self.__row2.insert(col,-1)
                    self.update1()
                if row == 3:
                    self.__row3.remove(-1)
                    self.__row3.insert(col,-1)
                    self.update1()
                self.__hint1 = False
                self.__moves += 1
            elif self.__c1 == col:
                if col == 0:
                    self.__col0.remove(-1)
                    self.__col0.insert(row,-1)
                    self.update2()
                if col == 1:
                    self.__col1.remove(-1)
                    self.__col1.insert(row,-1)
                    self.update2()
                if col == 2:
                    self.__col2.remove(-1)
                    self.__col2.insert(row,-1)
                    self.update2()
                if col == 3:
                    self.__col3.remove(-1)
                    self.__col3.insert(row,-1)
                    self.update2()
                self.__hint1 = False
                self.__moves += 1
        self.update()


    def winner_check(self):
        if self.__board == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,-1]]:
            self.__winner = True

    def hint(self):
        if self.__row0 == [1,2,3,4] and self.__row1 == [5,6,7,8] and self.__board[2][0] == 9 and self.__board[3][0] == 13 and self.__board[2][1] == 10 and self.__board[3][1] == 14:
            self.__hint = '        Move 11, 12 and 15 to their sequential position.'
        elif self.__row0 == [1,2,3,4] and self.__row1 == [5,6,7,8] and self.__board[2][0] == 9 and self.__board[3][0] == 13:
            self.__hint = 'Work in doubles. Place 10 and 14 in their sequential position.'
        elif self.__row0 == [1,2,3,4] and self.__row1 == [5,6,7,8]:
            self.__hint = 'Work in doubles. Place 9 and 13 in their sequential position.'
        elif self.__row0 == [1,2,3,4] and self.__board[1][0] == 5 and self.__board[1][1] == 6:
            self.__hint = 'Work in doubles. Place 7 and 8 in their sequential position.'
        elif self.__row0 == [1,2,3,4]:
            self.__hint = 'Work in doubles. Place 5 and 6 in their sequential position.'
        elif self.__board[0][0] == 1 and self.__board[0][1] == 2:
            self.__hint = 'Work in doubles. Place 3 and 4 in their sequential position.'
        elif self.__board[0][0] != 1 or self.__board[0][1] != 2:
            self.__hint = 'Work in doubles. Place 1 and 2 in their sequential position.'

    def update1(self):
        self.__col0 = [self.__row0[0],self.__row1[0],self.__row2[0],self.__row3[0]]
        self.__col1 = [self.__row0[1],self.__row1[1],self.__row2[1],self.__row3[1]]
        self.__col2 = [self.__row0[2],self.__row1[2],self.__row2[2],self.__row3[2]]
        self.__col3 = [self.__row0[3],self.__row1[3],self.__row2[3],self.__row3[3]]
        self.__row0 = [self.__col0[0],self.__col1[0],self.__col2[0],self.__col3[0]]
        self.__row1 = [self.__col0[1],self.__col1[1],self.__col2[1],self.__col3[1]]
        self.__row2 = [self.__col0[2],self.__col1[2],self.__col2[2],self.__col3[2]]
        self.__row3 = [self.__col0[3],self.__col1[3],self.__col2[3],self.__col3[3]]
        self.__board = [self.__row0,self.__row1,self.__row2,self.__row3]

    def update2(self):
        self.__row0 = [self.__col0[0],self.__col1[0],self.__col2[0],self.__col3[0]]
        self.__row1 = [self.__col0[1],self.__col1[1],self.__col2[1],self.__col3[1]]
        self.__row2 = [self.__col0[2],self.__col1[2],self.__col2[2],self.__col3[2]]
        self.__row3 = [self.__col0[3],self.__col1[3],self.__col2[3],self.__col3[3]]
        self.__board = [self.__row0,self.__row1,self.__row2,self.__row3]

    def restart(self):
        self.__winner = False
        self.__board = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        inversions = 0
        self.__moves = 0
        for i in range(15):
            x = randint(0,14)
            while self.__board[x] != -1:
                x = randint(0,14)
            self.__board[x] = i+1
        #Count inversions
        for i in range(15):
            for r in range(14-i):
                if self.__board[i] > self.__board[r+i+1]:
                    inversions += 1
        if inversions % 2 == 0:
            q = randint(1,2)
            if q == 1:
                w = randint(4,7)
            if q == 2:
                w = randint(12,15)
        if inversions % 2 == 1:
            q = randint(1,2)
            if q == 1:
                w = randint(0,3)
            if q == 2:
                w = randint(8,11)
        self.__board.insert(w,-1)
        self.__col0 = [self.__board[0],self.__board[4],self.__board[8],self.__board[12]]
        self.__col1 = [self.__board[1],self.__board[5],self.__board[9],self.__board[13]]
        self.__col2 = [self.__board[2],self.__board[6],self.__board[10],self.__board[14]]
        self.__col3 = [self.__board[3],self.__board[7],self.__board[11],self.__board[15]]
        self.__row0 = [self.__col0[0],self.__col1[0],self.__col2[0],self.__col3[0]]
        self.__row1 = [self.__col0[1],self.__col1[1],self.__col2[1],self.__col3[1]]
        self.__row2 = [self.__col0[2],self.__col1[2],self.__col2[2],self.__col3[2]]
        self.__row3 = [self.__col0[3],self.__col1[3],self.__col2[3],self.__col3[3]]
        self.__board = [self.__row0,self.__row1,self.__row2,self.__row3]
        self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Fifteen()
  sys.exit(app.exec_())
