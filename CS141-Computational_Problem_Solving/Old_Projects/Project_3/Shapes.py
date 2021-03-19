import sys
import random
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
#Seperate in files to make shapedrawer to make the file, and the shapes to define the shapes properties Shapes.py needs to define different
#shapes, don't have to paint
class Shape(QWidget):

    def __init__(self,x1,y1):
        self.length = random.randint(10,40)#make sure it doesn't go past the window,
        self.width = random.randint(10,40)
        self.positionx = x1
        self.positiony = y1
        self.color_brush = (QColor(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.color_pen = self.color_brush

class Square(Shape):#Need to be in the middle
    def __init__(self,x1,y1):#need x1 and y1
        super().__init__(x1,y1)
        self.middlex = self.length/2
        self.middley = self.length/2
        edgex = self.positionx + self.length
        edgey = self.positiony + self.length
        edge0x = self.positionx - self.middlex
        edge0y = self.positiony - self.middley
        if edgex > 500:
            self.positionx = 500-self.length
            self.middlex = 0
        if edge0x < 0:
            self.positionx = 0
            self.middlex = 0
        if edgey > 500:
            self.positiony = 500-self.length
            self.middley = 0
        if edge0y < 0:
            self.positiony = 0
            self.middley = 0

    def draw(self,qp):#define a draw method, so when we call it, it automatically draws. Pass Qpainter object as a drawing
        qp.setBrush(self.color_brush)#reupdates the list so it changes between squares and rectangles
        qp.setPen(self.color_pen)
        qp.drawRect(self.positionx - self.middlex,self.positiony-self.middley,self.length,self.length)

class Rectangle(Shape):

    def __init__(self,x1,y1):#need x1 and y1
        super().__init__(x1,y1)
        self.middlex = self.length/2
        self.middley = self.width/2
        edgex = self.positionx + self.length
        edgey = self.positiony + self.width
        edge0x = self.positionx - self.middlex
        edge0y = self.positiony - self.middley
        if edgex > 500:
            self.positionx = 500-self.length
            self.middlex = 0
        if edge0x < 0:
            self.positionx = 0
            self.middlex = 0
        if edgey > 500:
            self.positiony = 500-self.width
            self.middley = 0
        if edge0y < 0:
            self.positiony = 0
            self.middley = 0

    def draw(self,qp):
        qp.setBrush(self.color_brush)
        qp.setPen(self.color_pen)
        qp.drawRect(self.positionx - self.middlex,self.positiony - self.middley,self.length,self.width)

#click can't be on the boundary or outside, don't have to create specific class for isoscles or equilateral,
#it just has to be able to create those triangles.
class Triangle(Shape):
    def __init__(self,x1,y1):
        super().__init__(x1,y1)
        self.p1xside = random.randint(-40,40)
        self.p2xside = random.randint(-40,-3)
        self.p3xside = random.randint(3,40)
        g = random.randint(1,2)
        if g == 1:
            self.p1yup = random.randint(-40,-3)
            self.p2ydown = random.randint(3,40)
            self.p3ydown = random.randint(3,40)
        if g == 2:
            self.p1yup = random.randint(3,40)
            self.p2ydown = random.randint(-40,-3)
            self.p3ydown = random.randint(-40,-3)
        self.posx = self.positionx - ((self.p1xside + self.p2xside + self.p3xside)/3)
        self.posy =  self.positiony - ((self.p1yup + self.p2ydown + self.p3ydown)/3)
        self.x1 = self.p1xside + self.posx
        self.x2 = self.p2xside + self.posx
        self.x3 = self.p3xside + self.posx
        self.y1 = self.p1yup + self.posy
        self.y2 = self.p2ydown + self.posy
        self.y3 = self.p3ydown + self.posy
        while self.x1 > 500 or self.x2 > 500 or self.x3 > 500 or self.x1 < 0 or self.x2 < 0 or self.x3 < 0:
            self.p1xside = random.randint(-40,40)
            self.p2xside = random.randint(-40,-3)
            self.p3xside = random.randint(3,40)
            self.posx = self.positionx - ((self.p1xside + self.p2xside + self.p3xside)/3)
            self.x1 = self.p1xside + self.posx
            self.x2 = self.p2xside + self.posx
            self.x3 = self.p3xside + self.posx
        while self.y1 > 500 or self.y2 > 500 or self.y3 > 500 or self.y1 < 0 or self.y2 < 0 or self.y3 < 0:
            self.p1yup = random.randint(-40,-3)
            self.p2ydown = random.randint(3,40)
            self.p3ydown = random.randint(3,40)
            self.posy =  self.positiony - ((self.p1yup + self.p2ydown + self.p3ydown)/3)
            self.y1 = self.p1yup + self.posy
            self.y2 = self.p2ydown + self.posy
            self.y3 = self.p3ydown + self.posy

    def draw(self,qp):
        qp.setBrush(self.color_brush)
        qp.setPen(self.color_pen)
        qp.drawPolygon(
        QPoint(self.x1,self.y1),
        QPoint(self.x2,self.y2),
        QPoint(self.x3,self.y3)
        )

#triangle is graded leniently, as long as the clicking location is within the triangle, it's full credit.
#triangle should be any kind of triangle, isoscles, equilateral, some random triangle

class Circle(Shape):
    def __init__(self,x1,y1):
        super().__init__(x1,y1)
        self.middlex = self.length/2
        self.middley = self.length/2
        edgex = self.positionx + self.length
        edgey = self.positiony + self.length
        edge0x = self.positionx - self.middlex
        edge0y = self.positiony - self.middley
        if edgex > 500:
            self.positionx = 500-self.length
            self.middlex = 0
        if edge0x < 0:
            self.positionx = 0
            self.middlex = 0
        if edgey > 500:
            self.positiony = 500-self.length
            self.middley = 0
        if edge0y < 0:
            self.positiony = 0
            self.middley = 0

    def draw(self,qp):
        qp.setBrush(self.color_brush)
        qp.setPen(self.color_pen)
        qp.drawEllipse(self.positionx - self.middlex,self.positiony - self.middley,self.length,self.length)


class Ellipse(Shape):
    def __init__(self,x1,y1):
        super().__init__(x1,y1)
        self.middlex = self.length/2
        self.middley = self.width/2
        edgex = self.positionx + self.length
        edgey = self.positiony + self.width
        edge0x = self.positionx - self.middlex
        edge0y = self.positiony - self.middley
        if edgex > 500:
            self.positionx = 500-self.length
            self.middlex = 0
        if edge0x < 0:
            self.positionx = 0
            self.middlex = 0
        if edgey > 500:
            self.positiony = 500-self.width
            self.middley = 0
        if edge0y < 0:
            self.positiony = 0
            self.middley = 0

    def draw(self,qp):
        qp.setBrush(self.color_brush)
        qp.setPen(self.color_pen)
        qp.drawEllipse(self.positionx - self.middlex,self.positiony - self.middley,self.length,self.width)


#HINTS 3/19
#Except for triangle, we only need to consider the horizontal and vertical position.
#However, for the triangle, we need to consider every possible angle, it needs to be rotated by any single degree.
#The random size means the width and size should be random. For full credit, beyond randomizing the size, the shape must be small enough to stay within the 500x500
#window.
#In order to get the .5 and click anywhere within the center of the window the size of the shape shouldn't go beyond the window, but if it's near the edge and it's
#outside then its fine.
#can add sound on apps for bonus point.
#In grading, they'll only launch the ShapeDrawer.py file. They already gave us the skeleton file
#Need to create a new file called shapes.py and define the must have shapes and the properties associated with it. In order to do that, use inheritance, which Means
#we need to define a base class called shape.
#Must pass the qp as an argument. We can pass the qp in the paintevent as qp. Pass the qp as an additional argument so we don't have to make another object.
#Only need 6 classes, one for the base shape and 5 for the other classes. Shapes.py is a helper file.
