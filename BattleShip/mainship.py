import random
 
# Create a 5x5 board initialized with '~' (water)
board_size = 5
board = [['~' for _ in range(board_size)] for _ in range(board_size)]
 
# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
 
# Place the battleship randomly on the board
ship_row = random.randint(0, board_size - 1)
ship_col = random.randint(0, board_size - 1)
 
# Set the number of turns
turns = 5
 
print("Welcome to Battleship!")
print(f"You have {turns} attempts to sink the ship.")
print_board(board)
 
# Main game loop
for turn in range(turns):
    print(f"\nTurn {turn + 1}")
 
    # Get user's guess for row and column
    guess_row = int(input("Guess Row (0-4): "))
    guess_col = int(input("Guess Column (0-4): "))
 
    # Check if the guess is out of bounds
    if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
        print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == 'X':
        print("You already guessed that.")
    elif guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = 'B'
        print_board(board)
        break
    else:
        print("You missed!")
        board[guess_row][guess_col] = 'X'
 
    print_board(board)
 
    if turn == turns - 1:
        print("Game Over! You've used all your turns.")
        print(f"The ship was at Row {ship_row}, Column {ship_col}.")
 