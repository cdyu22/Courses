#Prior Work
class ITriangle(Shape):
    def __init__(self,x1,y1):
        super().__init__(x1,y1)
        self.distance = random.randint(300,400)
        self.x1distance = self.distance - random.randint(10,200)
        self.y1distance = self.distance - self.x1distance
        self.x1distance = self.x1distance**.5
        self.y1distance = self.y1distance**.5
        self.x2distance = self.distance - random.randint(10,200)
        self.y2distance = self.distance - self.x2distance
        self.x2distance = self.x2distance**.5
        self.y2distance = self.y2distance**.5
        q = random.randint(0,1)
        w = random.randint(0,1)
        e = random.randint(0,1)
        r = random.randint(0,1)
        if q == 0:
            self.x1distance = self.x1distance*-1
        else:
            pass
        if w == 0:
            self.x2distance = self.x2distance*-1
        else:
            pass
        if e == 0:
            self.y1distance = self.y1distance*-1
        else:
            pass
        if r == 0:
            self.y2distance = self.y2distance*-1
        else:
            pass

    def draw(self,qp):
        qp.setBrush(self.color_brush)
        qp.setPen(self.color_pen)
        qp.drawPolygon(QPoint(self.positionx,self.positiony),QPoint(self.positionx + self.x1distance,self.positiony + self.y1distance),QPoint(self.positionx + self.x2distance,self.positiony + self.y2distance))
#click can't be on the boundary or outside, don't have to create specific class for isoscles or equilateral, it just has to be able to create those triangles.
class ETriangle(Shape):
    def __init__(self,x1,y1):
        super().__init__(x1,y1)


    def draw(self,qp):
        qp.setBrush(self.color_brush)
        qp.setPen(self.color_pen)
        qp.drawPolygon(QPoint(self.positionx,self.positiony),QPoint(self.positionx,self.positiony),QPoint(self.positionx,self.positiony))
