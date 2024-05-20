import os
from time import sleep


def clear():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')


def main_menu():
    long_ebar = "=============================="
    long_mbar = "----------------------------"
    l_space = "                            "
    s_space = "       "
    
    view_game_name = long_ebar + '\n|--------TICTACTOE !!!-------|\n|' + long_mbar + "|"
    view_options = "|" + l_space + '|\n|' + l_space + '|\n|' + s_space + '1. Start Game ' + s_space + '|\n|' + s_space + '2. Exit' + s_space + '       |\n|' + l_space + '|\n|' + l_space + '|\n ' + long_mbar
    print(view_game_name)
    print(view_options)

    global game_start, counter
    while True:
        try:
            selection = int(input("Select (1/2): "))
        except EOFError:
            clear()
            break
        else:
            if selection == 1:
                game_start = True
                counter = 0
                clear()
                runGame()
                break
            elif selection == 2:
                game_start = False
                counter = 9
                clear()
                break
            else:
                clear()
                print(view_game_name)
                print("Selection input ERROR: Please try again!")
                print(view_options)


def printBoard():
    clear()
    u_grid = ' ___ ___ ___'
    sp = '      '
    count = 1
    increament = 0
    print(f"\n{u_grid}{sp}Positions:")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            if board[i][j] == count:
                print(f"   |", end="")
            else:
                print(f" {board[i][j]} |", end="")
            if j == 2:
                print(f"{sp[:-1]}{increament+1} | {increament+2} | {increament+3}")
            count += 1
        increament += 3
        if i != 2:
            print(f"{u_grid}{sp}__ ___ __")
        else:
            print(f'{u_grid}\n')


# This function will be called from within the placeCharacter function. 
# r : In which row of the current character was placed
# c : In which column of the current character was placed
# char : Player chosen shape
# returned value: True if anyone has won; Otherwise False
def checkBoard(r, c, char):
    co_ords = {
        (0,0): (
            ((0,1),(0,2)),
            ((1,1),(2,2)),
            ((1,0),(2,0))
            ),# check for input: 1
        (0,1): (
            ((0,0),(0,2)),
            ((1,1),(2,1))
            ),# check for input: 2
        (0,2): (
            ((0,0),(0,1)),
            ((1,1),(2,0)),
            ((1,2),(2,2))
            ),# check for input: 3
        (1,0): (
            ((0,0),(2,0)),
            ((1,1),(1,2))
            ),# check for input: 4
        (1,1): (
            ((1,0),(1,2)),
            ((0,1),(2,1)),
            ((0,0),(2,2)),
            ((0,2),(2,0))
            ),# check for input: 5
        (1,2): (
            ((0,2),(2,2)),
            ((1,0),(1,1))
            ),# check for input: 6
        (2,0): (
            ((0,0),(1,0)),
            ((0,2),(1,1)),
            ((2,1),(2,2))
            ),# check for input: 7
        (2,1): (
            ((2,0),(2,2)),
            ((0,1),(1,1))
            ),# check for input: 8
        (2,2): (
            ((0,2),(1,2)),
            ((0,0),(1,1)),
            ((2,0),(2,1))
            ) # check for input: 9
    }
    matched = False
    coordinates = co_ords[(r, c)]
    for i in range(len(coordinates)):
        if board[coordinates[i][0][0]][coordinates[i][0][1]] == char and board[coordinates[i][1][0]][coordinates[i][1][1]] == char:
            matched = True
            break
    return matched


#Write the necessary code to put the "char" in proper position of the board and check if anyone has won.
#pos : The position that has been given by the player as input.
#char : The character representing the player. It can be X or O.
#count: It represents the number of turns. It can be from 0 to 8.
#returned value: True if anyone has won; Otherwise False
def placeCharacter(pos,char,count):
    global board
    placing_dict = {
        1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2)
    }
    i, j = placing_dict[pos]
    if board[i][j] == pos:
        board[i][j] = char
    else:
        clear()
        return "ATTENTION: Position already in use. Please select another one !!"
    if count > 3:
        checkBoard(i, j, char)
        match = checkBoard(i, j, char)
        if match is True:
            return True
        else:
            return False


def gameInitialization():
    global player1_name, player2_name, force_exit

    print("ATTENTION: Player1 will make first move.")
    try:
        while True:
            player1_name = input("\nEnter Player1's name: ").strip()
            if player1_name != '':
                break
            else:
                print('ERROR: Name can\'t be empty!')
        while True:
            player2_name = input("\nEnter Player2's name: ").strip()
            if player2_name != '':
                break
            else:
                print('ERROR: Name can\'t be empty!')
    except EOFError:
        force_exit = True


