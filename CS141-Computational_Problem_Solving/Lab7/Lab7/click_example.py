import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Click(QWidget):
    
  def __init__(self):
    super().__init__()           
    self.setGeometry(300, 300, 550, 600)
    self.setWindowTitle('Click')
    self.show()              
  
  def mousePressEvent(self, event):
    while True:
      continue
    print('You clicked at ' + str(event.x()) + ',' + str(event.y()) + '.')
  
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    greenPen = QPen(QBrush(Qt.green),10)
    qp.setPen(greenPen)
    qp.drawChord(100,100,200,200,(30*16),(120*16))
    smallGreen = QPen(QBrush(Qt.green),4)
    redPen  = QPen(QBrush(Qt.red),4)
    qp.setPen(smallGreen)
    qp.drawRect(145,149,20,20)
    qp.drawRect(251,149,20,20)
    qp.drawChord(288,119,50,50,(60*16),(120*16))
    qp.setPen(redPen)
    qp.drawEllipse(302,122,5,5)
    textPen = QPen(3)
    qp.setPen(textPen)
    qp.drawText(150,200,"TURTLE POWER!")
    qp.end()
    
if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = Click()
  sys.exit(app.exec_())
