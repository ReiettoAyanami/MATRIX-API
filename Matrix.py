import pygame
from pygame import Rect
from ColorData import ColorData

class Matrix:


    def __init__(self,size:int = 8) -> None:

        self.__size = size
        self.__changed = []
        self.__brightnessChanged = []
        self.__nextFrame = [[[0,0,0] for j in range(self.__size)]for i in range(self.__size)]
        self.__mat = [[[0,0,0] for j in range(self.__size)]for i in range(self.__size)]
        self.__brightness = 255



    @property
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, newBrightness:int) -> None:

        self.__brightnessChanged = []
        
        if self.__brightness != newBrightness:
            for i in range(len(self.__mat)):
                for j in range(len(self.__mat[i])):
                    if self.__mat[i][j] != [int(self.__mat[i][j][k] * newBrightness/255) for k in range(3)]:
                        self.__brightnessChanged.append(ColorData((j * self.__size )+ i, [int(self.__mat[i][j][k] * newBrightness/255) for k in range(3)]))
        self.__brightness = newBrightness
        
    

    def setColorAt(self,x:int,y:int,color:list[int]):
        self.__mat[x][y] = color



    def getMatrixChanges(self) -> list[ColorData]:

        self.__changed = []
        self.__changed += self.__brightnessChanged
    

        for i in range(len(self.__mat)):
            for j in range(len(self.__mat[i])):

                if self.__mat[i][j] != self.__nextFrame[i][j]:
                    self.__mat[i][j] = self.__nextFrame[i][j]
                    self.__changed.append(ColorData(((j * self.__size )+ i), [int(self.__mat[i][j][k] * self.__brightness/255) for k in range(3)]))

        return self.__changed
