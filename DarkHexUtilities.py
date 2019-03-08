columnLetters = "abcdefghjklmnopqrstuvwxyz"
pieces = [".", "B", "W"]

def prettyBoard(board, rows, columns):
    offset = " "
    print("   ", end="")
    for i in range(columns):
        print(columnLetters[i], end=" ")
    print()
    for i in range(rows):
        print(offset, end="")
        print(str(i+1) + "\\", end=" ")
        for j in range(columns):
            print(pieces[board[(columns * i) + j]], end=" ")
        print("\\" + str(i+1))
        offset = offset + " "
    print(offset, "  ", end="")
    for i in range(columns):
        print(columnLetters[i], end=" ")
    print()
