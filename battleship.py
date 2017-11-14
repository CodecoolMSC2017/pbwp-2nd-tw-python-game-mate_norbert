import random, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def menu():
    print("Start""\n","Exit")
    print()
    option = input("Press 's' to start and 'x' to exit ")
    if option == "s":
        print()
        number_players = int(input("How many players will be?"))
        players = []
        i = 0
        while i < number_players:
            player_name = input("What's your name?")
            players.append(player_name)
            i += 1
    elif option == "x":
        exit()      

def print_board(): #  prints the board
    table = [[" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]]
    print("    1   2   3   4   5   6   7   8")
    print("  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    print("A ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[0][0], board[0][1], board[0][2],board[0][3], board[0][4], board[0][5],board[0][6], board[0][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("B ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[1][0], board[1][1], board[1][2],board[1][3], board[1][4], board[1][5],board[1][6], board[1][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("C ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[2][0], board[2][1], board[2][2],board[2][3], board[2][4], board[2][5],board[2][6], board[2][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("D ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[3][0], board[3][1], board[3][2],board[3][3], board[3][4], board[3][5],board[3][6], board[3][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("E ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[4][0], board[4][1], board[4][2],board[4][3], board[4][4], board[4][5],board[4][6], board[4][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("F ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[5][0], table6[1], table6[2],table6[3], table6[4], table6[5],table6[6], table6[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("G ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[6][0], board[6][1], board[6][2],board[6][3], board[6][4], board[6][5],board[6][6], board[6][7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("H ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (board[7][0], board[7][1], board[7][2],board[7][3], board[7][4], board[7][5],board[7][6], board[7][7]))
    print("  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")


def placement(): #  placement of the ships
    pass


def v_or_h(): #  vertical or horizontal placement
    while True:
        user_input = input("vertical or horizontal (v,h) ? ")
        if user_input == "v" or user_input == "h":
            return user_input
		else:
            print("Invalid input. Please only enter v or h")


def validate(): #  validate user ship placement( out of board, overplacement )
    if orientation == "v" and x+ship > 8:
		return False
	elif orientation == "h" and y+ship > 8:
		return False
	else:
		if ori == "v":
			for i in range(ship):
				if board[x+i][y] != -1:
					return False
		elif ori == "h":
			for i in range(ship):
				if board[x][y+i] != -1:
					return False
    return True            


def get_coor(): #  ask for coordinates
    pass


def move_check():
    pass


def check_sink():
    pass

    
def main():
    print_board()


if __name__ == '__main__':
    main()