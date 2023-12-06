# X for placing ships and hit battleships.
# ' ' for empty space.
# '-' for hitting the ship.


from random import randint

# Board for holding ship locations
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def print_board(board):
    print("  A B C D E F G H")
    print(' =====================')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for _ in range(5):  # Fixed syntax error in the loop definition
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input("Guess Row: 1-8 ")
    while row not in '12345678':
        print("Invalid input. Try again.")
        row = input("Guess Row: 1-8 ")

    column = input("Guess Column: A-H ").lower()  # Fixed to convert column input to lowercase
    while column not in 'abcdefgh':
        print("Invalid input. Try again.")
        column = input("Guess Column: A-H ").lower()

    return int(row) - 1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to my battleship game!')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You guessed that one already.")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("Good One! that is a Hit!")
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print("Sorry, that's a miss.")
        GUESS_BOARD[row][column] = '-'
        turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left.")  # Fixed the quotes and added space
        if turns == 0:
            print("Game Over")
            print("The ships were here:")
            print_board(HIDDEN_BOARD)
