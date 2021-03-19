import sys #Allows us to launch applications later. Always needed when using pyqt(?)
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor  #These three lines help us import classes from the pyqt file.
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint


class Face(QWidget):#We're creating a new class named face, instead of starting from scratch we're doing an inheritance. It's a lcass that allows us to create QtWidget
#Or in other words, create a window.

  def __init__(self):
    super().__init__()#Call this class constructor method init to let it run automatically. We can use the QWidget class to make it. Starting by scratch would be a lot.
    self.setGeometry(50, 50, 500, 500) #QWidget helps us draw it out. If we just run this template, it will open a window, but it will be blank, uncustomized.
    #Set geometry sets window and size of window. The first two arguments are where we put the window on the screen. The third one is width, fourth is height.
    #Top left of the window is set at 50,50, and lines are drawn to the right and down to create window.
    self.setWindowTitle('Face') #Sets title of window, we named it face.
    self.__clicktext = 'No Click Yet'
    self.show()#IF we don't have this line, the window created will just be stored in the memory, if we want it to appear we need this command.

  def paintEvent(self, event):#Need to overload this with our own code. If not it'll just stay open. #must be called event
    qp = QPainter()
    qp.begin(self)#Need to put some code after this line.
    #To make eye, we need the x,y coordinate of the top left, the width and the height. Top left corner of window is 0,0.
    qp.drawEllipse(100,100,100,100)
    qp.drawEllipse(300,100,100,100)
    qp.setBrush(Qt.black)
    #want to make eyes follow the mouse. need to divide the movement into x and y directions.
    #qp.drawEllipse(125,125,50,50)
    #qp.drawEllipse(325,125,50,50)
    qp.setBrush(QColor(0,0,255))
    bluePen = QPen(Qt.blue,3)#3 is optional, if not it'll default to 0.
    qp.setPen(bluePen)
    qp.drawPolygon(QPoint(250,175),QPoint(300,275),QPoint(200,275))
    redPen = QPen(Qt.red,5)
    qp.setPen(redPen)
    qp.drawLine(150,300,250,350)
    qp.drawLine(250,350,350,300)
    qp.drawText(20,20,self.__clicktext)
    blackPen = QPen(Qt.black,3)
    qp.setPen(blackPen)
    qp.setBrush(Qt.black)
    if self.__clicktext == 'No Click Yet':
        qp.drawEllipse(125,125,50,50)
        qp.drawEllipse(325,125,50,50)
    else:
        qp.drawEllipse(100 + self.__x/10,100+self.__y/10,50,50)
        qp.drawEllipse(300 + self.__x/10,100+self.__y/10,50,50)
    qp.end()#Need to put this to tell the computer when it will end.

  def mousePressEvent(self, event):#This can control what we want to do after we push the mouse. Currently, by default, nothing happens.
    self.__x = event.x()
    self.__y = event.y()
    print(self.__x,self.__y)
    self.__clicktext = '(' + str(self.__x) + ',' + str(self.__y) +')'
    self.update()





    #event is a QMouse object event. Can collect a bunch of information, including the location and other information. We can use that argument to build the building
    #method. Two methods, x and y method.

if __name__ == '__main__':#This is something we haven't seen before. Means that when we run the file directly using the python command, name is a keyword.
    #When we call a function from the file, __main_ will be used with name (???) to make this comparison true, which will exclude the body of the if statement.
    #If statement isn't relally needed. Trying to import this file into another file.
    #if there's a file_1.py and file_2.py we can use an import statement to do an import from another file. so import file_1. When we run file 2 using the command
    #python file_2.py when we're trying to run file_2 with file_1 it will assign a different value in this statement, and the name will not equal main, making
    #if statement false, so python won't enter the if statement. So for that imported file we want to make sure is included.
     app = QApplication(sys.argv)#Everytime we try to call some function we just directly call it, but the pyqt function isn't like that. We need a Qapplication object.
     #This is a building class in pyqt called QApplication, creates an object called app.
     ex = Face()#Need a class instance, it'll be called Face, which is the class name.
     sys.exit(app.exec_())#This is the moment were the application will be launched. Once the application is launched, it'll exclude the constructor method(init)
     #for face class, and try to call the paintevent implicitly. Means that you can't control when a system can call that method. It'll be calld randomly.
     #sys.exit makes sure once the program is done, the program will exit.
     #Just type these three lines of code, just have to change the class name from Face. Just leave the rest of this program as it is.

#pyqt has over 600 functions, so just follow the example we do in labs and lectures to see how we can draw something using the pyqt. She's also providing a tutorial
#website. Explore by yourself online.

#Check what an overloaded function is.

### 3/19
#This will launch the code and implicitly call the paintevent to do the drawing. Will keep calling the paintevent after some times, will be called randomly
#by the system. Once the application is launched, we enter the mainloop, want to check if anything interferes, we want to catch if a mouse click happens.
#when it does, the computer will look for the mousepressevent and execute it. After that, mousepressevent is done after self.update().
#Want to change the location of the eyeball every click, we have to redraw the picture everytime, we're just changing the location of the eyeball and redrawing
#everything.
#Last question is how can we associate the location of the eyeball with the new click.
