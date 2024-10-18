from pygame_functions import *

screenSize(1000,1000)
setAutoUpdate(False)

class Block:
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.sprite = makeSprite(image)
        self.draw()
        showSprite(self.sprite)

    def move(self,x,y):
        self.x = x
        self.y = y
        self.draw()

    def draw(self):
        moveSprite(self.sprite,self.x,self.y)

    def isClicked(self):
        return spriteClicked(self.sprite)

def drawGrid():
    drawRect(100,100,800,800,"red",2)
    for row in range(200,900,100):
        drawLine(100,row,900,row,"red",2)
        drawLine(row,100,row,900, "red",2)

blocks = [Block(160,180,"b1.png"),Block(360,180,"b2.png")]


draggedBlock = None
while True:
    clearShapes()
    drawGrid()
    if not draggedBlock:
        #see if a new block has been selected
        for b in blocks:
            if b.isClicked():
                draggedBlock = b
    if draggedBlock:
        if mousePressed():
            # has been picked up
            draggedBlock.move(mouseX()-50,mouseY()-50)
        else:
            # has been dropped
            # find out which row and column the block has been dropped
            row = mouseY()//100 -1  # taken off 1 because we don't start on the far left or the top
            col = mouseX()//100 -1
            print("Dropped at ",row, col)
            draggedBlock.move(100+col*100, 100+row*100) # snap in
            draggedBlock = None

    updateDisplay()
    tick(100)
endWait()
