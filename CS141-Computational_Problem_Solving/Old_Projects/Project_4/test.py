import sys
import random
from random import randint
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

from random import randint
board = [[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
for i in range(15):
    x = randint(0,3)
    y = randint(0,3)
    if board[x][y] == -1:
        board[x][y] = i
    else:
        while board[x][y] == -1:
            x = randint(0,3)
            y = randint(0,3)
        board[x][y] = i

print(board)
