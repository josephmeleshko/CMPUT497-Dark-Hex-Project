import random
class DarkHexRandomPlayer(object):
    """
    Random player for dark hex
    """
    def __init__(self, colour, rows, columns):
        self.colour = colour
        self.rows = rows
        self.columns = columns

    def genmove(self, board, unknownPieces, time, status):
        moves = list(enumerate(board))
        random.shuffle(moves)
        i = 0
        while True:
            if moves[i][1] == 0:
                return moves[i][0] // self.columns, moves[i][0] % self.columns
            else:
                i += 1
