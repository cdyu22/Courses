import sys, threading, time
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDialog, QInputDialog, QErrorMessage

ROWS = 5
SEATS = 3
CELL_SIZE = 90
GRID_ORIGINX = 50
GRID_ORIGINY = 50

class Seating(QWidget):

  def __init__(self): #this is line 14
    super().__init__()
    self.__desks = [['']*SEATS]*ROWS
    self.setWindowTitle('Seating Chart')
    self.setGeometry(300, 300, 2 * GRID_ORIGINX + CELL_SIZE * SEATS, \
        3 * GRID_ORIGINY + CELL_SIZE * ROWS)
    self.show()


  def paintEvent(self, event): #this is line 23
    qp = QPainter()
    blackPen = QPen(Qt.black)
    qp.begin(self)
    qp.setPen(blackPen)
    for r in range(ROWS):
      for c in range(SEATS):
        qp.drawRect(GRID_ORIGINX + c * CELL_SIZE, GRID_ORIGINY + r * CELL_SIZE, CELL_SIZE,\
         CELL_SIZE)
        qp.setPen(Qt.blue)
        qp.drawText(GRID_ORIGINX + c * CELL_SIZE + 3, GRID_ORIGINY + r * CELL_SIZE + 20,\
            self.__desks[r][c])
        qp.setPen(blackPen)
    qp.end()

  def mousePressEvent(self, event): #this is line 38
    row = (event.y() - GRID_ORIGINY) // CELL_SIZE
    col = (event.x() - GRID_ORIGINX) // CELL_SIZE
    if 0 <= row < ROWS and 0 <= col < SEATS:
      name,ok = QInputDialog.getText(self, 'Add a guest', 'Enter name:')
      if(len(name)>15):
          QErrorMessage(self).showMessage('Name too long, please try again. Must be less than 15 letters.')
      else:
        self.__desks[row][col] = name
    self.update()


  def __is_full(self): #this is line 50
    for place in self.__desks:
        for spot in place:
            if spot == '':
                return False
        return True

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Seating()
  sys.exit(app.exec_())
