
class ColorData:

    def __init__(self, index:int = 0, color:tuple[int] = (0,0,0)) -> None:

        self.__index = index
        self.__color = color


    def toEncodedString(self) -> str:

        """
        Transforms this object's attributes into an encoded string that will be parsed and interpreted by the arduino.

        Args:
            index : the index of the element you want to encode.

        Returns:
            A string which is formatted like this:
            
            - .iiirrrgggbbb\\n -> the format.
            - . -> start reading data;
            - iii -> index: 001;
            - rrr -> red color: 020;
            - ggg -> green color: 100;
            - bbb -> blue color: 069;
            - \\n -> stop reading data.


        """


        
        attr = [self.__index] + [self.__color[i] for i in range(len(self.__color))]
        data = '.'

        
        for i in range(len(attr)):
            
            current = str(attr[i])

            if len(current) < 3:
                
                
                zeros = ''
                for i in range(3 - len(current)):
                    zeros += '0'

                current = zeros + current
                data += current
            else:
                data += current

        data += '\n'
        return data.encode()

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, newIndex:int = 0) -> None:
        self.__index = newIndex
    
    @property
    def color(self) -> tuple:
        return self.__color

    @color.setter
    def color(self, newColor:tuple[int] = (0,0,0)) -> None:
        self.__color = newColor
