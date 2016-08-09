from PySide.QtGui import *
from PySide.QtCore import *
import sys

class MyWin(QWidget):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)

        self.pages = [
        # instructions | 0 - - - - - - - - - - -
            QLabel("""            Welcome to the GUIDE.

                                        You are trapped in this place. Your objective is very simple: to escape.
                                        Your only purpose is to get out, not to explore the GUIDE.
                                        You can click on the options given below to perform actions and advance towards your goal.
                                        In order to achieve this you have to keep 3 things in mind:

                                        1.    There IS a way out.
                                        2.    There are NOT closed loops, the game changes with each click.
                                        3.    The closer you look, the less you see.""",self),
        # text1 | 1 - - - - - - - - - - -
        QLabel("""                  You are on a gray room. To your left is a long hallway.
                  To your right there is another long hallway. What do you want to do?""", self),
       # text2A | 2 - - - - - - - - - - -
        QLabel("""                  You went left. At the end of the hallway there is a curve to go right.
                 What do you want to do?""", self),
        # text2B | 3 - - - - - - - - - - -
        QLabel("""                  You went right. At the end of the hallway there is a curve to go left.
                 What do you want to do?""",self),
        # text3A5A | 4 - - - - - - - - - - -
        QLabel("""                   You approached to see what is behind the curve. It is a dead end. You have to go back.""",self),
        # text3B5B | 5 - - - - - - - - - - -
        QLabel("""                  You are back to where you started. You are on a gray room.
                 To your left is a long hallway. To your right there is another long hallway.
                 What do you want to do?""",self),
        # text4A6A | 6 - - - - - - - - - - -
        QLabel("""                    You are on the left hallway. At the end of the hallway there is a curve to go right.
                  What do you want to do? """,self),
        # text4B6B | 7 - - - - - - - - - - -
        QLabel("""                    You are on the right hallway. At the end of the hallway there is a curve to go left.
                  What do you want to do? """,self),
        # text6C7B8B | 8 - - - - - - - - - - -
        QLabel("""                    If you want to get out of the GUIDE, just get out.""",self),
        # text7C8A | 9 - - - - - - - - - - -
        QLabel("""                    You do.""",self)]

        # - - - - - - - - - - -  Pages creation  - - - - - - - - - - -

        self.stack =  QStackedWidget(self)
        self.stack.addWidget(self.pages[0])
        self.stack.addWidget(self.pages[1])
        self.stack.addWidget(self.pages[2])
        self.stack.addWidget(self.pages[3])
        self.stack.addWidget(self.pages[4])
        self.stack.addWidget(self.pages[5])
        self.stack.addWidget(self.pages[6])
        self.stack.addWidget(self.pages[7])
        self.stack.addWidget(self.pages[8])
        self.stack.addWidget(self.pages[9])


        # - - - - - - - - -- Button Statement - - - - - - - - - - -

        self.beginButton = QPushButton("BEGIN", self)
        # 1
        self.goRightButtonA = QPushButton ("GO RIGHT", self)
        self.goLeftButtonA = QPushButton("GO LEFT", self)
        # 2
        self.curveButtonA = QPushButton ("GO AND SEE WHAT IS BEHIND THE CURVE",self)
        self.curveButtonB = QPushButton ("GO AND SEE WHAT IS BEHIND THE CURVE",self)
        self.goBackButtonCenter = QPushButton("GO BACK",self)
        # 3
        self.goLeftButtonB = QPushButton("GO LEFT",self)
        self.goRightButtonB = QPushButton("GO RIGHT",self)
        self.goBackButtonLeftHallway = QPushButton("GO BACK",self)
        self.goBackButtonRightHallway = QPushButton("GO BACK",self)
        # 4
        self.curveButtonA1 = QPushButton("GO AND SEE WHAT IS BEHIND THE CURVE", self)
        self.curveButtonB1 = QPushButton ("GO AND SEE WHAT IS BEHIND THE CURVE",self)
        self.goBackButtonCenter2 = QPushButton("GO BACK",self)
        # 5
        self.goBackButtonLeftHallway2 = QPushButton("GO BACK",self)
        self.goBackButtonRightHallway2 = QPushButton ("GO BACK",self)
        self.goLeftButtonC = QPushButton("GO LEFT",self)
        self.goRightButtonC = QPushButton("GO RIGHT",self)
        self.getOutButton = QPushButton("GET OUT OF THE GUIDE",self)
        # 6
        self.iDontKnowButton = QPushButton("I DON'T KNOW HOW TO",self)
        self.curveButtonA2 = QPushButton("GO AND SEE WHAT IS BEHIND THE CURVE",self)
        self.curveButtonB2 = QPushButton("GO AND SEE WHAT IS BEHIND THE CURVE",self)




        #  - - - - - - - - - - - - - - - - - - - - - - Mask Image - - - - - - - - - - - - - - - - - - - - - - - - - - -

        maskicon = QPixmap('Icons8-Windows-8-Cinema-Comedy-Mask.ico')
        maskicon = maskicon.scaled(120,120)
        mask = QLabel()
        mask.setPixmap(maskicon)
        mask.setAlignment(Qt.AlignCenter)



        # - - - - - - - - - - - - - - - -- -- - - - -  Layout - - - - - - - - - - - - - - - - - - - - - - - - -

        # What is being shown

        self.layout = QVBoxLayout(self)
        empty=QLabel(" ")
        self.layout.addWidget(empty)
        self.layout.addWidget(empty)
        self.layout.addWidget(empty)
        self.layout.addWidget(mask)
        self.layout.addWidget(empty)
        self.layout.addWidget(empty)
        self.layout.addWidget(empty)
        self.layout.addWidget(self.stack)

    # - - - - - - - - - - - Buttons addition
        self.layout.addWidget(self.beginButton)
        # 1
        self.layout.addWidget(self.goLeftButtonA)
        self.layout.addWidget(self.goRightButtonA)
        # 2
        self.layout.addWidget(self.curveButtonA)
        self.layout.addWidget(self.curveButtonB)
        self.layout.addWidget(self.goBackButtonCenter)
        # 3
        self.layout.addWidget(self.goLeftButtonB)
        self.layout.addWidget(self.goRightButtonB)
        self.layout.addWidget(self.goBackButtonLeftHallway)
        self.layout.addWidget(self.goBackButtonRightHallway)
        # 4
        self.layout.addWidget(self.curveButtonA1)
        self.layout.addWidget(self.curveButtonB1)
        self.layout.addWidget(self.goBackButtonCenter2)
        # 5
        self.layout.addWidget(self.goBackButtonLeftHallway2)
        self.layout.addWidget(self.goBackButtonRightHallway2)
        self.layout.addWidget(self.goLeftButtonC)
        self.layout.addWidget(self.goRightButtonC)
        self.layout.addWidget(self.getOutButton)
        # 6
        self.layout.addWidget(self.iDontKnowButton)
        self.layout.addWidget(self.curveButtonA2)
        self.layout.addWidget(self.curveButtonB2)

        self.currentPage = 0

    # - - - - - - - - - - - - Button connections
        # 1
        self.beginButton.clicked.connect(self.ShowLayout1)
        self.goLeftButtonA.clicked.connect(self.ShowLayout2A)
        self.goRightButtonA.clicked.connect(self.ShowLayout2B)
        # 2
        self.curveButtonA.clicked.connect(self.ShowLayout3A5A1)
        self.curveButtonB.clicked.connect(self.ShowLayout3A5A2)
        self.goBackButtonCenter.clicked.connect(self.ShowLayout3B5B)
        # 3
        self.goLeftButtonB.clicked.connect(self.ShowLayout4A6A)
        self.goRightButtonB.clicked.connect(self.ShowLayout4B6B)
        self.goBackButtonLeftHallway.clicked.connect(self.ShowLayout4A6A)
        self.goBackButtonRightHallway.clicked.connect(self.ShowLayout4B6B)
        # 4
        self.curveButtonA1.clicked.connect(self.ShowLayout3A5A12)
        self.curveButtonB1.clicked.connect(self.ShowLayout3A5A22)
        self.goBackButtonCenter2.clicked.connect(self.ShowLayout3B5B2)
        # 5
        self.goBackButtonLeftHallway2.clicked.connect(self.ShowLayout4A6A2)
        self.goBackButtonRightHallway2.clicked.connect(self.ShowLayout4B6B2)
        self.goLeftButtonC.clicked.connect(self.ShowLayout4A6A2)
        self.goRightButtonC.clicked.connect(self.ShowLayout4B6B2)
        self.getOutButton.clicked.connect(self.ShowLayout6C7B8B)
        # 6
        self.iDontKnowButton.clicked.connect(self.ShowLayout7C8A)
        self.curveButtonA2.clicked.connect(self.ShowLayout3A5A12)
        self.curveButtonB2.clicked.connect(self.ShowLayout3A5A22)

    # - - - - - - - - - - - - Button Hidding
        # 1
        self.goLeftButtonA.hide()
        self.goRightButtonA.hide()
        # 2
        self.curveButtonA.hide()
        self.curveButtonB.hide()
        self.goBackButtonCenter.hide()
        # 3
        self.goLeftButtonB.hide()
        self.goRightButtonB.hide()
        self.goBackButtonLeftHallway.hide()
        self.goBackButtonRightHallway.hide()
        # 4
        self.curveButtonA1.hide()
        self.curveButtonB1.hide()
        self.goBackButtonCenter2.hide()
        # 5
        self.goBackButtonLeftHallway2.hide()
        self.goBackButtonRightHallway2.hide()
        self.goLeftButtonC.hide()
        self.goRightButtonC.hide()
        self.getOutButton.hide()
        # 6
        self.iDontKnowButton.hide()
        self.curveButtonA2.hide()
        self.curveButtonB2.hide()

    def ShowLayout1(self):
        self.currentPage = 1
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goLeftButtonA.show()
        self.goRightButtonA.show()
        self.beginButton.hide()

    def ShowLayout2A(self):
        self.currentPage = 2
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.curveButtonA.show()
        self.goBackButtonCenter.show()
        self.goRightButtonA.hide()
        self.goLeftButtonA.hide()

    def ShowLayout2B(self):
        self.currentPage = 3
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.curveButtonB.show()
        self.goBackButtonCenter.show()
        self.goRightButtonA.hide()
        self.goLeftButtonA.hide()

    def ShowLayout3A5A1(self):
        self.currentPage = 4
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goBackButtonLeftHallway.show()
        self.curveButtonA.hide()
        self.goBackButtonCenter.hide()

    def ShowLayout3A5A2(self):
        self.currentPage = 4
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goBackButtonRightHallway.show()
        self.curveButtonB.hide()
        self.goBackButtonCenter.hide()

    def ShowLayout3B5B(self):
        self.currentPage = 5
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goLeftButtonB.show()
        self.goRightButtonB.show()
        self.curveButtonB.hide()
        self.curveButtonA.hide()
        self.goBackButtonCenter.hide()

    def ShowLayout4A6A(self):
        self.currentPage = 6
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.curveButtonA1.show()
        self.goBackButtonCenter2.show()
        self.goBackButtonLeftHallway.hide()
        self.goLeftButtonB.hide()
        self.goRightButtonB.hide()

    def ShowLayout4B6B(self):
        self.currentPage = 7
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.curveButtonB1.show()
        self.goBackButtonCenter2.show()
        self.goBackButtonRightHallway.hide()
        self.goLeftButtonB.hide()
        self.goRightButtonB.hide()

    def ShowLayout3A5A12(self):
        self.currentPage = 4
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goBackButtonLeftHallway2.show()
        self.getOutButton.show()
        self.curveButtonA1.hide()
        self.goBackButtonCenter2.hide()
        self.curveButtonA2.hide()

    def ShowLayout3A5A22(self):
        self.currentPage = 4
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goBackButtonRightHallway2.show()
        self.getOutButton.show()
        self.curveButtonB1.hide()
        self.goBackButtonCenter2.hide()
        self.curveButtonB2.hide()

    def ShowLayout3B5B2(self):
        self.currentPage = 5
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.goLeftButtonC.show()
        self.goRightButtonC.show()
        self.curveButtonB1.hide()
        self.curveButtonA1.hide()
        self.goBackButtonCenter2.hide()
        self.curveButtonA2.hide()
        self.curveButtonB2.hide()
        self.getOutButton.hide()

    def ShowLayout4A6A2(self):
        self.currentPage = 6
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.curveButtonA2.show()
        self.getOutButton.show()
        self.goBackButtonCenter2.show()

        self.goBackButtonLeftHallway2.hide()
        self.goLeftButtonC.hide()
        self.goRightButtonC.hide()
        self.getOutButton.hide()

    def ShowLayout4B6B2(self):
        self.currentPage = 7
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.curveButtonB2.show()
        self.goBackButtonCenter2.show()
        self.getOutButton.show()
        self.goBackButtonRightHallway2.hide()
        self.goLeftButtonC.hide()
        self.goRightButtonC.hide()
        self.getOutButton.hide()

    def ShowLayout6C7B8B(self):
        self.currentPage = 8
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.iDontKnowButton.show()
        self.goBackButtonLeftHallway2.hide()
        self.getOutButton.hide()
        self.curveButtonA2.hide()
        self.goBackButtonCenter2.hide()
        self.goBackButtonRightHallway2.hide()
        self.curveButtonB2.hide()

    def ShowLayout7C8A(self):
        self.currentPage = 9
        if self.currentPage >= len(self.pages):
            self.currentPage = 0
        self.stack.setCurrentWidget(self.pages[self.currentPage])
        self.getOutButton.show()
        self.iDontKnowButton.hide()


    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Congratulations',
            "You achieved your goal. "
            "You got out of the GUIDE, the Graphical User Interface Destroying Experience", QMessageBox.Close)

        if reply == QMessageBox.Close:
            event.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    #mywin.move(0,0)
    mywin.setGeometry(300, 60, 800, 600)
    mywin.setWindowTitle('GUIDE')
    mywin.setWindowIcon(QIcon('Icons8-Windows-8-Cinema-Comedy-Mask.ico'))
    mywin.show()
    sys.exit(app.exec_())
