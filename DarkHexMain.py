import DarkHexServer
import DarkHexHumanPlayer
import DarkHexRandomPlayer
import DarkHexSimulationPlayer
import DarkHexMohexPlayer

#Human Vs Random, hide Random Player's moves
#server = DarkHexServer.DarkHexServer(black=DarkHexHumanPlayer.DarkHexHumanPlayer(0, 3, 4), white=DarkHexRandomPlayer.DarkHexRandomPlayer(1, 3, 4), timelimit=60, timeEnforced=0)

#Random Vs Random, print true board state to terminal
#server = DarkHexServer.DarkHexServer(black=DarkHexRandomPlayer.DarkHexRandomPlayer(0, 3, 4), white=DarkHexRandomPlayer.DarkHexRandomPlayer(1, 3, 4), timeEnforced=1, debug=2)

#Random Vs Mohex, print true board state to terminal
#server = DarkHexServer.DarkHexServer(black=DarkHexRandomPlayer.DarkHexRandomPlayer(0, 3, 4), white=DarkHexMohexPlayer.DarkHexMohexPlayer("1", 3, 4, "~/Documents/GitHub/benzene-vanilla-cmake/build/src/mohex/mohex"), timeEnforced=1, debug=2)

#Human Vs Mohex, hide Mohex's moves
#server = DarkHexServer.DarkHexServer(black=DarkHexHumanPlayer.DarkHexHumanPlayer(0, 3, 4), white=DarkHexMohexPlayer.DarkHexMohexPlayer(1, 3, 4, "~/Documents/GitHub/benzene-vanilla-cmake/build/src/mohex/mohex"), timeEnforced=0, debug=0)

#Human Vs Mohex, larger board
#server = DarkHexServer.DarkHexServer(black=DarkHexHumanPlayer.DarkHexHumanPlayer(0, 7, 7), white=DarkHexMohexPlayer.DarkHexMohexPlayer("1", 7, 7, "~/Documents/GitHub/benzene-vanilla-cmake/build/src/mohex/mohex"), startPlayer=0, timeEnforced=0, debug=0, rows=7, columns=7)

#Random Vs Simulation, print true board state to terminal
#server = DarkHexServer.DarkHexServer(black=DarkHexRandomPlayer.DarkHexRandomPlayer(0, 3, 4), white=DarkHexSimulationPlayer.DarkHexSimulationPlayer(1, 3, 4, 100), timeEnforced=1, debug=2)

#Mohex Vs Simulation, print true board state to terminal
#server = DarkHexServer.DarkHexServer(black=DarkHexMohexPlayer.DarkHexMohexPlayer(0, 3, 4, "~/Documents/GitHub/benzene-vanilla-cmake/build/src/mohex/mohex"), white=DarkHexSimulationPlayer.DarkHexSimulationPlayer(1, 3, 4, 100), timeEnforced=1, debug=2)

#Human Vs Simulation, hide Simulation Player's move
#server = DarkHexServer.DarkHexServer(3, 4, DarkHexHumanPlayer.DarkHexHumanPlayer(0, 3, 4), DarkHexSimulationPlayer.DarkHexSimulationPlayer(1, 3, 4, 1000), 1, 100, 2, 0, 0)

manual = False

