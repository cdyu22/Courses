import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class EyeChart(QWidget):

  def __init__(self):
    super().__init__()
    self.setGeometry(300, 300, 200, 200)
    self.setWindowTitle('Eye Chart')
    self.__cur_keys = ''
    self.show()

  def keyPressEvent(self, event):
    if(event.text().isalpha()):
        if(len(self.__cur_keys)<5):
            self.__cur_keys += event.text().upper()
        else:
            self.__cur_keys = self.__cur_keys[1:] + event.text().upper()
    self.update()

  def mousePressEvent(self,event):
    self.__cur_keys=''#difference between space and no space?
    self.update()

  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    qp.setPen(QPen(Qt.blue))
    qp.drawText(80,100,self.__cur_keys)
    qp.end()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = EyeChart()
  sys.exit(app.exec_())