def shape_selection():
    global player1_shape, player2_shape, force_exit
    while True:
        try:
            shape_selection = input(f"\n{player1_name}, which shape do you choose?: ")
        except EOFError:
            force_exit = True
            break
        else:
            if shape_selection == 'x' or shape_selection == 'o':
                player1_shape = chr(ord(shape_selection)-32)
            elif shape_selection == '0':
                player1_shape = 'O'
            elif shape_selection == 'X'or shape_selection == 'O':
                player1_shape = shape_selection
            else:
                print('Invalid Shape Input: Please select again!')

            if player1_shape == "O":
                player2_shape = "X"
                print(f"\n{player1_name}'s chosen shape:", player1_shape)
                print(f"{player2_name}'s chosen shape:", player2_shape, "\n")
                sleep(1.5)
                clear()
                break
            elif player1_shape == "X":
                player2_shape = "O"
                print(f"\n{player1_name}'s chosen shape:", player1_shape)
                print(f"{player2_name}'s chosen shape:", player2_shape, "\n")
                sleep(1.5)
                clear()
                break


def restartGame():
    global counter, game_restart, force_exit
    try:
        restart = input('Restart game? (Y/N): ')
    except EOFError:
        counter = 9
        clear()
    else:
        if restart in 'yY' or restart == 'Yes' or restart == 'yes':
            counter = 0
            game_restart = True
            clear()
        else:
            counter = 9
            game_restart = False
            clear()
            main_menu()


def runGame():
    global board, counter, force_exit
    draw=False
    p_name=None
    while counter<9:
        if counter == 0 and game_restart is True:
            board = [[1,2,3],[4,5,6],[7,8,9]]
            change_players = input("Restart with different players? (Y/N):")
            if change_players in "Yy" or change_players == "yes" or change_players == "Yes":
                gameInitialization()
                if force_exit is False:
                    shape_selection()
                    if force_exit is True:
                        clear()
                        break
                else:
                    clear()
                    break
        elif counter == 0 and game_start is True:
            board = [[1,2,3],[4,5,6],[7,8,9]]
            gameInitialization()
            if force_exit is False:
                shape_selection()
                if force_exit is True:
                    clear()
                    break
            else:
                clear()
                break

        if counter%2==0:
            printBoard()
            while True:
                try:
                    player1_input = int(input(f"{player1_name}, where do you want to place '{player1_shape}': "))
                except ValueError:
                    print("Invalid Character. Please select again.")
                except EOFError:
                    force_exit = True
                    break
                else:
                    if not(0 < player1_input <= 9):
                        print("Error: Input Out-Of-Bound. Please select again.")
                    else:
                        state = placeCharacter(player1_input, player1_shape, counter)
                        if counter == 8 and state is False:
                            draw = True
                            break
                        elif state is True:
                            p_name = player1_name
                            break
                        elif state is False or state is None:
                            break
                        else:
                            printBoard()
                            print(f'\n{state}')
            if force_exit is False:
                printBoard()
            else:
                clear()
                break
        else:
            printBoard()
            while True:
                try:
                    player2_input = int(input(f"{player2_name}, where do you want to place '{player2_shape}': "))
                except ValueError:
                    print("Invalid Character. Please select again.")
                except EOFError:
                    force_exit = True
                    break
                else:
                    if not(0 < player2_input <= 9):
                        print("Error: Input Out-Of-Bound. Please select again.")
                    else:
                        state = placeCharacter(player2_input, player2_shape, counter)
                        if counter == 8 and state is False:
                            draw = True
                            break
                        elif state is True:
                            p_name = player2_name
                            break
                        elif state is False or state is None:
                            break
                        else:
                            printBoard()
                            print(f'\n{state}')
            if force_exit is False:
                printBoard()
            else:
                clear()
                break
        counter+=1
        if draw is True:
            print("The game ends in a draw.")
            restartGame()
        if state is True:
            print(f"{p_name} has won the game!!!!")
            restartGame()


board = [[1,2,3],[4,5,6],[7,8,9]]

force_exit = False
player1_name = player2_name = None
player1_shape = str()
player2_shape = str()

clear()

game_start = False
game_restart = False
counter = 0

main_menu()