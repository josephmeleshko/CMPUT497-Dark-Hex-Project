import io, subprocess

letters = "abcdefghijklmnopqrstuvwxyz"

class DarkHexMohexPlayer(object):
    """
    A player for dark hex that queries mohex for a conventional move

    Largely based on the program class from benzene-vanilla-cmake (but updated to Python3)
    """
    def __init__(self, colour, rows, columns, command):
        self.colour = colour
        self.rows = rows
        self.columns = columns
        self.mohex = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdin = self.mohex.stdin
        self.stdout = self.mohex.stdout
        self.stderr = self.mohex.stderr

        self.sendCommand("boardsize " + str(columns) + " " + str(rows))

    def sendCommand(self, command):
        command += "\n"
        self.stdin.write(command.encode())
        self.stdin.flush()
        answer = []
        while True:
            line = self.stdout.readline().decode("utf-8")
            if line == "\n":
                break
            if line[0] == "=":
                line = line [2:]
            answer.append(line[:-1])
        return answer

    def genmove(self, boardstate, hiddenCount, timelimit, status):
        self.sendCommand("clear_board")
        self.sendCommand("timelimit " + str(timelimit - 1))
        for move in range(len(boardstate)):
            if boardstate[move] == 1:
                self.sendCommand("play b " + letters[move % self.columns] + str((move // self.columns) + 1))
            elif boardstate[move] == 2:
                self.sendCommand("play w " + letters[move % self.columns] + str((move // self.columns) + 1))
        move = self.sendCommand("genmove " + ("b" if self.colour == 0 else "w"))[0]
        return int(move[1:]) - 1, letters.index(move[0])
        
