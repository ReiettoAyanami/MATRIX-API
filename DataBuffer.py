from typing import Any
from ColorData import *

class DataBuffer:

    def __init__(self, startBuff:list[ColorData], maxBufferDimension:int = 64) -> None:
        self.__buffer = startBuff
        self.maxBufferDimension = maxBufferDimension
    
    def addData(self,newData:list[ColorData]) -> None:
        for d in newData:
            if len(self.__buffer) > self.maxBufferDimension:
                break
            self.__buffer.append(d)

    def clear(self) -> None:
        self.__buffer = []

    def pop(self, idx:int) -> None:
        self.__buffer.pop(idx)


    def __len__(self) -> int:
        return len(self.__buffer)

    def __getitem__(self, key) -> Any:
        return self.__buffer[key]

    def __setitem__(self, key, newValue) -> Any:
        self.__buffer[key] = newValue

