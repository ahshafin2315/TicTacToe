import os
from time import sleep
import numpy as np
from typing import Tuple, Optional, Union

# Constants
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1
BOARD_SIZE = 3

# Display constants
GAME_TITLE = "========== TIC TAC TOE =========="
MENU_BAR = "------------------------------"
MENU_OPTIONS = """
1. Start Game
2. Exit
"""

def clear() -> None:
    os.system('cls' if os.name == "nt" else 'clear')

def main_menu() -> None:
    print(GAME_TITLE)
    print(MENU_BAR)
    print(MENU_OPTIONS)

    global game_start, counter
    while True:
        try:
            selection = int(input("Select (1/2): "))
            if selection == 1:
                game_start = True
                counter = 0
                clear()
                run_game()
                break
            elif selection == 2:
                game_start = False
                counter = 9
                clear()
                break
            raise ValueError
        except (ValueError, EOFError):
            clear()
            print(GAME_TITLE)
            print("Selection input ERROR: Please try again!")
            print(MENU_BAR)
            print(MENU_OPTIONS)

def print_board(board: np.ndarray) -> None:
    clear()
    symbols = {EMPTY: ' ', PLAYER_X: 'X', PLAYER_O: 'O'}
    print("\n  1 | 2 | 3 ")
    print(" ---+---+---")
    print("  4 | 5 | 6 ")
    print(" ---+---+---")
    print("  7 | 8 | 9 \n")
    
    for i in range(BOARD_SIZE):
        print(f" {symbols[board[i][0]]} | {symbols[board[i][1]]} | {symbols[board[i][2]]} ")
        if i != 2:
            print("---+---+---")
    print()

def check_winner(board: np.ndarray, last_move: Tuple[int, int], player: int) -> bool:
    # Check row
    if np.all(board[last_move[0]] == player):
        return True
    # Check column
    if np.all(board[:, last_move[1]] == player):
        return True
    # Check diagonals
    if last_move[0] == last_move[1] and np.all(np.diag(board) == player):
        return True
    if last_move[0] + last_move[1] == 2 and np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def place_move(board: np.ndarray, pos: int, player: int) -> Tuple[bool, Optional[str]]:
    row, col = (pos-1) // 3, (pos-1) % 3
    if board[row][col] == EMPTY:
        board[row][col] = player
        return check_winner(board, (row, col), player), None
    return False, "Position already taken!"

def get_player_input(player_name: str, symbol: str) -> int:
    while True:
        try:
            pos = int(input(f"{player_name} ({symbol}), enter position (1-9): "))
            if 1 <= pos <= 9:
                return pos
            print("Invalid position! Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def run_game() -> None:
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    players = [
        {"name": input("Enter Player 1 name: "), "symbol": 'X', "value": PLAYER_X},
        {"name": input("Enter Player 2 name: "), "symbol": 'O', "value": PLAYER_O}
    ]
    
    current_player = 0
    moves = 0
    
    while moves < 9:
        print_board(board)
        player = players[current_player]
        pos = get_player_input(player["name"], player["symbol"])
        
        won, error = place_move(board, pos, player["value"])
        if error:
            print(error)
            continue
            
        moves += 1
        if won:
            print_board(board)
            print(f"\n{player['name']} wins!")
            break
        
        current_player = (current_player + 1) % 2
        
    if moves == 9 and not won:
        print_board(board)
        print("\nGame Draw!")
    
    if input("\nPlay again? (y/n): ").lower().startswith('y'):
        clear()
        run_game()
    else:
        clear()
        main_menu()

if __name__ == "__main__":
    game_start = False
    counter = 0
    clear()
    main_menu()