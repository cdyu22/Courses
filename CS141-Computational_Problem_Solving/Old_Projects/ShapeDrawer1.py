import sys
import random
from Shapes import Shape, Ellipse
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from random import randint

class ShapeDrawer(QWidget):

  def __init__(self):
    super().__init__()
    self.__shapes = list()
    self.setGeometry(50, 50, 500, 500)
    self.setWindowTitle('Shapes')
    self.show()

  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    for shape in self.__shapes:
        shape.draw(qp)
    qp.end()

  def mousePressEvent(self, event):
    self.__shapes.append(Ellipse(event.x(),event.y()))
    self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShapeDrawer()
    sys.exit(app.exec_())
