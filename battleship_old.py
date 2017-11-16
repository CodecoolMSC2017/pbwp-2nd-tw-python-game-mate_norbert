import random
import os
import time

players = []

def cls():
        os.system('cls' if os.name=='nt' else 'clear')
cls()


def getchar():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def menu(players):
    print("                      ╔════════════════════════════╗ ")
    print("                      ║  Let's play Battleship!    ║ ")
    print("                      ╚════════════════════════════╝ ")
    print("                                   |__")
    print("                                   |\/")
    print("                                   ---")
    print("                                 / | [")
    print("                          !      | |||")
    print("                        _/|     _/|-++'")
    print("                    +  +--|    |--|--|_ |-")
    print("                 { /|__|  |/\__|  |--- |||__/")
    print("                +---------------___[}-_===_.'____                 /\ ")
    print("            ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _")
    print(" __..._____--==/___]_|__|_____________________________[___\==--____,------' ...7")
    print("|                                                                      BB-61  /")
    print(" \                                                                           /")
    print("  \_________________________________________________________________________|")
    print("                                                                             ")
    print('                      =========== MENU ==============')
    print("                                (s)Start              ")
    print("                                (x)Exit               ")
    print('                      ===============================')
    print("                    Press any key to start and 'x' to exit ")
    while True:
        c = getchar()
        if c == 'x':
            break
    
        print()
        number_players = number()
        i = 0
        while i < number_players:
            player_name = input("                       What's your name? ")
            players.append(player_name)
            i += 1
     
        cls()      
        return players       


def number():
    while True:
        n = input("                            Number of players: ")
        if n.isdigit():
            return int(n)
        else:
            print("Please enter a number ")


def print_board(table):
    board = table
    print("      ╔══════════════════════════════════╗ ")
    print("      ║ Battleship has a size of 4 tiles ║ ")
    print("      ║ Destroyer has a size of 3 tiles  ║ ")
    print("      ║ Cruiser has a size of 2 tiles    ║ ")
    print("      ║ Submarine has a size of 1 tile   ║ ")
    print("      ╚══════════════════════════════════╝ ")
    print("          1   2   3   4   5   6   7   8")
    print("        ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    print("      A ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[0][0], board[0][1], 
    board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      B ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[1][0], board[1][1], 
    board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      C ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[2][0], board[2][1],
     board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      D ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[3][0], board[3][1],
     board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      E ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[4][0], board[4][1],
     board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      F ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[5][0], board[5][1],
     board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      G ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[6][0], board[6][1],
     board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7]))
    print("        ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("      H ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[7][0], board[7][1],
     board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7]))
    print("        ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")


def v_or_h():
    
    #get ship orientation from user
    while(True):
        user_input = input("     Vertical or horizontal placement (v,h) ? ")
        if user_input == "v" or user_input == "h":
            return user_input
        else:
            print ("    Invalid input. Please only enter v or h")


def convert(x):
    if x in ['a', 'A']:
        return 1
    elif x in ['b', 'B']:
        return 2
    elif x in ['c', 'C']:
        return 3
    elif x in ['d', 'D']:
        return 4
    elif x in ['e', 'E']:
        return 5
    elif x in ['f', 'F']:
        return 6
    elif x in ['g', 'G']:
        return 7
    elif x in ['h', 'H']:
        return 8


def get_coor():
        
    while (True):
        user_input = input("     Please enter coordinates (row,col) ? ")
        coor = list(user_input)
        
        if len(coor) != 2:
            print("     Invalid entry, too few/many coordinates.")
            continue
        letter = user_input[0]
        characters = ('a', 'A', 'b', 'B','c', 'C','d', 'D','e', 'E','f', 'F','g', 'G','h', 'H')
        if letter not in characters:
            print("          Invalid letter")
            continue
        x = convert(letter)
        y = user_input[1]
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8')
        if y not in numbers:
            print('          Invalid value')
            continue
            
        mix = str(x) + ',' + str(y)
        coor = mix.split(",")
        coor[0] = int(coor[0])-1
        coor[1] = int(coor[1])-1
        
        return coor


def validate(board, ships, ship, ori, x, y):
    # validate the ship can be placed at given coordinates
    if ori == "v" and x + ships.get(ship) > 8:
        return False
    elif ori == "h" and y + ships.get(ship) > 8:
        return False
    else:
        if ori == "v":
            for i in range(ships.get(ship)):
                if board[x + i][y] != ' ':
                    return False
        elif ori == "h":
            for i in range(ships.get(ship)):
                if board[x][y + i] != ' ':
                    return False

    return True


def placement(board, ships, players): # ship placement
    cls()
    for ship in ships.keys():
        print_board(board)
        valid = False
        while(not valid):
            print("          " + str(which_player(players)) + " place a", ship)
            x,y = get_coor()
            ori= v_or_h()
            valid = validate(board,ships, ship, ori, x, y)
            if valid == True:
                board = place_ship(board, ships, ships[ship], ori, x, y)
            else:
                print("          Invalid placement, try again")
                continue
            cls()
    return board


def place_ship(board, ships, ship, ori, x, y):
    for i in range(ship):
        if ship == ships["Destroyer"]:
            if ori is 'v':
                board[x+i][y] = 'D'
            else:
                board[x][y+i] = 'D'
        elif ship == ships["Battleship"]:
            if ori is 'v':
                board[x+i][y] = 'B'
            else:
                board[x][y+i] = 'B'
        elif ship == ships["Cruiser"]:
            if ori is 'v':
                board[x+i][y] = 'C'
            else:
                board[x][y+i] = 'C'
        elif ship == ships["Submarine"]:
            if ori is 'v':
                board[x+i][y] = 'S'
            else:
                board[x][y+i] = 'S'                 
    return board     


def which_player(players):
    for player in players:
        return player


def draw(players):
    player_1 = players[0]
    player_2 = players[1]
    player_3 = players[2]
    player_4 = players[3]
    print('===========================\n')
    for i in range(4):
        sorszam = (random.randrange(4) + 1)
        if sorszam == 1:
            print(player_1 + ' will start the game!')
        elif sorszam == 2:
            print(player_2 + ' will start the game!')
        elif sorszam == 3:
            print(player_3 + ' will start the game!')
        elif sorszam == 4:
            print(player_4 + ' will start the game!')        


def fire(board, x, y):
    if board[x][y] == " ":
        return "MISS"
    elif board[x][y] == "X"  or board[x][y] == "#":
        return "TRY AGAIN"
    else:
        return "HIT"

def guessing(game, player):
    hit_counter = {"Battleship": 5, "Destroyer": 4, "Cruiser": 3, "Submarine": 2}
    print(player)
    x,y = get_coor()
    print(x)
    print(y)
    for key in game:
        if key == player:
            continue
        print(game.get(player))
        
    
    



def main(players):
    ships = {"Battleship": 5, "Destroyer": 4, "Cruiser": 3, "Submarine": 2}
    


    game = {}
    menu(players)
    count = 0
    for player in range(len(players)):
        board = []
        for i in range(8):
            board_row = []
            for j in range(8):
                board_row.append(' ')
            board.append(board_row)
        placement(board, ships, players[player])
        game.update({players[player] : board})
        count += 1    
        if count == 4:
            time.sleep(4)
        else:
            continue

    while True:    
        for player in range(len(players)):
             
            guessing(game, players[player])   
            cls()
        
    

if __name__=="__main__":
    main(players)
