
class Side():
    '''A line of l length.

    :attr length int: represents the length of a side

    :param l in: becomes the length attribute of this Side
    '''
    def __init__(self, l):
        self.length = l
    
    def __str__(self):
        return f"This side's length is {self.length}"

    def __repr__(self):
        return f"This side's length is {self.length}"

class Square():
    '''A square consisting of 4 sides.

    :param width int: width of the shape
    :param height int: height of the shape
    :param color str: default='black' color of the shape

    :attr sideX1 int: left vertical wall length
    :attr sideX2 int: right vertical wall length
    :attr sideY1 int: top horizontal wall length
    :attr sideY1 int: bottom horizontal wall length
    :attr area int: area of the shape
    :attr color str: the color of the shape
    '''
    def __init__(self, width, height, color='black'):
        self.sideX1, self.sideX2 = Side(height), Side(height)
        self.sideY1, self.sideY2 = Side(width), Side(width)
        self.area = width * height
        self.color = color

    def __str__(self):
        outStr = (f"This square's height is {self.sideX1.length}\n" +
            f"This square's width is {self.sideY1.length}\n" +
            f"This square's area is {self.area}\n" +
            f"This square's color is {self.color}")
        return outStr

    def __repr__(self):
        outStr = (f"This square's height is {self.sideX1.length}\n" +
            f"This square's width is {self.sideY1.length}\n" +
            f"This square's area is {self.area}\n" +
            f"This square's color is {self.color}")
        return outStr

    def __add__(self, otherSquare):
            '''Combines two squares together to create a new square.

            :param otherSquare Square: second square to be added

            :return new Square: a new Square obj with combined attributes
            '''
            if type(otherSquare) == type(self):
                newWidth = self.sideY1.length + otherSquare.sideY1.length
                newHeight = self.sideX1.length + otherSquare.sideX1.length
                newColor = f'{self.color}ish {otherSquare.color}'

                return Square(newWidth, newHeight, newColor)
            else:
                raise TypeError('A square can only be added to another square.')
