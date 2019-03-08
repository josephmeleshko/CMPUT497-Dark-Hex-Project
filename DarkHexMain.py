import DarkHexServer
import DarkHexHumanPlayer
import DarkHexRandomPlayer

#Human Vs Random, hide Random Player's moves
server = DarkHexServer.DarkHexServer(3, 4, DarkHexHumanPlayer.DarkHexHumanPlayer(0, 3, 4), DarkHexRandomPlayer.DarkHexRandomPlayer(1, 3, 4), 1, 100, 0)

#Random Vs Random, print true board state to terminal
#server = DarkHexServer.DarkHexServer(3, 4, DarkHexRandomPlayer.DarkHexRandomPlayer(0, 3, 4), DarkHexRandomPlayer.DarkHexRandomPlayer(1, 3, 4), 1, 100, 2)

print(server.play())
