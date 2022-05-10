from graphics import *

def drawSquare(tlx, tly, size, win):
    square = Rectangle(Point(tlx, tly), Point(tlx + size, tly + size))
    square.setFill("Black")
    square.draw(win)


def drawSquares(win:GraphWin):
    size = win.getWidth() // 3
    tlX = win.getWidth() // 2 - size // 2
    tlY = win.getHeight() // 2 - size // 2
    square = Rectangle(Point(tlX, tlY), Point(tlX + size, tlY + size))
    square.setFill("Black")
    square.draw(win)

    drawTopCenter(Point(win.getWidth()//2, win.getHeight()//2), size, win)
    drawBottomCenter(Point(win.getWidth()//2, win.getHeight()//2), size, win)
    drawRight(Point(win.getWidth() // 2, win.getHeight() // 2), size, win)
    drawLeft(Point(win.getWidth() // 2, win.getHeight() // 2), size, win)
    drawTL(Point(win.getWidth() // 2, win.getHeight() // 2), size, win)
    drawTR(Point(win.getWidth() // 2, win.getHeight() // 2), size, win)
    drawBL(Point(win.getWidth() // 2, win.getHeight() // 2), size, win)
    drawBR(Point(win.getWidth() // 2, win.getHeight() // 2), size, win)


def drawTopCenter(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX()
    newCenterY = oldCenter.getY() - oldSize
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawBottomCenter(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX()
    newCenterY = oldCenter.getY() + oldSize
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawRight(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX() + oldSize
    newCenterY = oldCenter.getY()
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawLeft(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX() - oldSize
    newCenterY = oldCenter.getY()
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawTL(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX() - oldSize
    newCenterY = oldCenter.getY() - oldSize
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawTR(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX() + oldSize
    newCenterY = oldCenter.getY() - oldSize
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawBL(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX() - oldSize
    newCenterY = oldCenter.getY() + oldSize
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def drawBR(oldCenter: Point, oldSize:int, win:GraphWin):
    thisSize = oldSize // 3
    newCenterX = oldCenter.getX() + oldSize
    newCenterY = oldCenter.getY() + oldSize
    tlx = newCenterX - thisSize // 2
    tly = newCenterY - thisSize // 2
    drawSquare(tlx, tly, thisSize, win)
    if thisSize > 3:
        drawTopCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawBottomCenter(Point(newCenterX, newCenterY), thisSize, win)
        drawRight(Point(newCenterX, newCenterY), thisSize, win)
        drawLeft(Point(newCenterX, newCenterY), thisSize, win)
        drawTR(Point(newCenterX, newCenterY), thisSize, win)
        drawTL(Point(newCenterX, newCenterY), thisSize, win)
        drawBL(Point(newCenterX, newCenterY), thisSize, win)
        drawBR(Point(newCenterX, newCenterY), thisSize, win)


def main():
    win = GraphWin("Triangle", 900, 900)
   # win.setBackground("Black")
    drawSquares(win)


    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
