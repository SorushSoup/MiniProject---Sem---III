import random

# Constants
BOARD_SIZE = 4  # The board will be 4x4

# Initialize the board
def initialize_board():
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]  # Create a 4x4 board filled with 0
    add_new_tile(board)  # Add a new tile with value 2 or 4
    add_new_tile(board)  # Add another tile
    return board

# Add a new tile to the board
def add_new_tile(board):
    empty_tiles = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == 0]
    if empty_tiles:  # If there are empty spaces
        r, c = random.choice(empty_tiles)  # Choose a random empty space
        board[r][c] = random.choice([2, 4])  # Place a 2 or 4 in the chosen space

# Display the board
def display_board(board):
    for row in board:  # For each row in the board
        print(" ".join(str(num).ljust(4) for num in row))  # Print each number with spaces

# Combine tiles in a row to the left
def combine_tiles(row):
    new_row = [num for num in row if num != 0]  # Remove all zeros
    for i in range(len(new_row) - 1):  # Combine numbers if they are the same
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [num for num in new_row if num != 0]  # Remove zeros again
    while len(new_row) < BOARD_SIZE:  # Add zeros at the end to make it the same length as the board
        new_row.append(0)
    return new_row

# Move tiles in the board
def move(board, direction):
    if direction == 'w':  # Up
        for c in range(BOARD_SIZE):
            col = [board[r][c] for r in range(BOARD_SIZE)]
            new_col = combine_tiles(col)
            for r in range(BOARD_SIZE):
                board[r][c] = new_col[r]
    elif direction == 's':  # Down
        for c in range(BOARD_SIZE):
            col = [board[r][c] for r in range(BOARD_SIZE)]
            new_col = combine_tiles(col[::-1])[::-1]
            for r in range(BOARD_SIZE):
                board[r][c] = new_col[r]
    elif direction == 'a':  # Left
        for r in range(BOARD_SIZE):
            board[r] = combine_tiles(board[r])
    elif direction == 'd':  # Right
        for r in range(BOARD_SIZE):
            board[r] = combine_tiles(board[r][::-1])[::-1]

# Check if the game is over
def is_game_over(board):
    for row in board:
        if 0 in row:  # Check if there are empty spaces
            return False
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE - 1):
            if board[r][c] == board[r][c + 1] or board[c][r] == board[c + 1][r]:  # Check for possible merges
                return False
    return True

# Main game loop
def game_loop():
    board = initialize_board()  # Start the game with a new board
    display_board(board)  # Display the initial board

    while True:
        move_direction = input("Enter move (WASD): ").lower()  # Ask for the move direction
        if move_direction in ['w', 'a', 's', 'd']:
            old_board = [row[:] for row in board]  # Copy the board before the move
            move(board, move_direction)  # Move the tiles in the chosen direction
            if board != old_board:  # If the board has changed
                add_new_tile(board)  # Add a new tile
                display_board(board)  # Show the updated board
                if is_game_over(board):  # Check if the game is over
                    print("Game Over!")
                    break
        else:
            print("Invalid move. Use W, A, S, or D.")

# Run the game
game_loop()