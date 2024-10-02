import tkinter as tk
import random

# Constants
BOARD_SIZE = 4  # The board will be 4x4
TILE_SIZE = 100  # Size of each tile
RADIUS = 20  # Radius for rounded corners

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Game")
        self.board = self.initialize_board()
        self.score = 0

        self.create_widgets()
        self.display_board()
        self.update_score()

    def initialize_board(self):
        board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.add_new_tile(board)
        self.add_new_tile(board)
        return board

    def add_new_tile(self, board):
        empty_tiles = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            board[r][c] = random.choice([2, 4])

    def create_widgets(self):
        self.score_label = tk.Label(self.root, text="Score: 0", font=('Arial', 24))
        self.score_label.pack()

        self.canvas = tk.Canvas(self.root, width=BOARD_SIZE * TILE_SIZE, height=BOARD_SIZE * TILE_SIZE, bg="#bbada0")
        self.canvas.pack()

        self.root.bind("<Key>", self.key_pressed)

    def get_color(self, value):
        colors = {
            0: "#ccc0b3", 2: "#eee4da", 4: "#ede0c8",
            8: "#f2b179", 16: "#f59563", 32: "#f67c5f",
            64: "#f67c5f", 128: "#f9b8a1", 256: "#fcac6c",
            512: "#fc6e3d", 1024: "#f94c3b", 2048: "#f83e29"
        }
        return colors.get(value, "#3c3a32")

    def draw_rounded_rectangle(self, x1, y1, x2, y2, radius, color):
        # Draw rounded rectangle using arcs and rectangles
        self.canvas.create_oval(x1, y1, x1 + radius * 2, y1 + radius * 2, fill=color, outline="")
        self.canvas.create_oval(x2 - radius * 2, y1, x2, y1 + radius * 2, fill=color, outline="")
        self.canvas.create_oval(x1, y2 - radius * 2, x1 + radius * 2, y2, fill=color, outline="")
        self.canvas.create_oval(x2 - radius * 2, y2 - radius * 2, x2, y2, fill=color, outline="")
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=color, outline="")
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=color, outline="")

    def draw_tile(self, r, c, value):
        x1 = c * TILE_SIZE
        y1 = r * TILE_SIZE
        x2 = x1 + TILE_SIZE
        y2 = y1 + TILE_SIZE
        color = self.get_color(value)
        
        # Draw the tile
        self.draw_rounded_rectangle(x1, y1, x2, y2, RADIUS, color)

        # Draw the text
        self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(value) if value > 0 else "", font=('Arial', 24), fill="#776e65", tags=f"text_{r}_{c}")

    def clear_board(self):
        self.canvas.delete("all")  # Clear all items on the canvas

    def display_board(self):
        self.clear_board()
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                value = self.board[r][c]
                self.draw_tile(r, c, value)

    def key_pressed(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.handle_key(event.keysym)

    def handle_key(self, direction):
        if direction == 'Up':
            self.move_up()
        elif direction == 'Down':
            self.move_down()
        elif direction == 'Left':
            self.move_left()
        elif direction == 'Right':
            self.move_right()

        if self.is_game_over():
            self.display_game_over()

    def move_up(self):
        for c in range(BOARD_SIZE):
            col = [self.board[r][c] for r in range(BOARD_SIZE)]
            new_col = self.combine_tiles(col)
            for r in range(BOARD_SIZE):
                self.board[r][c] = new_col[r]
        self.add_new_tile(self.board)
        self.update_score()
        self.display_board()

    def move_down(self):
        for c in range(BOARD_SIZE):
            col = [self.board[r][c] for r in range(BOARD_SIZE)][::-1]
            new_col = self.combine_tiles(col)[::-1]
            for r in range(BOARD_SIZE):
                self.board[r][c] = new_col[r]
        self.add_new_tile(self.board)
        self.update_score()
        self.display_board()

    def move_left(self):
        for r in range(BOARD_SIZE):
            self.board[r] = self.combine_tiles(self.board[r])
        self.add_new_tile(self.board)
        self.update_score()
        self.display_board()

    def move_right(self):
        for r in range(BOARD_SIZE):
            self.board[r] = self.combine_tiles(self.board[r][::-1])[::-1]
        self.add_new_tile(self.board)
        self.update_score()
        self.display_board()

    def combine_tiles(self, tiles):
        new_tiles = [num for num in tiles if num != 0]
        for i in range(len(new_tiles) - 1):
            if new_tiles[i] == new_tiles[i + 1]:
                new_tiles[i] *= 2
                self.score += new_tiles[i]  # Update score on combine
                new_tiles[i + 1] = 0
        new_tiles = [num for num in new_tiles if num != 0]
        while len(new_tiles) < BOARD_SIZE:
            new_tiles.append(0)
        return new_tiles

    def is_game_over(self):
        if any(0 in row for row in self.board):
            return False
        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE - 1):
                if self.board[r][c] == self.board[r][c + 1] or self.board[c][r] == self.board[c + 1][r]:
                    return False
        return True

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def display_game_over(self):
        self.canvas.create_text((BOARD_SIZE * TILE_SIZE) / 2, (BOARD_SIZE * TILE_SIZE) / 2, text="Game Over!", font=('Arial', 48), fill="black", tags="game_over")

# Main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
