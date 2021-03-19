import sys
import random
from Shapes import Shape, Square, Rectangle, Circle, Ellipse, Triangle
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
    qp.begin(self)#all drawers are done within paintevent, when you click mouse, it'll invoke mousepressevent, need to decide which shape will be drawn for this click.
    #need to randomly generate shape. Use the list once the click happens, append shape into list, keep updating when clicking more. It'll draw
    #go through the entire list one by onelike in project description, in the paint eventi need to just use the loop, for shapes in sef.__shapes list for item
    #my_list, the variable will be assigned with elements in the given list, iteration by iteration unti. the structure helps us go thru the list
    for shape in self.__shapes:
        shape.draw(qp)#method names must be consistent, polymorphism, use draw.
    qp.end()

  def mousePressEvent(self, event):
    x = random.randint(0,4)
    if x == 0:
        self.__shapes.append(Square(event.x(),event.y()))
    if x == 1:
        self.__shapes.append(Rectangle(event.x(),event.y()))
    if x == 2:
        self.__shapes.append(Circle(event.x(),event.y()))
    if x == 3:
        self.__shapes.append(Ellipse(event.x(),event.y()))
    if x == 4:
        self.__shapes.append(Triangle(event.x(),event.y()))

    #need to updateself.))shapes whenever I do mouse click into list(), and then need to pass x and y coordinates into the object.
    #must pass event x and event y when creating a square object
    #TODO generate a random shape and add it to the list of shapes
    #with self.__shapes.append(newshape). Remove the pass line.
    self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShapeDrawer()
    sys.exit(app.exec_())

#Everytime we click the mouse we create a new shape object, which we must then put into the list, just keep adding new shape objects. Once we reinvoke the paintEvent
#the only thing we need to do is draw the shapes one by one. Self.shapes is a shapeholder to let us remember what shape it was.
#Need to reiterate over the entire list to make sure that we don't forget past shapes.
