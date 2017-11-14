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

def print_board(): #  print the board
    pass    


def placement(): #  placement of the ships
    pass


def v_or_h(): #  vertical or horizontal placement
    while(True):
		user_input = input("vertical or horizontal (v,h) ? ")
		if user_input == "v" or user_input == "h":
			return user_input
		else:
			print "Invalid input. Please only enter v or h"



def validate(): #  validate user ship placement( out of board, overplacement )
    if orientation == "v" and x+ship > 10:
		return False
	elif orientation == "h" and y+ship > 10:
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
    pass


if __name__ == '__main__':
    main()