import os
import time


class Canvas:
    """
    A canvas class to allow printing images to the console window
    """
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [['' for y in range(self._y)] for x in range(self._x)]

    def set_pos(self, pos: [int, int], mark: str) -> None:
        """
        Set the specified point on the canvas to the specified mark
        :param pos: The position to update in the form [x, y]
        :param mark: The character to place at the specified position
        """
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self) -> None:
        """
        clears the terminal screen
        """
        os.system('cls' if os.name=='nt' else 'clear')

    def print(self):
        """
        Print the current canvas to the terminal screen
        """
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))   
        time.sleep(0.05)

class TerminalScribe:
    """
    Class that controls the drawing of images to a canvas
    :param canvas: The canvas to draw on
    """
    def __init__(self, c: Canvas):
        self.canvas = canvas
        self.pos = [0, 0]
        self.mark = '*'
        self.trail='.'

    def draw(self, pos: [int, int]) -> None:
        """
        Draws a mark at the specified point on the canvas, 
        updating the previous postioitn to the trail character
        :param pos: Position to be updated in the form [x, y]
        """
        self.canvas.set_pos(self.pos, self.trail)
        self.pos = pos
        self.canvas.set_pos(self.pos, self.mark)
        self.canvas.print()

canvas = Canvas(20, 20)
scribe = TerminalScribe(canvas)

for i in range(0,10):
    for j in range(0,10):
        scribe.draw([i,j])
