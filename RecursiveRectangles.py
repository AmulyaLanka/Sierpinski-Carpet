#############################
# Amulya Lanka
# CIS 2532
#
#############################
from graphics import *

class RecursiveGraphic(object):
    
    def __init__(self, win: GraphWin):
        self.size = win.getWidth() // 2
        self.startWidth = 250
        self.startHeight = 200
        self.tlX = win.getWidth() // 2 - self.startWidth // 2
        self.tlY = win.getHeight() // 2 - self.startHeight // 2

    def drawRectangles(self, win):
        self.drawCenterRectangle(win)
        # Make the initial call to your method(s) here
        self.drawTL(self.tlX - self.startWidth // 2, self.tlY - self.startHeight // 2, self.startWidth // 2, self.startHeight // 2, win)
        self.drawTR(self.tlX + self.startWidth, self.tlY - self.startHeight // 2, self.startWidth // 2, self.startHeight // 2, win)
        self.drawBL(self.tlX - self.startWidth // 2, self.tlY + self.startHeight, self.startWidth // 2, self.startHeight // 2, win)
        self.drawBR(self.tlX + self.startWidth, self.tlY + self.startHeight, self.startWidth // 2, self.startHeight // 2, win)

    def drawCenterRectangle(self, win):
        rect = Rectangle(Point(self.tlX, self.tlY), Point(self.tlX + self.startWidth, self.tlY + self.startHeight))
        rect.setFill("Black")
        rect.draw(win)

    # Create your recursive method(s) here

    def drawTL(self,X, Y, width, height, win):
        rect = Rectangle(Point(X, Y), Point(X + width, Y + height))
        rect.setFill("Black")
        rect.draw(win)
        if width > 1:
            self.drawTL(X - width // 2, Y - height // 2, width // 2, height // 2, win)
            self.drawTR(X + width, Y - height // 2, width // 2, height// 2, win)
            self.drawBL(X - width // 2, Y + height, width // 2, height// 2, win)

    def drawTR(self, X, Y, width, height, win):
        rect = Rectangle(Point(X, Y), Point(X + width, Y + height))
        rect.setFill("Black")
        rect.draw(win)
        if width > 1:
            self.drawTL(X - width // 2, Y - height // 2, width // 2, height // 2, win)
            self.drawTR(X + width, Y - height // 2, width // 2, height // 2, win)
            self.drawBR(X + width, Y + height, width // 2, height // 2, win)

    def drawBL(self, X, Y, width, height, win):
        rect = Rectangle(Point(X, Y), Point(X + width, Y + height))
        rect.setFill("Black")
        rect.draw(win)
        if width > 1:
            self.drawTL(X - width // 2, Y - height // 2, width // 2, height // 2, win)
            self.drawBL(X - width // 2, Y + height, width // 2, height // 2, win)
            self.drawBR(X + width, Y + height, width // 2, height // 2, win)

    def drawBR(self, X, Y, width, height, win):
        rect = Rectangle(Point(X, Y), Point(X + width, Y + height))
        rect.setFill("Black")
        rect.draw(win)
        if width > 1:
            self.drawTR(X + width, Y - height // 2, width // 2, height // 2, win)
            self.drawBL(X - width // 2, Y + height, width // 2, height // 2, win)
            self.drawBR(X + width, Y + height, width // 2, height // 2, win)

def main():
    win = GraphWin("Recursive Rectangles", 1000, 650)
    rg = RecursiveGraphic(win)
    rg.drawRectangles(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()



################################################################################################################

# from graphics import *
# import random
# import time
#
#
# class Card():
#     def __init__(self, point, lenny):
#
#         self.__location = point  # private attribute
#         self.__face = lenny
#         self.__point1 = Point((self.__location.getX()-25), (Point(self.__location.getY()-25)))
#
#         self.__point2 = Point((self.__location.getX()+25), (Point(self.__location.getY()+25)))
#
#         self.__button = Rectangle(self.__point1, self.__point2)
#
#     def getface(self):
#         return self.__face
#
#     def showFace(self, win):
#         textBox = Text(self.__location, self.__face)
#         textBox.draw(win)
#         time.sleep(.5)
#         textBox.undraw()
#
#     def drawButton(self, win):
#         self.__button.setFill('pink')
#         self.__button.draw(win)
#
#     def clickTheButton(self, win, click):
#         clickX = click.getX()
#         clickY = click.getY()
#         #if x <= x1 && x >= x2 && y <= y1 && y >= y2
#         if clickX <= self.__point1.getX() and clickX >= self.__point2.getX() and  clickY <= self.__point1.getY() and clickY >= self.__point2.getY():
#
#             self.__button.undraw()
#             self.showFace(win)
#             return True
#         else:
#             return False
#
# def main():
#     win = GraphWin("Memory Game", 500, 200)
#     win.setBackground(color_rgb(255, 255, 51))
#
#     data = ["( ͡° ͜ʖ ͡°)", "¯\_(ツ)_/¯", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)","ಠ_ಠ",
#             "( ͡° ͜ʖ ͡°)", "¯\_(ツ)_/¯", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "ಠ_ಠ"]
#
#     listOfPoints = [Point(50,50), Point(150, 50), Point(250, 50), Point(350, 50), Point(450, 50),
#                     Point(50, 150), Point(150, 150), Point(250, 150), Point(350, 150), Point(450, 150)]
#
#     #shuffle either listofpoints or data
#     random.shuffle(data)
#     cards = []
#     for i in range(10):
#         cards.append(Card(listOfPoints[i], data[i]))
#
#     for card in cards:
#         card.drawButton()
#
#     cardsFacingUp = 0
#     matchesCount = 0
#     while matchesCount != 5:
#         click = win.getMouse()
#         card1 = 0
#         card2 = 0
#
#         for card in cards:
#             if card.clickTheButton(win, click):
#                 break
#             else:
#                 card1 += 1
#         click = win.getMouse()
#
#         for card in cards:
#             if card.clickTheButton(win, click):
#                 break
#             else:
#                 card2 += 1
#
#         if cards[card1].getface() == cards[card2].getface():
#             if card1 < card2:
#                 cards.pop(card2)
#                 cards.pop(card1)
#             else:
#                 cards.pop(card1)
#                 cards.pop(card2)
#             matchesCount += 1
#         else:
#             cards[card1].drawButton(win)
#             cards[card2].drawButton(win)
#
# if __name__ == '__main__':
#     main()





