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
    pass


def validate(): #  validate user ship placement( out of board, overplacement )
    pass


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