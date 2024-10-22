# DragAndDrop

This is a demo of using Pygame to create a system where you can pick up, drag and drop blocks.

When the While loop is running, the program is waiting for you to hold down the mouse button on one of the sprites.
When you do this, it becomes the "draggedblock". The block then follows the mouse around.

When you release the mouse, the block checks to see where it is, according to a game grid.
At this point, the game might take some action based on where the block has been dropped.
In this example, it "snaps in" to the grid, using the // division to round its position to the
nearest 100 pixels.

If you were making a game where you could drag items onto other ones, you could do this when they dropped
the item, or do a check in every tick of this loop, to see if the sprite was touching any other sprites.

eg.

if touching(sprite1, sprite2):
    # sprite1 is currently hovering over sprite2

