class DarkHexBoard(object):
    """
    Board with knowledge tracking for the host server
    """
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.blackPieces = [0]*(rows*columns)
        self.whitePieces = [0]*(rows*columns)
        self.blackInformation = [0]*(rows*columns)
        self.whiteInformation = [0]*(rows*columns)
        self.hiddenBlackPieces = 0
        self.hiddenWhitePieces = 0

    def index(self, row, column):
        """
        Quick index math
        """
        return (row * self.columns) + column

    def move(self, colour, row, column):
        """
        colour: Black = 0, White = 1
        row:
        column:

        return: 0 = Success
                1 = Out of bounds
                2 = Occupied (information not updated)
                3 = Occupied (information updated)
                4 = Unknown error
        """

        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return 1

        index = self.index(row, column)

        if self.blackPieces[index] == 1:
            if colour == 1:
                if self.whiteInformation[index] == 0:
                    self.whiteInformation[index] = 1
                    self.hiddenBlackPieces -= 1
                    return 3
            return 2
        elif self.whitePieces[index] == 1:
            if colour == 0:
                if self.blackInformation[index] == 0:
                    self.blackInformation[index] = 1
                    self.hiddenWhitePieces -= 1
                    return 3
            return 2

        if colour == 0:
            self.blackPieces[index] = 1
            self.blackInformation[index] = 1
            self.hiddenBlackPieces += 1
            return 0
        elif colour == 1:
            self.whitePieces[index] = 1
            self.whiteInformation[index] = 1
            self.hiddenWhitePieces += 1
            return 0

        return 4

    def generateBoard(self):
        """
        return: Array of the board, not hiding anything
        """
        board = [0]*(self.rows * self.columns)
        for i in range(self.rows * self.columns):
            if self.blackPieces[i] == 1:
                board[i] = 1
            elif self.whitePieces[i] == 1:
                board[i] = 2
        return board

    def generatePlayerBoard(self, colour):
        """
        colour: Black = 0, White = 1

        return: Array generated for the colour given (black = 1, white = 2)
        """
        playerBoard = [0]*(self.rows * self.columns)
        for i in range(self.rows * self.columns):
            if colour == 0 and self.blackInformation[i] == 0:
                continue
            elif colour == 1 and self.whiteInformation[i] == 0:
                continue
            if self.blackPieces[i] == 1:
                playerBoard[i] = 1
            elif self.whitePieces[i] == 1:
                playerBoard[i] = 2
        return playerBoard

    def checkBlackWin(self):
        markedCells = set()
        for column in range(self.columns):
            if self.blackPieces[self.index(0, column)]:
                markedCells.add((0, column))
        newCells = markedCells.copy()
        while len(newCells) > 0:
            neighbours = self.getNeighbours(newCells.pop())
            for cell in neighbours:
                if not self.blackPieces[self.index(cell[0], cell[1])]:
                    continue
                if cell[0] == self.rows - 1:
                    return True
                if cell not in markedCells:
                    newCells.add(cell)
                    markedCells.add(cell)
        return False

    def checkWhiteWin(self):
        markedCells = set()
        for row in range(self.rows):
            if self.whitePieces[self.index(row, 0)]:
                markedCells.add((row, 0))
        newCells = markedCells.copy()
        while len(newCells) > 0:
            neighbours = self.getNeighbours(newCells.pop())
            for cell in neighbours:
                if self.whitePieces[self.index(cell[0], cell[1])]:
                    if cell[1] == self.columns - 1:
                        return True
                    if cell not in markedCells:
                        newCells.add(cell)
                        markedCells.add(cell)
        return False

    def getNeighbours(self, cell):
        returnList = []
        if cell[0] > 0:
            returnList.append((cell[0] - 1, cell[1]))
        if cell[0] < self.rows - 1:
            returnList.append((cell[0] + 1, cell[1]))
        if cell[1] > 0:
            returnList.append((cell[0], cell[1] - 1))
        if cell[1] < self.columns - 1:
            returnList.append((cell[0], cell[1] + 1))
        if cell[0] > 0 and cell[1] < self.columns - 1:
            returnList.append((cell[0] - 1, cell[1] + 1))
        if cell[0] < self.rows - 1 and cell[1] > 0:
            returnList.append((cell[0] + 1, cell[1] - 1))
        return returnList

