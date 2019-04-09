import DarkHexUtilities

columnLetters = "abcdefghjklmnopqrstuvwxyz"

class DarkHexHumanPlayer(object):
    """
    Human interface for dark hex
    """
    def __init__(self, colour, rows, columns):
        self.colour = colour
        self.rows = rows
        self.columns = columns

    def genmove(self, board, unknownPieces, time, status):
        print(status)
        print(time, "Time Remaining")
        DarkHexUtilities.prettyBoard(board, self.rows, self.columns)
        move = input("Move? (x#)")
        return int(move[1:]) - 1, columnLetters.find(move[0].lower())
