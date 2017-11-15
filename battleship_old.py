import random
import os

players = []

def cls():
        os.system('cls' if os.name=='nt' else 'clear')
cls()

def menu(players):
    print(" ╔════════════════════════════╗ ")
    print(" ║  Let's play Battleship!    ║ ")
    print(" ╚════════════════════════════╝ ")
    print('===============================')
    print('Hit marker: X')
    print('Miss marker: M\n')
    print('============MENU===============')
    print("Start""\n""Exit")
    print('===============================')
    option = input("Press 's' to start and 'x' to exit ")
    if option == "s":
        print()
        number_players = int(input("How many players will be? "))
       # players = []
        i = 0
        while i < number_players:
            player_name = input("What's your name? ")
            players.append(player_name)
            i += 1
    elif option == "x":
        exit() 
    cls()      
    return players       


def print_board(table):
    board = table
    print("         ╔════════════════════════════╗ ")
    print("         ║ Battleship has a size of 5 ║ ")
    print("         ║ Destroyer has a size of 4  ║ ")
    print("         ║ Submarine has a size of 3  ║ ")
    print("         ╚════════════════════════════╝ ")

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
        user_input = input("vertical or horizontal (v,h) ? ")
        if user_input == "v" or user_input == "h":
            return user_input
        else:
            print ("Invalid input. Please only enter v or h")


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
        user_input = input("Please enter coordinates (row,col) ? ")
        coor = list(user_input)
        
        if len(coor) != 2:
            print("Invalid entry, too few/many coordinates.")
            continue
        letter = user_input[0]
        characters = ('a', 'A', 'b', 'B','c', 'C','d', 'D','e', 'E','f', 'F','g', 'G','h', 'H')
        if letter not in characters:
            print("Invalid letter")
            continue
        x = convert(letter)
        y = user_input[1]
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8')
        if y not in numbers:
            print('Invalid value')
            continue
            
        mix = str(x) + ',' + str(y)
        coor = mix.split(",")
        coor[0] = int(coor[0])-1
        coor[1] = int(coor[1])-1
        
        return coor


def validate(board, ships, ship, ori, x, y):
    # validate the ship can be placed at given coordinates
    if ori == "v" and x + ships.get(ship) > 7:
        return False
    elif ori == "h" and y + ships.get(ship) > 7:
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
            print(str(which_player(players)) + " place a ", ship)
            x,y = get_coor()
            ori= v_or_h()
            valid = validate(board,ships, ship, ori, x, y)
            if valid == True:
                board = place_ship(board, ships[ship], ori, x, y)
            else:
                print("Invalid placement, try again")
                continue
            cls()
    return board


def place_ship(board, ship, ori, x, y):
    for i in range(ship):
        if ori is 'v':
            board[x+i][y] = 'O'
        else:
            board[x][y+i] = 'O' 
    return board     

'''
print("")
print("     Let's play Battleship!\n")
print("You have to place two ships on the board ")
print("one with size 3 and one with size 2")
print('Hit marker: X')
print('Miss marker: M\n')


print('===========================')
player_1 = input("Player One enter your name: ")
player_2 = input("Player Two enter your name: ")
cls()'''

def which_player(players):
    for player in players:
        return player

def draw():
    print('===========================\n')
    for i in range(1,2):
        sorszam = (random.randrange(2) + 1)
        if sorszam == 1:
            print(player_1 + ' will start the game!')
        else:
            temp=player_1
            player_1=player_2
            player_2=temp
            print(player_1+' will start the game!')


def main(players):
    ships = {"Battleship": 5, "Destroyer": 4, "Submarine": 3}
    board = []
    for i in range(8):
        board_row = []
        for j in range(8):
            board_row.append(' ')
        board.append(board_row)
    
    
    
    while True:
        
        menu(players)
        placement(board, ships, players)
        
        break
    

if __name__=="__main__":
    	main(players)