if not manual:
    while True:
        try:
            numGames = int(input("How many games would you like played? "))
            break
        except:
            print("Invalid number of games")

    while True:
        try:
            rows, columns = map(int, input("What are the dimensions of the board? ").split())
            break
        except:
            print("Invalid board dimensions")

    while True:
        try:
            startingPlayer = int(input("Who starts?\n1) Black\n2) White\n? "))
            if startingPlayer > 0 and startingPlayer < 3:
                startingPlayer -= 1
                break
            else:
                print("invalid setting")
        except:
            print("invalid setting")

    while True:
        player1 = input("Who would you like the first player to be?\n1) Human Player\n2) Random Player\n3) Simulation Player\n4) Mohex Player\n? ")
        if player1 == "1":
            player1 = DarkHexHumanPlayer.DarkHexHumanPlayer(0, rows, columns)
            break
        elif player1 == "2":
            player1 = DarkHexRandomPlayer.DarkHexRandomPlayer(0, rows, columns)
            break
        elif player1 == "3":
            try:
                simulations = int(input("How many simulations should the simulation player do for each possible move? "))
                player1 = DarkHexSimulationPlayer.DarkHexSimulationPlayer(0, rows, columns, simulations)
                break
            except:
                print("Invalid simulation number")
        elif player1 == "4":
            try:
                player1 = DarkHexMohexPlayer.DarkHexMohexPlayer(0, rows, columns, input("Mohex executable location? "))
                break
            except:
                print("Mohex failed to launch")
        else:
            print("Unknown Player")

    while True:
        player2 = input("Who would you like the second player to be?\n1) Human Player\n2) Random Player\n3) Simulation Player\n4) Mohex Player\n? ")
        if player2 == "1":
            player2 = DarkHexHumanPlayer.DarkHexHumanPlayer(0, rows, columns)
            break
        elif player2 == "2":
            player2 = DarkHexRandomPlayer.DarkHexRandomPlayer(0, rows, columns)
            break
        elif player2 == "3":
            try:
                simulations = int(input("How many simulations should the simulation player do for each possible move? "))
                player2 = DarkHexSimulationPlayer.DarkHexSimulationPlayer(0, rows, columns, simulations)
                break
            except:
                print("Invalid simulation number")
        elif player2 == "4":
            try:
                player2 = DarkHexMohexPlayer.DarkHexMohexPlayer(0, rows, columns, input("Mohex executable location? "))
                break
            except:
                print("Mohex failed to launch")
        else:
            print("Unknown Player")

    while True:
        try:
            timeSetting = int(input("Time Style?\n1) Don't reset timer\n2) Reset timer after each valid move\n3) Reset Timer after each attempted move\n? "))
            if timeSetting > 0 and timeSetting < 4:
                timeSetting -= 1
                break
            else:
                print("Invalid time setting")
        except:
            print("Invalid time setting")

    while True:
        try:
            timelimit = float(input("How much time? (in seconds)"))
            break
        except:
            print("Not a number")

    while True:
        try:
            enforceTime = int(input("Enforce Timer?\n1) Don't enforce timer\n2) Going over time results in a loss\n? "))
            if enforceTime > 0 and enforceTime < 3:
                enforceTime -= 1
                break
            else:
                print("Invalid time setting")
        except:
            print("Invalid time setting")

    while True:
        try:
            debug = int(input("Print out absolute information?\n1) No information\n2) Just status messages\n3) Print board\n? "))
            if debug > 0 and debug < 4:
                debug -= 1
                break
            else:
                print("Invalid setting")
        except:
            print("Invalid setting")

    logfile = input("Log Games? (Specify filepath or leave blank for no log files) ")
    if logfile == "":
        logfile = None

    player1Wins = 0
    player2Wins = 0
    for x in range(numGames):
        if logfile != None:
            currentLog = logfile + str(x)
        else:
            currentLog = None
        if x % 2 == 1:
            status, winner = DarkHexServer.DarkHexServer(rows=rows, columns=columns, startPlayer=startingPlayer, timelimit=timelimit, timeStyle=timeSetting, timeEnforced=enforceTime, debug=debug, logfile=currentLog, black=player1, white=player2).play()
            print(status)
            if winner == 0:
                player1Wins += 1
            else:
                player2Wins += 1
        else:
            status, winner = DarkHexServer.DarkHexServer(rows=rows, columns=columns, startPlayer=startingPlayer, timelimit=timelimit, timeStyle=timeSetting, timeEnforced=enforceTime, debug=debug, logfile=currentLog, white=player1, black=player2).play()
            print(status)
            if winner == 0:
                player2Wins += 1
            else:
                player1Wins += 1

    print("Player 1 Wins:", player1Wins, "Player 2 Wins:", player2Wins)

else:
    print(server.play())
