import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

RECX = 200
RECY = 200
RECWIDTH = 300
RECHEIGHT = 300
WINDOWX = 200
WINDOWY = 400

class DoubleClick(QWidget):
    
  def __init__(self):
    super().__init__()           
    self.setGeometry(WINDOWX, WINDOWY, 600, 600)
    self.setWindowTitle('Double Click')
    self.__inside = False
    self.show()              
  
  def __inRect(self,x,y):
  	return (RECX<x<RECX+RECWIDTH and RECY<y<RECY+RECHEIGHT)
  	
  def mouseDoubleClickEvent(self, event):
    self.__inside = False
    if(self.__inRect(event.x(),event.y())):
    	self.__inside=True
    self.update()
  
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    greenPen = QPen(QBrush(Qt.green),10)
    qp.setPen(greenPen)
    qp.drawRect(RECX,RECY,RECWIDTH,RECHEIGHT)
    if(self.__inside):
        textPen = QPen(QBrush(Qt.red),3)
        qp.setPen(textPen)
        qp.drawText(5, 30,"Got it!")
    qp.end()
    
if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = DoubleClick()
  sys.exit(app.exec_())