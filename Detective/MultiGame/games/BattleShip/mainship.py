import tkinter as tk
from tkinter import messagebox
import random

# Initialize the board size and number of ships
board_size = 7  # Increased board size
ship_lengths = [2, 3, 4]  # Possible lengths of ships
num_ships = 5  # Increased number of ships

# Global variables
board = []
ships = []
turns_left = 0
score = 0

# Function to create the game board
def create_board():
    return [['~' for _ in range(board_size)] for _ in range(board_size)]

# Function to place ships randomly on the board
def place_ships():
    global board  # Declare board as a global variable
    ships = []
    for _ in range(num_ships):
        while True:
            length = random.choice(ship_lengths)  # Randomly choose a ship length
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, board_size - 1)
                col = random.randint(0, board_size - length)
                if all(board[row][col + i] == '~' for i in range(length)):  # Check if space is clear
                    for i in range(length):
                        board[row][col + i] = 'S'
                    ships.append((row, col, orientation, length))
                    break
            else:  # vertical
                row = random.randint(0, board_size - length)
                col = random.randint(0, board_size - 1)
                if all(board[row + i][col] == '~' for i in range(length)):  # Check if space is clear
                    for i in range(length):
                        board[row + i][col] = 'S'
                    ships.append((row, col, orientation, length))
                    break
    return ships

# Function to update the GUI board display
def update_board_gui():
    global board  # Declare board as a global variable
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == '~' or board[i][j] == 'S':
                board_label[i][j].config(text="🌊", state="normal", bg="#99d9ea", fg="blue", relief="raised")  # Water (not revealed)
            elif board[i][j] == 'X':
                board_label[i][j].config(text="❌", bg="#ff4d4d", fg="white", relief="sunken")  # Miss (X)
            elif board[i][j] == 'B':
                board_label[i][j].config(text="🚢", bg="#4caf50", fg="white", relief="sunken")  # Hit (Ship)

# Function to handle the player's guess
def make_guess(row, col):
    global board, ships, turns_left, score  # Declare these as globals
    if board[row][col] == 'X' or board[row][col] == 'B':
        result_label.config(text="You've already guessed that spot!", fg="orange")
        return

    if board[row][col] == 'S':
        board[row][col] = 'B'  # Hit
        result_label.config(text="Direct hit! You've found a ship!", fg="green")
        score += 10
        turns_left += 1  # Grant an extra turn for a hit
    else:
        board[row][col] = 'X'  # Miss
        result_label.config(text="You missed! -1 turn.", fg="red")
        score -= 1
        turns_left -= 1  # Lose a turn for a miss

    update_board_gui()
    turns_label.config(text=f"Turns left: {turns_left}")
    score_label.config(text=f"Score: {score}")

    if turns_left == 0 or all(board[r][c] == 'B' for r, c, _, _ in ships):
        end_game()

# Function to start the game from the main menu
def start_game():
    global board, ships, turns_left, score  # Declare as global
    turns_left = 10  # Reduced number of turns to increase difficulty
    score = 0
    result_label.config(text="Game Started! Hunt down the ships!", fg="blue")
    turns_label.config(text=f"Turns left: {turns_left}")
    score_label.config(text=f"Score: {score}")

    # Place ships randomly and reset the board
    board = create_board()
    ships = place_ships()
    update_board_gui()

    # Show the game screen
    main_menu_frame.pack_forget()
    game_frame.pack()

# Function to end the game and display the results
def end_game():
    if score > 0:
        messagebox.showinfo("Game Over", f"You sunk all the ships! Your score: {score}")
    else:
        messagebox.showinfo("Game Over", f"You ran out of turns! Your score: {score}")
    reset_game()

# Function to reset the game state
def reset_game():
    global board, ships, turns_left, score
    board = create_board()
    ships = []
    turns_left = 10
    score = 0
    main_menu_frame.pack()  # Return to the main menu
    game_frame.pack_forget()  # Hide the game frame

# Create the main Tkinter window
root = tk.Tk()
root.title("Battleship Game")
root.configure(bg="#add8e6")  # Light blue background

# Main menu frame
main_menu_frame = tk.Frame(root, bg="#add8e6")
main_menu_frame.pack(expand=True)  # Center the frame

# Title label
title_label = tk.Label(main_menu_frame, text="🏴‍☠️ Battleship Game 🏴‍☠️", bg="#add8e6", font=('Helvetica', 24, 'bold'), fg="#333")
title_label.pack(pady=20)

# Start button
start_button = tk.Button(main_menu_frame, text="Start Game", command=start_game, font=('Helvetica', 16), bg="#90ee90", fg="black", padx=20, pady=10)
start_button.pack(pady=20)

# Game frame
game_frame = tk.Frame(root, bg="#add8e6")

# Create a label grid for the game board
board_label = [[None for _ in range(board_size)] for _ in range(board_size)]
for i in range(board_size):
    for j in range(board_size):
        button = tk.Button(game_frame, text="🌊", width=4, height=2,
                           command=lambda row=i, col=j: make_guess(row, col), font=('Helvetica', 16), bg="#99d9ea")
        button.grid(row=i, column=j, padx=5, pady=5)
        board_label[i][j] = button

# Labels for turns and score using grid manager
turns_label = tk.Label(game_frame, text=f"Turns left: {turns_left}", bg="#add8e6", font=('Helvetica', 14))
turns_label.grid(row=board_size, column=0, columnspan=board_size)  # Place below the grid
score_label = tk.Label(game_frame, text=f"Score: {score}", bg="#add8e6", font=('Helvetica', 14))
score_label.grid(row=board_size + 1, column=0, columnspan=board_size)  # Place below the turns label
result_label = tk.Label(game_frame, text="", bg="#add8e6", font=('Helvetica', 14))
result_label.grid(row=board_size + 2, column=0, columnspan=board_size)  # Place below the score label

# Run the Tkinter event loop
root.mainloop()
