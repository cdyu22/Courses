import sys
import random
from random import randint
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

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
        self.__tracker = 1
        self.__multiplier = 1
        self.__counter = 0
        self.__length = 0
        self.__hardmode = False
        #Lists
        self.__hlist = []
        self.__vlist = []
        self.__drow1list = []
        self.__dcol1list = []
        self.__drow2list = []
        self.__dcol2list = []
        #Power-ups
        self.__pup_cancel = 5
        self.__cancel = False
        self.__pup_multi = 3
        self.__multi = False
        self.__pup_s2c = 3
        self.__s2c = False
        self.__pup_bomb = 1
        self.__bomb = False
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
                self.full_check()
                qp.setPen(QColor(0,0,0))
                if self.__full == True:
                    qp.drawText(215,30,'Game Over!')
                #Easy Mode
                if self.__hardmode == True:
                    qp.setBrush(QColor(255,255,255))
                if self.__hardmode == False:
                    qp.setBrush(QColor(169,169,169))
                qp.drawRect(435,35,60,178)
                qp.drawText(444,123,'Normal')
                qp.drawText(450,137,'Mode')
                #Hard Mode
                if self.__hardmode == True:
                    qp.setBrush(QColor(169,169,169))
                if self.__hardmode == False:
                    qp.setBrush(QColor(255,255,255))
                qp.drawRect(435,217,60,178)
                qp.drawText(451,305,'Hard')
                qp.drawText(450,319,'Mode')
                #Draw Board
                qp.setBrush(QColor(255,255,255))
                qp.drawRect(GRID_ORIGINX + CELL_SIZE * col,GRID_ORIGINY + CELL_SIZE * row, CELL_SIZE, CELL_SIZE)
                qp.drawText(70,410,'Score: ' + str(self.__score))
                qp.drawText(150,410,'x ' + str(self.__tracker))
                if self.__board[row][col] == 1:
                    qp.setPen(QColor(178,255,102))
                    qp.setBrush(QColor(178,255,102))
                    qp.drawEllipse(SHAPE_XC + CELL_SIZE * col,SHAPE_YC + CELL_SIZE * row,39,39)
                elif self.__board[row][col] == 2:
                    qp.setBrush(QColor(255,102,102))
                    qp.setPen(QColor(255,102,102))
                    qp.drawRect(SHAPE_XR + CELL_SIZE * col,SHAPE_YR + CELL_SIZE * row,35,35)
                qp.setPen(QPen(Qt.black,0))
                qp.setBrush(QColor(255,255,255))
                #Reset Button
                qp.drawRect(70,415,360,30)
                qp.drawText(230,435,'Restart')
                #No Blocks Next Turn
                qp.drawRect(70,450,88,45)
                qp.drawText(88,462,'No Blocks')
                qp.drawText(87,477,'Next Turn')
                #+1 to Multiplier
                qp.drawRect(161,450,88,45)
                qp.drawText(170,472,'+1 Multiplier')
                #Make Block A Placer
                qp.drawRect(251,450,88,45)
                qp.drawText(275,462,'Square')
                qp.drawText(272,477,'to Circle')
                #Bomb Button
                qp.drawRect(342,450,88,45)
                qp.drawText(368,475,'Bomb')
                #Record
                qp.setPen(QColor(255,102,102))
                qp.drawText(108,490,'(' + str(self.__pup_cancel) + ')')
                qp.drawText(198,490,'(' + str(self.__pup_multi) + ')')
                qp.drawText(289,490,'(' +str(self.__pup_s2c) + ')')
                qp.drawText(377,490,'(' + str(self.__pup_bomb) + ')')
                #Signal
                qp.setPen(QColor(255,102,102))
                if self.__cancel == True and self.__multi == False:
                    qp.drawText(165,30,'No Blocks Next Turn Activated!')
                if self.__multi == True and self.__cancel == False:
                    qp.drawText(178,30,'+1 to Multiplier Activated!')
                if self.__multi == True and self.__cancel == True:
                    qp.drawText(107,30,'No Blocks Next Turn and +1 to Multiplier Activated!')
                if self.__s2c == True:
                    qp.drawText(172,30,'Square to Circle Activated!')
                if self.__bomb == True:
                    qp.drawText(198,30,'Bomb is Activated!')
        qp.end()

    def full_check(self):
        for r in range(8):
            for c in range(8):
                if self.__board[r][c] == -1:
                    return
        self.__full = True

    def mousePressEvent(self, event):
        self.__x = event.x()
        self.__y = event.y()
        #Normal Mode
        if self.__hardmode == True and (435 <= self.__x <= 495) and (35 <= self.__y <= 213):
            self.__hardmode = False
            self.restart()
            self.update()
        #Hard Mode
        if self.__hardmode == False and (435 <= self.__x <= 495) and (217 <= self.__y <= 395):
            self.__hardmode = True
            self.restarthard()
            self.update()
        if self.__hardmode == True and (70 <= self.__x <= 430) and (415 <= self.__y <= 445):
            self.restarthard()
            self.update()
            return
        if self.__hardmode == False and (70 <= self.__x <= 430) and (415 <= self.__y <= 445):
            self.restart()
            self.update()
            return
        if self.__full == True:
            return
        #Power-ups
        #No Blocks Next Turn: Click again to cancel
        if self.__cancel == False and (70 <= self.__x <= 158) and (450 <= self.__y <= 495):
            if self.__pup_cancel > 0:
                self.__cancel = True
                self.__pup_cancel -= 1
            else:
                pass
        elif self.__cancel == True and (70 <= self.__x <= 158) and (450 <= self.__y <= 495):
            self.__cancel = False
            self.__pup_cancel += 1
        #+1 to multiplier
        if self.__multi == False and (161 <= self.__x <= 249) and (450 <= self.__y <= 495):
            if self.__pup_multi > 0:
                self.__multi = True
                self.__pup_multi -= 1
        elif self.__multi == True and (161 <= self.__x <= 249) and (450 <= self.__y <= 495):
            self.__multi = False
            self.__pup_multi += 1
        #Make Block a Placer
        if self.__bomb ==False and self.__s2c == False and self.__multi == False and self.__cancel == False and (251 <= self.__x <= 339) and (450 <= self.__y <= 495):
            if self.__pup_s2c > 0:
                self.__s2c = True
                self.__pup_s2c -= 1
        elif self.__s2c == True and (251 <= self.__x <= 339) and (450 <= self.__y <= 495):
            self.__s2c = False
            self.__pup_s2c += 1
        #Bomb
        if self.__bomb ==False and self.__s2c == False and self.__multi == False and self.__cancel == False and (342 <= self.__x <= 430) and (450 <= self.__y <= 495):
            if self.__pup_bomb > 0:
                self.__bomb = True
                self.__pup_bomb -= 1
        elif self.__bomb == True and (342 <= self.__x <= 430) and (450 <= self.__y <= 495):
            self.__bomb = False
            self.__pup_bomb += 1
        #Restart
        if (70 <= self.__x <= 430) and (415 <= self.__y <= 445):
            self.restart()
            self.update()
            return
        row = (self.__y - GRID_ORIGINY) // CELL_SIZE
        col = (self.__x - GRID_ORIGINX) // CELL_SIZE
        if 0 <= row <= 7 and 0 <= col <= 7:
            if self.__board[row][col] == 2 and self.__s2c == True:
                self.__board[row][col] = 1
                self.__s2c = False
            if self.__board[row][col] != 2 and self.__s2c == True:
                self.__s2c = False
                self.__pup_s2c += 1
            #Normal Stuff
            if self.__board[row][col] == -1:
                if self.__hardmode == False:
                    self.__board[row][col] = 1
                    x = randint(0,7)
                    y = randint(0,7)
                    while self.__board[x][y] == 2:
                        x = randint(0,7)
                        y = randint(0,7)
                    if self.__cancel == False and self.__bomb == False:
                        self.__board[x][y] = 2
                if self.__hardmode == True:
                    self.__board[row][col] = 1
                    x = randint(0,7)
                    y = randint(0,7)
                    z = randint(1,10)
                    if 1 <= z <= 7:
                        while self.__board[x][y] == 2:
                            x = randint(0,7)
                            y = randint(0,7)
                    if 8 <= z <= 10:
                        while self.__board[x][y] != 1:
                            x = randint(0,7)
                            y = randint(0,7)
                    if self.__cancel == False and self.__bomb == False:
                        self.__board[x][y] = 2

            #BOMB
            if self.__bomb == True:
                self.__board[row][col] = -1
                if 0 <= (row-1) <= 7 and 0 <= (col-1) <= 7:
                    self.__board[row-1][col-1] = -1
                if 0 <= (row-1) <= 7 and 0 <= (col) <= 7:
                    self.__board[row-1][col] = -1
                if 0 <= (row-1) <= 7 and 0 <= (col+1) <= 7:
                    self.__board[row-1][col+1] = -1
                if 0 <= (row) <= 7 and 0 <= (col-1) <= 7:
                    self.__board[row][col-1] = -1
                if 0 <= (row) <= 7 and 0 <= (col+1) <= 7:
                    self.__board[row][col+1] = -1
                if 0 <= (row+1) <= 7 and 0 <= (col-1) <= 7:
                    self.__board[row+1][col-1] = -1
                if 0 <= (row+1) <= 7 and 0 <= (col) <= 7:
                    self.__board[row+1][col] = -1
                if 0 <= (row+1) <= 7 and 0 <= (col+1) <= 7:
                    self.__board[row+1][col+1] = -1
            #END BOMB
            self.__bomb = False
            self.__cancel = False
            self.hcheck(row,col)
            self.vcheck(row,col)
            self.dlrcheck(row,col)
            self.drlcheck(row,col)
            self.clear(row,col)
            self.multiplier()
            self.__score += self.__counter
            self.__counter = 0
            self.__multiplier = 1
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
            if b == 7 and tick > 3:
                b = 8
        if tick > 3:
            self.__counter += tick
            while tick > 0:
                self.__hlist.append(b-tick)
                tick -= 1

    def vcheck(self,row,col):
        tock = 0
        for a in range(8):
            if self.__board[a][col] == 1:
                tock += 1
            if self.__board[a][col] != 1:
                if tock > 3:
                    break
                else:
                    tock = 0
            if a == 7 and tock > 3:
                a = 8
        if tock > 3:
            self.__counter += tock
            while tock > 0:
                self.__vlist.append(a-tock)
                tock -= 1

    def dlrcheck(self,row,col):
        tack = 0
        a = row
        b = col
        while self.__board[a][b] == 1:
            self.__drow1list.append(a)
            self.__dcol1list.append(b)
            a += 1
            b += 1
            tack += 1
            if (a < 0) or (a > 7) or (b < 0) or (b > 7):
                break
        a = row - 1
        b = col - 1
        while self.__board[a][b] == 1:
            self.__drow1list.append(a)
            self.__dcol1list.append(b)
            a -= 1
            b -= 1
            tack += 1
            if (a < 0) or (a > 7) or (b < 0) or (b > 7):
                break
        if tack > 3:
            self.__counter += tack
            tack = 0
        else:
            self.__drow1list.clear()
            self.__dcol1list.clear()

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

    def clear(self,row,col):
        if len(self.__hlist) != 0:
            for c in self.__hlist:
                self.__board[row][c] = -1
            self.__length += len(self.__hlist)
            self.__hlist.clear()
            self.__multiplier += 1
        if len(self.__vlist) != 0:
            for r in self.__vlist:
                self.__board[r][col] = -1
            self.__length += len(self.__vlist)
            self.__vlist.clear()
            self.__multiplier += 1
        if len(self.__drow1list) > 3:
            for r,c in zip(self.__drow1list,self.__dcol1list):
                self.__board[r][c] = -1
            self.__length += len(self.__drow1list)
            self.__drow1list.clear()
            self.__dcol1list.clear()
            self.__multiplier += 1
        if len(self.__drow2list) > 3:
            for r,c in zip(self.__drow2list,self.__dcol2list):
                self.__board[r][c] = -1
            self.__length += len(self.__drow2list)
            self.__drow2list.clear()
            self.__dcol2list.clear()
            self.__multiplier += 1
        if self.__length >= 10 and self.__hardmode == False:
            self.randompup()

    def multiplier(self):
        if self.__multiplier > 1:
            self.__multiplier -= 1
            self.__counter = self.__counter - self.__multiplier + 1
        if self.__multi == True and self.__length > 3:
            self.__multiplier += 1
            self.__multi = False
        self.__counter = self.__counter * self.__multiplier
        self.__tracker = self.__multiplier
        self.__multiplier = 1
        self.__length = 0

    def restart(self):
        self.__score = 0
        self.__tracker = 1
        self.__multiplier = 1
        self.__length = 0
        self.__hlist = []
        self.__vlist = []
        self.__drow1list = []
        self.__dcol1list = []
        self.__drow2list = []
        self.__dcol2list = []
        self.__pup_cancel = 5
        self.__cancel = False
        self.__pup_multi = 3
        self.__multi = False
        self.__pup_s2c = 3
        self.__s2c = False
        self.__pup_bomb = 1
        self.__bomb = False
        self.__counter = 0
        self.__full = False
        self.__hardmode = False
        self.__board = [[-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1]]

    def restarthard(self):
        self.__score = 0
        self.__hardmode = True
        self.__tracker = 1
        self.__multiplier = 1
        self.__length = 0
        self.__hlist = []
        self.__vlist = []
        self.__drow1list = []
        self.__dcol1list = []
        self.__drow2list = []
        self.__dcol2list = []
        self.__pup_cancel = 3
        self.__cancel = False
        self.__pup_multi = 1
        self.__multi = False
        self.__pup_s2c = 1
        self.__s2c = False
        self.__pup_bomb = 1
        self.__bomb = False
        self.__counter = 0
        self.__full = False
        self.__board = [[-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1]]

    def randompup(self):
        pup = randint(1,12)
        if 1 <= pup <= 5:
            self.__pup_cancel += 1
        if 6 <= pup <= 8:
            self.__pup_multi += 1
        if 9 <= pup <= 11:
            self.__pup_s2c += 1
        if pup == 12:
            self.__pup_bomb += 1

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = TribeBubbles()
  sys.exit(app.exec_())
