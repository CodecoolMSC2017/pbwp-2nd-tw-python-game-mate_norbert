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
    table1 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table2 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table3 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table4 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table5 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table6 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table7 = [" ", " ", " ", " ", " ", " ", " ", " "]
    table8 = [" ", " ", " ", " ", " ", " ", " ", " "]
    print("    A   B   C   D   E   F   G   H")
    print("  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    print("1 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table1[0], table1[1], table1[2],table1[3], table1[4], table1[5],table1[6], table1[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("2 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table2[0], table2[1], table2[2],table2[3], table2[4], table2[5],table2[6], table2[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("3 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table3[0], table3[1], table3[2],table3[3], table3[4], table3[5],table3[6], table3[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("4 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table4[0], table4[1], table4[2],table4[3], table4[4], table4[5],table4[6], table4[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("5 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table5[0], table5[1], table5[2],table5[3], table5[4], table5[5],table5[6], table5[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("6 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table6[0], table6[1], table6[2],table6[3], table6[4], table6[5],table6[6], table6[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("7 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table7[0], table7[1], table7[2],table7[3], table7[4], table7[5],table7[6], table7[7]))
    print("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("8 ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║ %s ║" % (table8[0], table8[1], table8[2],table8[3], table8[4], table8[5],table8[6], table8[7]))
    print("  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")


def placement(): #  placement of the ships
    pass


def v_or_h(): #  vertical or horizontal placement
    while(True):
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