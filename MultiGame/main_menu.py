import tkinter as tk
import subprocess
import os
from tkinter import font
from PIL import Image, ImageTk  # Importing the necessary modules from Pillow

def launch_game_2048():
    game_path = os.path.join('games', '_2048', 'main2048.py')
    subprocess.Popen(['python', game_path])

def launch_game_Wordle():
    game_path = os.path.join('games', 'Wordle', 'play_wordle.py')
    subprocess.Popen(['python', game_path])
    
def launch_game_PingPong():
    game_path = os.path.join('games', 'PingPong', 'PingPong.py')
    subprocess.Popen(['python', game_path])

def launch_game_BattleShip():
    game_path = os.path.join('games', 'BattleShip', 'mainship.py')
    subprocess.Popen(['python', game_path])

# Set up the main window
root = tk.Tk()
root.title("Game Menu")
root.geometry("400x300")  # Set window size

# Load the background JPEG image
background_image = Image.open('background.jpg')  # Update with your image path
background_image = background_image.resize((400, 300), Image.LANCZOS)  # Resize the image if necessary
background_photo = ImageTk.PhotoImage(background_image)  # Convert to PhotoImage

# Create a label for the background
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the title label
title_label = tk.Label(root, text="Welcome to the Game Menu", font=("Helvetica", 16), bg="#f9f9f9", fg="#333")
title_label.pack(pady=30)

# Load custom font
custom_font = font.Font(family="Helvetica", size=14, weight="bold")

# Create buttons to launch the games
play_button_2048 = tk.Button(root, text="Play 2048", command=launch_game_2048, font=custom_font, 
                        bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=10)
play_button_2048.pack(pady=10)

play_button_wordle = tk.Button(root, text="Play Wordle", command=launch_game_Wordle, font=custom_font, 
                        bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=10)
play_button_wordle.pack(pady=10)

play_button_pingpong = tk.Button(root, text="Play PingPong", command=launch_game_PingPong, font=custom_font, 
                        bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=10)
play_button_pingpong.pack(pady=10)

play_button_battleship = tk.Button(root, text="Play BattleShip", command=launch_game_BattleShip, font=custom_font, 
                        bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=10)
play_button_battleship.pack(pady=10)

# Add a footer label
footer_label = tk.Label(root, text="Enjoy your game!", font=("Helvetica", 12), bg="#f9f9f9", fg="#555")
footer_label.pack(side="bottom", pady=20)

# Start the GUI event loop
root.mainloop()
