import random
import os

def cls():
    	os.system('cls' if os.name=='nt' else 'clear')
cls()

def print_board(table):
    board = table
    print(board)
    print("    1   2   3   4   5   6   7   8")
    print("  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    print("A ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("B ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("C ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("D ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("E ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("F ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("G ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("H ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7]))
    print("  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")

boardplacement_player_one= [
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0']
]
boardplacement_player_oneGuess= [
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0']
]
boardplayer_two= [
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0']
]
boardplayer_twoGuess= [
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0'],
['0','0','0','0','0']
]
shipSize_3 = []
shipSize_2 = []

def placement_player_one(): # ship placement
    board = []
    for i in range(8):
        board_row = []
        for j in range(8):
            board_row.append(' ')
        board.append(board_row)
    print('===========================')
    print(player_1 + ', place your ships\n')
    add1=input('Place your size 3 ship first (x,y): ')
    orientation=input('Set orientation (h, v): ')
    
    # converts coordinates to list indexes
    parts=add1.split(',')
    x = int(parts[0])
    y = int(parts[1])
    row = x - 1
    coloumn = y - 1
   
    # marking ships on the board with 2 and 3 to mark their size so
    # later we can calculate which ship is sunk
    for i in range(3):
        if orientation is 'v':
            board[row+i][coloumn] = '3'
        else:
            board[row][coloumn+i] = '3'
    
    return board
    
    
    
    
def player_two(): # ship placement
    print('===========================')
    print(player_2 + ', place your ships\n')
    board = []
    for i in range(8):
        board_row = []
        for j in range(8):
            board_row.append(' ')
        board.append(board_row)
    print('===========================')
    print(player_1 + ', place your ships\n')
    add1=input('Place your size 3 ship first (x,y): ')
    orientation=input('Set orientation (h, v): ')
    
    # converts coordinates to list indexes
    parts=add1.split(',')
    x = int(parts[0])
    y = int(parts[1])
    row = x - 1
    coloumn = y - 1
   
    # marking ships on the board with 2 and 3 to mark their size so
    # later we can calculate which ship is sunk
    for i in range(3):
        if orientation is 'v':
            board[row+i][coloumn] = '3'
        else:
            board[row][coloumn+i] = '3'
    
    return board
    
print("")
print("     Let's play Battleship!\n")
print("You have to place two ships on the board ")
print("one with size 3 and one with size 2")
print('Hit marker: X')
print('Miss marker: M\n')


print('===========================')
player_1 = input("Player One enter your name: ")
player_2 = input("Player Two enter your name: ")

# player draw
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


# MAIN
turn = 0
hitCount1=0
hitCount2=0
P1hitCount_Size2=0
P1hitCount_Size3=0
P2hitCount_Size2=0
P2hitCount_Size3=0

while True:
    print ('======================')
    print("It's your turn "+player_1)
    board = placement_player_one()
    print_board(board)
    print ('2/', P1hitCount_Size2)
    print ('3/',  P1hitCount_Size3)
    guess=input('Target coordinates: (x,y):')
    parts=guess.split(',')
    x = int(parts[0])
    y = int(parts[1])
    row = x - 1
    coloumn = y - 1
    P1ship2 = '2'
    P1ship3 = '3'
    if P1ship2 in boardplayer_two[row][coloumn]: # it searches for hits in the small ship first
        print ('+++++++  HIT +++++++')
        boardplacement_player_oneGuess[row][coloumn] = 'X' # it stores the 'Miss' value for visualizing later
        P1hitCount_Size2 +=1
    elif boardplayer_two[row][coloumn] == '0':
        print ('------ MISS ------')
        boardplacement_player_oneGuess[row][coloumn] = 'M'
    elif P1ship3 in boardplayer_two[row][coloumn]: # it searches for hits in the big ship
        print ('+++++++  HIT +++++++')
        boardplacement_player_oneGuess[row][coloumn] = 'X'
        P1hitCount_Size3 +=1
    elif boardplayer_two[row][coloumn] == '0':
        print ('------ MISS ------')
        boardplacement_player_oneGuess[row][coloumn] = 'M'

    if P1hitCount_Size2 + P1hitCount_Size3 == 5:
        print ('\n+++++ ' + player_1 + ' WINS +++++')
        break

    
    print("\nIt's your turn " +player_2)
    for x in boardplayer_twoGuess:
        print(*x)
    print ('2/', P2hitCount_Size2)
    print ('3/', P2hitCount_Size3)
    guess2=input('Target coordinates: (x,y):')
    parts2=guess2.split(',')
    x2 = int(parts2[0])
    y2 = int(parts2[1])
    row2 = x2 - 1
    coloumn2 = y2 - 1
    P2ship2 = '2'
    P2ship3 = '3'
    if P2ship2 in boardplacement_player_one[row2][coloumn2]:
        print ('+++++++  HIT +++++++')
        boardplayer_twoGuess[row2][coloumn2] = 'X'
        P2hitCount_Size2 +=1
    elif boardplacement_player_one[row2][coloumn2] == '0':
        print ('------ MISS ------')
        boardplayer_twoGuess[row2][coloumn2] = 'M'
    elif P2ship3 in boardplacement_player_one[row2][coloumn2]:
        print ('+++++++  HIT +++++++')
        boardplayer_twoGuess[row2][coloumn2] = 'X'
        P2hitCount_Size3 +=1
    elif boardplacement_player_one[row2][coloumn2] == '0':
        print ('------ MISS ------')
        boardplayer_twoGuess[row2][coloumn2] = 'M'
    
    if P2hitCount_Size2 + P2hitCount_Size3 == 5:
        print ('\n+++++++ ' + player_2 + ' WINS +++++++')
        
        break
