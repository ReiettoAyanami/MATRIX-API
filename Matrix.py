import pygame
from pygame import Rect
from ColorData import ColorData

class Matrix:

    """

    A class used to graphically represent the led matrix connected to the arduino.

    Attributes:

        pos: (tuple) the top left corner of the matrix.
        buttonSize: (tuple) the size of the buttons.
        size: (int) the size in pixels of the matrix.
        mat: (list[list[Button]]) a list containing buttons that represents every pixel in the physical matrix.
        brightness: (int) the brightness that has to be sent to the physical matrix.
        changed: (list[ColorData]) the pixels changed from the last frame sent to the arduino.
        brightnessChanged: (list[ColorData]) the list of pixels that changed modifying the brightness value.
        nextFrame: (list[list[Button]]) a matrix containing the next frame that will be displayed and then swapped if different from the current frame contained in mat.

    """


    def __init__(self,pos:tuple = (0,0),buttonSize:tuple = (1,1),rect:pygame.Rect = None, size:int = 8) -> None:
        """
        Args:

            pos: the top left corner of the matrix.
            buttonSize: the size of the buttons.
            rect: the general dimensions of the matrix, if assigned, pos and buttonSize will be ignored and the respective attributes will be calculated based on the rect's attributes.
            size: the size in pixels of the matrix.

        """

        self.pos = self.x, self.y = pos
        self.buttonSize = self.buttonW, self.buttonH = buttonSize

        if rect:
            self.pos = self.x, self.y = Rect(rect).topleft
            self.buttonSize = self.buttonW, self.buttonH = Rect(rect).w/size, Rect(rect).h/size

        self.size = size
        self.changed = []
        self.brightnessChanged = []
        self.nextFrame = [[[0,0,0] for j in range(self.size)]for i in range(self.size)]
        self.mat = [[[0,0,0] for j in range(self.size)]for i in range(self.size)]
        self.brightness = 255
                
    def setBrightness(self, newBrightness:int | float) -> None:
        """
        Changes the brightness parameter and adds data to the changed pixels.

        Args:
            newBrightness: the new brightness value.
        """
        
        self.brightnessChanged = []
        
        if self.brightness != newBrightness:
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    if self.mat[i][j] != [int(self.mat[i][j][k] * newBrightness/255) for k in range(3)]:
                        self.brightnessChanged.append(ColorData((j * self.size )+ i, [int(self.mat[i][j][k] * newBrightness/255) for k in range(3)]))
        self.brightness = newBrightness
        
    

    def setColorAt(self,x:int,y:int,color:list[int]):
        
        """
        Updates the button color at a given position.

        Args:
            x: the x position on the matrix.
            y: the y position on the matrix.
            color: the color that will replace the old one.

        """


        self.mat[x][y] = color

    def getMatrixChanges(self) -> list[ColorData]:
        
        """
        Keeps track of the tiles changed on the matrix and changes them.

        Returns:
            A list of ColorData objects:
        """


        self.changed = []
        self.changed += self.brightnessChanged
    

        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):

                if self.mat[i][j] != self.nextFrame[i][j]:
                    self.mat[i][j] = self.nextFrame[i][j]
                    self.changed.append(ColorData(((j * self.size )+ i), [int(self.mat[i][j][k] * self.brightness/255) for k in range(3)]))

        return self.changed
