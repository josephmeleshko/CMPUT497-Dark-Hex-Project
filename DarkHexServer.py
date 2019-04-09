import DarkHexBoard, DarkHexUtilities
import time

letters = "abcdefghijklmnopqrstuvwxyz"

class DarkHexServer(object):
    """
    Sever to facilitate communication between two Dark Hex players
    rows: rows of board
    columns: columns of board
    black: black player, queries black.genmove(boardArray, time, informationString)
    white: white player, queries white.genmove(boardArray, time, informationString)
    startPlayer: first player to move (0, 1)
    timelimit: amount of time given for each move (not enforced)
    timeStyle: 2 = reset timer after each attempted move, 1 = reset timer after each accepted move, 0 = don't reset timer
    timeEnforced: 0 = don't enforce time, 1 = kill players for going over time
    debug: 0 = no information, 1 = statusMessages, 2 = print board and status messages
    """
    def __init__(self, 
        rows=3,
        columns=4,
        black=None,
        white=None,
        startPlayer=1,
        timelimit=10,
        timeStyle=2,
        timeEnforced=1,
        debug=0,
        initialBlackPieces=[],
        initialWhitePieces=[],
        initialBlackInformation=[],
        initialWhiteInformation=[],
        logfile=None
        ):

        assert (black and white), "Missing Black Or White Player"
        self.black = black
        self.white = white

        self.board = DarkHexBoard.DarkHexBoard(rows, columns)
        self.rows = rows
        self.columns = columns

        for cell in initialBlackPieces:
            self.board.blackPieces[cell] = 1
        for cell in initialWhitePieces:
            self.board.whitePieces[cell] = 1
        for cell in initialBlackInformation:
            self.board.blackInformation[cell] = 1
        for cell in initialWhiteInformation:
            self.board.blackInformation[cell] = 1

        self.debug = debug
        self.currentPlayer = startPlayer
        self.timelimit = timelimit
        self.timeStyle = timeStyle
        self.timeEnforced = timeEnforced
        self.blackTime = self.timelimit
        self.whiteTime = self.timelimit
        self.logfile = open(logfile, "w")

    def play(self):
        """
        Play the game, query the players back and forth until somebody wins
        No enforcement of timelimit, but it tracks it
        """
        self.blackTime = self.timelimit
        self.whiteTime = self.timelimit
        statusMessage = "Start of Game"
        while True:
            if self.debug >= 2:
                DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
            if self.debug >= 1:
                print(statusMessage)
            if self.logfile != None:
                self.logfile.write(statusMessage + "\n")

            if self.currentPlayer == 0:
                currentBoard = self.board.generatePlayerBoard(0)
                startTime = time.time()
                row, column = self.black.genmove(currentBoard, self.board.hiddenWhitePieces, self.blackTime, statusMessage)
                self.blackTime -= time.time() - startTime
                if self.blackTime < 0 and self.timeEnforced == 1:
                    DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
                    if self.logfile != None:
                        self.logfile.write("Black has run out of time")
                        self.logfile.flush()
                        self.logfile.close()
                    return "Black has run out of time", 1

                result = self.board.move(0, row, column)
                if result == 0:
                    if self.logfile != None:
                        self.logfile.write("b " + letters[column] + str(row + 1) + "\n")
                    win = self.board.checkBlackWin()
                    if win:
                        DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
                        if self.logfile != None:
                            self.logfile.write("Black has won")
                            self.logfile.flush()
                            self.logfile.close()
                        return "Black has won", 0
                    self.currentPlayer = 1
                    if self.timeStyle > 0:
                        self.blackTime = self.timelimit
                    statusMessage = "Black has moved"
                    continue
                elif result == 1:
                    statusMessage = "Black returned out of bounds move"
                    continue
                elif result == 2:
                    statusMessage = "Black moved on top of a piece"
                    continue
                elif result == 3:
                    if self.timeStyle > 1:
                        self.blackTime = self.timelimit
                    statusMessage = "Black discovered a white piece"
                    continue
                elif result == 4:
                    return "Error at play move " + str(self.currentPlayer) + " " + str(row) + " " + str(column), -1

            if self.currentPlayer == 1:
                currentBoard = self.board.generatePlayerBoard(1)
                startTime = time.time()
                row, column = self.white.genmove(currentBoard, self.board.hiddenBlackPieces, self.whiteTime, statusMessage)
                self.whiteTime -= time.time() - startTime
                if self.whiteTime < 0 and self.timeEnforced == 1:
                    DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
                    if self.logfile != None:
                        self.logfile.write("White has run out of time")
                        self.logfile.flush()
                        self.logfile.close()
                    return "White has run out of time", 0

                result = self.board.move(1, row, column)
                if result == 0:
                    if self.logfile != None:
                        self.logfile.write("w " + letters[column] + str(row + 1) + "\n")
                    win = self.board.checkWhiteWin()
                    if win:
                        DarkHexUtilities.prettyBoard(self.board.generateBoard(), self.rows, self.columns)
                        if self.logfile != None:
                            self.logfile.write("White has won")
                            self.logfile.flush()
                            self.logfile.close()
                        return "White has won", 1
                    self.currentPlayer = 0
                    if self.timeStyle > 0:
                        self.whiteTime = self.timelimit
                    statusMessage = "White has moved"
                    continue
                elif result == 1:
                    statusMessage = "White returned out of bounds move"
                    continue
                elif result == 2:
                    statusMessage = "White moved on top of a piece"
                    continue
                elif result == 3:
                    if self.timeStyle > 1:
                        self.whiteTime = self.timelimit
                    statusMessage = "White discovered a black piece"
                    continue
                elif result == 4:
                    return "Error at play move " + str(self.currentPlayer) + " " + str(row) + " " + str(column), -1
