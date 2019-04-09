import random
import DarkHexUtilities

class DarkHexSimulationPlayer(object):
    """
    Simulation player for dark hex
    """
    def __init__(self, colour, rows, columns, simulations):
        self.colour = colour
        self.rows = rows
        self.columns = columns
        self.board = [0]*(self.rows * self.columns)
        self.pieces = [0]*(self.rows * self.columns)
        self.simulations = simulations
        self.blackPieces = [0]*(self.rows * self.columns)
        self.whitePieces = [0]*(self.rows * self.columns)

    def index(self, row, column):
        """
        Quick index math
        """
        return (row * self.columns) + column

    def genmove(self, board, unknownPieces, time, status):
        moves = []
        for cell in range(len(board)):
            if board[cell] == 0:
                moves.append(cell)

        wins = [0] * len(moves)
        for move in range(len(moves)):
            for i in range(self.simulations):
                simulationBoard = board.copy()
                simulationMoves = moves.copy()
                simulationBoard[moves[move]] = 1 if self.colour == 0 else 2
                simulationMoves.remove(moves[move])
                wins[move] += self.simulate(simulationBoard, simulationMoves, unknownPieces)

        bestMove = None
        bestWins = -1
        for move in range(len(moves)):
            if wins[move] > bestWins:
                bestWins = wins[move]
                bestMove = moves[move]

        return bestMove // self.columns, bestMove % self.columns
        
    def simulate(self, board, moves, unknownPieces):
        for cell in range(len(board)):
            self.blackPieces[cell] = 0
            self.whitePieces[cell] = 0
            if board[cell] == 1:
                self.blackPieces[cell] = 1
            elif board[cell] == 2:
                self.whitePieces[cell] = 1

        for i in range(unknownPieces):
            move = random.choice(moves)
            moves.remove(move)
            if self.colour == 0:
                self.whitePieces[move] = 1
            elif self.colour == 1:
                self.blackPieces[move] = 1

        currentPlayer = 0 if self.colour == 1 else 1
        while len(moves) > 0:
            move = random.choice(moves)
            moves.remove(move)
            if currentPlayer == 0:
                self.blackPieces[move] = 1
            elif currentPlayer == 1:
                self.whitePieces[move] = 1
            currentPlayer = 1 if currentPlayer == 0 else 0

        if self.colour == 0:
            return 1 if self.checkBlackWin() else 0
        elif self.colour == 1:
            return 1 if self.checkWhiteWin() else 0

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

    def generateBoard(self):
        board = [0]*(self.rows * self.columns)
        for i in range(self.rows * self.columns):
            if self.blackPieces[i] == 1:
                board[i] = 1
            elif self.whitePieces[i] == 1:
                board[i] = 2
        return board

