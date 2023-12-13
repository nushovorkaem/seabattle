#game one
import random

respond = None
game_over = False

def GenEnemies(board_size):
    return random.randint(1, board_size), random.randint(1, board_size)  # x and y place of ship

def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
        print('-' * (5 * len(row) - 1) + '--')

def take_user_input():
    return int(input(f"Provide row number (1-{board_size}): ")), int(input(f"Provide column number (1-{board_size}): "))

def check_guess(board, enemies, guess_row, guess_col):
    if (guess_col, guess_row) in enemies:
        print('BullsEye!')
        board[guess_row-1][guess_col-1] = ' X '
        enemies.remove((guess_col, guess_row))
        if not enemies:
            print_board(board)
            return 'Congratulations! You\'ve sunk all the enemy ships and won the game!'
    else:
        if (guess_row < 1 or guess_row > board_size) or (guess_col < 1 or guess_col > board_size):
            return "Don't shoot out of the board!"
        elif board[guess_row-1][guess_col-1] == " O ":
            return "You already shot there!"
        else:
            print("Missed!")
            board[guess_row-1][guess_col-1] = " O "

    return None

print('Hi and welcome to the game!')
board_size = int(input('How big board do you want? (NxN size type)\n'))
num_ships = int(input('How many enemies do you want to have?\n'))
amount_of_attempts = int(input('How many tries do you want to have?\n'))

print(f'\n\n\nYou have {amount_of_attempts} tries to sink the enemy fleet where there are {num_ships} ships!\nGood Luck!')

# Initializing board
board = [['    '] * board_size for _ in range(board_size)]

# Creating enemies
enemies = [GenEnemies(board_size) for _ in range(num_ships)]

while not game_over:
    for _ in range(amount_of_attempts):
        print_board(board)
        guess_row, guess_col = take_user_input()
        respond = check_guess(board, enemies, guess_row, guess_col)

        if respond:
            print(respond)
            game_over = True  # Set game_over flag to True when the player wins
            break  # Break out of the loop after a successful guess

    if game_over:
        print('Game Over!')
    elif amount_of_attempts - 1 == 0:
        print("You are out of ammo. End of the game, loser.")
        break 
#seabattle game
#hope it work
