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
                2 = Occupied by self
                3 = Occupied by opponent (information updated)
                4 = Unknown error
        """

        if row < 0 or row >= self.rows or column < 0 or column >= self.columns:
            return 1

        index = self.index(row, column)

        if self.blackPieces[index] == 1:
            if colour == 1:
                self.whiteInformation[index] = 1
                return 3
            else:
                return 2
        elif self.whitePieces[index] == 1:
            if colour == 0:
                self.blackInformation[index] = 1
                return 3
            else:
                return 2

        if colour == 0:
            self.blackPieces[index] = 1
            self.blackInformation[index] = 1
            return 0
        elif colour == 1:
            self.whitePieces[index] = 1
            self.whiteInformation[index] = 1
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
        """
        return: True if Black has won otherwise False
        """
        activeSet = set()
        for column in range(self.columns):
            if self.blackPieces[self.index(0, column)]:
                activeSet.add((0, column))
        while len(activeSet) > 0:
            cell = activeSet.pop()
            neighbours = self.getBlackNeighbours(cell)
            for n in neighbours:
                if n[0] + 1 == self.rows:
                    return True
                activeSet.add(n)
        return False

    def getBlackNeighbours(self, cell):
        """
        return: neighbours below and to the right
        """
        returnSet = []
        if cell[1] != 0:
            if self.blackPieces[self.index(cell[0] + 1, cell[1] - 1)] == 1:
                returnSet.append((cell[0] + 1, cell[1] - 1))
        if cell[1] + 1 != self.columns:
            if self.blackPieces[self.index(cell[0], cell[1] + 1)] == 1:
                returnSet.append((cell[0], cell[1] + 1))
        if self.blackPieces[self.index(cell[0] + 1, cell[1])] == 1:
            returnSet.append((cell[0]+1, cell[1]))
        return returnSet

    def checkWhiteWin(self):
        """
        return: True if White has won otherwise False
        """
        activeSet = set()
        for row in range(self.rows):
            if self.whitePieces[self.index(row, 0)]:
                activeSet.add((row, 0))
        while len(activeSet) > 0:
            cell = activeSet.pop()
            neighbours = self.getWhiteNeighbours(cell)
            for n in neighbours:
                if n[1] + 1 == self.columns:
                    return True
                activeSet.add(n)
        return False

    def getWhiteNeighbours(self, cell):
        """
        return: neighbours to the right and below
        """
        returnSet = []
        if cell[0] != 0:
            if self.whitePieces[self.index(cell[0] - 1, cell[1] + 1)] == 1:
                returnSet.append((cell[0] - 1, cell[1] + 1))
            if self.blackPieces[self.index(cell[0] - 1, cell[1])] == 1:
                returnSet.append((cell[0] - 1, cell[1]))
        if self.whitePieces[self.index(cell[0], cell[1] + 1)] == 1:
            returnSet.append((cell[0], cell[1] + 1))
        return returnSet
