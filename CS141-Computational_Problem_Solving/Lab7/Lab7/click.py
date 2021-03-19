import sys
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Click(QWidget):
    
  def __init__(self):
    super().__init__()           
    self.setGeometry(300, 300, 550, 600)
    self.setWindowTitle('Click')
    self.show()              
  
  def mousePressEvent(self, event):
    print('You clicked at ' + str(event.x()) + ',' + str(event.y()) + '.')
  
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    # draw things here
    qp.end()
    
if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = Click()
  sys.exit(app.exec_())