import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class LetterState:
    def __init__(self, character: str):
        self.character: str = character
        self.is_in_word: bool = False
        self.is_in_position: bool = False

    def __repr__(self):
        return f"[{self.character} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}]"


class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    VOIDED_LETTER = "*"

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()
        result = [LetterState(x) for x in word]
        remaining_secret = list(self.secret)

        # Check for GREEN letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.is_in_position = True
                remaining_secret[i] = self.VOIDED_LETTER

        # Check for YELLOW letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.is_in_position:
                continue
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.VOIDED_LETTER
                    letter.is_in_word = True
                    break

        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved


class WordleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.keyboard_buttons = {}  # Initialize the keyboard_buttons here
        self.initUI()
        self.word_set = self.load_word_set("games/Wordle/data/wordle_words.txt")
        self.secret = random.choice(list(self.word_set))
        self.wordle = Wordle(self.secret)
        self.attempt_count = 0

    def initUI(self):
        self.setWindowTitle("Wordle Game")
        self.setGeometry(100, 100, 400, 600)

        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E; /* Dark background */
                color: white; /* White text */
            }
            QLineEdit {
                background-color: #4E4E4E; /* Darker input box */
                color: white; /* White text */
                border: 2px solid #5A5A5A; /* Border color */
                padding: 5px;
                font-size: 18px; /* Larger font for input */
            }
            QLabel {
                background-color: #2E2E2E; /* Dark background for labels */
                border: 2px solid #5A5A5A; /* Border for grid cells */
                font-size: 24px; /* Font size for better visibility */
                border-radius: 8px; /* Rounded corners */
                padding: 10px; /* Padding for labels */
                margin: 5px; /* Margin around labels */
            }
            QPushButton {
                font-size: 16px; /* Font size for buttons */
                border: 2px solid #5A5A5A; /* Border color */
                border-radius: 8px; /* Rounded corners */
                padding: 10px; /* Padding for buttons */
            }
        """)

        layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.guess_entry = QLineEdit(self)
        self.guess_entry.setMaxLength(5)  # Assuming 5-letter words
        self.guess_entry.returnPressed.connect(self.submit_guess)  # Connect Enter key to submit_guess

        layout.addWidget(self.guess_entry)
        layout.addLayout(self.grid_layout)

        # Configure grid layout properties
        self.grid_layout.setSpacing(10)
        self.grid_layout.setContentsMargins(20, 20, 20, 20)

        # Set the grid cells for attempts (up to 6 attempts)
        for i in range(6):
            for j in range(5):
                label = QLabel("")
                label.setAlignment(Qt.AlignCenter)
                label.setFont(QFont("Arial", 24))  # Font size for better visibility
                label.setFixedSize(60, 60)  # Increased fixed size for uniformity
                label.setStyleSheet("border: 2px solid #5A5A5A; border-radius: 8px;")  # Border and rounded corners
                self.grid_layout.addWidget(label, i, j)

        # Create a label for displaying messages
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.message_label)

        # Create keyboard layout
        self.keyboard_layout = QGridLayout()
        self.create_keyboard()
        layout.addLayout(self.keyboard_layout)

        self.setLayout(layout)

    def load_word_set(self, path: str):
        word_set = set()
        try:
            with open(path, "r") as f:
                for line in f.readlines():
                    word = line.strip().upper()
                    word_set.add(word)
        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        return word_set

    def create_keyboard(self):
        keys = [
            "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
            "A", "S", "D", "F", "G", "H", "J", "K", "L",
            "Z", "X", "C", "V", "B", "N", "M"
        ]

        for index, key in enumerate(keys):
            button = QPushButton(key)
            button.setFixedSize(40, 40)
            button.clicked.connect(self.key_pressed)
            self.keyboard_buttons[key] = button
            self.keyboard_layout.addWidget(button, index // 10, index % 10)

    def key_pressed(self):
        button = self.sender()
        letter = button.text()
        if self.wordle.can_attempt:
            current_text = self.guess_entry.text()
            if len(current_text) < self.wordle.WORD_LENGTH:
                self.guess_entry.setText(current_text + letter)

    def submit_guess(self):
        x = self.guess_entry.text().upper()  # Convert input to uppercase
        self.guess_entry.clear()  # Clear the entry box

        if len(x) != self.wordle.WORD_LENGTH:
            self.display_message(f"Word must be {self.wordle.WORD_LENGTH} characters long!", "red")
            return

        if x not in self.word_set:
            self.display_message(f"{x} is not a valid word!", "red")
            return

        self.wordle.attempt(x)
        self.display_results()

    def display_results(self):
        result = self.wordle.guess(self.wordle.attempts[-1])
        self.update_grid(self.attempt_count, result)
        self.update_keyboard(result)
        self.attempt_count += 1

        if self.wordle.is_solved:
            self.display_message("You've solved the puzzle!", "green")
        elif not self.wordle.can_attempt:
            self.display_message(f"You failed to solve the puzzle! The secret word was: {self.wordle.secret}", "red")

    def update_grid(self, row, result):
        for col, letter in enumerate(result):
            label = self.grid_layout.itemAtPosition(row, col).widget()
            label.setText(letter.character)  # Set letter in the label

            # Set styles based on letter state
            if letter.is_in_position:
                self.set_tile_style(label, "green", "white")  # Green for correct position
            elif letter.is_in_word:
                self.set_tile_style(label, "yellow", "black")  # Yellow for correct letter
            else:
                self.set_tile_style(label, "gray", "white")  # Gray for incorrect letter

    def set_tile_style(self, label, bg_color, text_color):
        label.setStyleSheet(f"background-color: {bg_color}; color: {text_color}; border: 2px solid #5A5A5A; border-radius: 8px;")

    def update_keyboard(self, result):
        for letter in result:
            button = self.keyboard_buttons[letter.character]
            if letter.is_in_position:
                self.set_key_style(button, "green")  # Green for correct position
            elif letter.is_in_word:
                self.set_key_style(button, "yellow")  # Yellow for correct letter
            else:
                self.set_key_style(button, "gray")  # Gray for incorrect letter

    def set_key_style(self, button, color):
        if color == "green":
            button.setStyleSheet("background-color: green; color: white; border: 2px solid #5A5A5A; border-radius: 8px;")
        elif color == "yellow":
            button.setStyleSheet("background-color: yellow; color: black; border: 2px solid #5A5A5A; border-radius: 8px;")
        elif color == "gray":
            button.setStyleSheet("background-color: gray; color: white; border: 2px solid #5A5A5A; border-radius: 8px;")

    def display_message(self, message, color):
        self.message_label.setText(message)  # Set the message in the label
        if color == "red":
            self.message_label.setStyleSheet("color: red;")  # Set text color to red for errors
        elif color == "green":
            self.message_label.setStyleSheet("color: green;")  # Set text color to green for success


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WordleGUI()
    ex.show()
    sys.exit(app.exec_())
