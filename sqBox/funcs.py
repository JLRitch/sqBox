def addSquares(squareX, squareY):
    '''Combines two squares together to create a new square.

    :param squareX Square: first square to be added
    :param squareY Square: second square to be added
    '''
    from .shapes import Square

    newWidth = squareX.sideY1.length + squareY.sideY1.length
    newHeight = squareX.sideX1.length + squareY.sideX1.length
    newColor = f'{squareX.color}ish {squareY.color}'

    return Square(newWidth, newHeight, newColor)