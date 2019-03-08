import DarkHexBoard, DarkHexUtilities
import time

class DarkHexServer(object):
    """
    Sever to facilitate communication between two Dark Hex players
    rows: rows of board
    columns: columns of board
    black: black player, queries black.genmove(boardArray, time, informationString)
    white: white player, queries white.genmove(boardArray, time, informationString)
    startPlayer: first player to move (0, 1)
    timelimit: amount of time given for each move (not enforced)
    debug: 0 = no information, 1 = statusMessages, 2 = print board and status messages
    """
    def __init__(self, rows, columns, black, white, startPlayer, timelimit, debug):
        self.board = DarkHexBoard.DarkHexBoard(rows, columns)
        self.rows = rows
        self.columns = columns
        self.black = black
        self.white = white
        self.debug = debug
        self.currentPlayer = startPlayer
        self.timelimit = timelimit

    def play(self):
        """
        Play the game, query the players back and forth until somebody wins
        No enforcement of timelimit, but it tracks it
        """
        timeRemaining = self.timelimit
        statusMessage = "Start of Game"
        while True:
            if self.debug >= 2:
                DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
            if self.debug >= 1:
                print(statusMessage)
            if self.currentPlayer == 0:
                currentBoard = self.board.generatePlayerBoard(0)
                startTime = time.time()
                row, column = self.black.genmove(currentBoard, timeRemaining, statusMessage)
                timeRemaining -= time.time() - startTime
                if timeRemaining < 0:
                    pass
                result = self.board.move(0, row, column)
                if result == 0:
                    win = self.board.checkBlackWin()
                    if win:
                        DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
                        return "Black has won"
                    self.currentPlayer = 1
                    timeRemaining = self.timelimit
                    statusMessage = "Black has moved"
                    continue
                elif result == 1:
                    statusMessage = "Black returned out of bounds move"
                    continue
                elif result == 2:
                    statusMessage = "Black moved on top of their own pieces"
                    continue
                elif result == 3:
                    statusMessage = "Black discovered a white piece"
                    continue
                elif result == 4:
                    return "Error at play move " + str(self.currentPlayer) + " " + str(row) + " " + str(column)

            if self.currentPlayer == 1:
                currentBoard = self.board.generatePlayerBoard(1)
                startTime = time.time()
                row, column = self.white.genmove(currentBoard, timeRemaining, statusMessage)
                timeRemaining -= time.time() - startTime
                if timeRemaining < 0:
                    pass
                result = self.board.move(1, row, column)
                if result == 0:
                    win = self.board.checkWhiteWin()
                    if win:
                        DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
                        return "White has won"
                    self.currentPlayer = 0
                    timeRemaining = self.timelimit
                    statusMessage = "White has moved"
                    continue
                elif result == 1:
                    statusMessage = "White returned out of bounds move"
                    continue
                elif result == 2:
                    statusMessage = "White moved on top of their own pieces"
                    continue
                elif result == 3:
                    statusMessage = "White discovered a black piece"
                    continue
                elif result == 4:
                    return "Error at play move " + str(self.currentPlayer) + " " + str(row) + " " + str(column)
