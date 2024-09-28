import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QLabel
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from letter_state import LetterState  # Ensure this is correctly implemented
from wordle import Wordle  # Ensure this is correctly implemented


class WordleGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Load words and select secret word
        self.word_set = self.load_word_set("data/wordle_words.txt")
        self.secret = random.choice(list(self.word_set))
        self.wordle = Wordle(self.secret)
        self.attempt_count = 0

    def initUI(self):
        self.setWindowTitle("Wordle Game")
        self.setGeometry(100, 100, 400, 500)

        # Set dark mode stylesheet
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
                border: 2px solid black; /* Border for grid cells */
                font-size: 24px; /* Font size for better visibility */
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
                label.setFixedSize(50, 50)  # Fixed size for uniformity
                label.setStyleSheet("border: 2px solid black;")  # Border for grid cells
                self.grid_layout.addWidget(label, i, j)

        # Create a label for displaying messages
        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setFont(QFont("Arial", 18))
        layout.addWidget(self.message_label)

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
        self.attempt_count += 1

        if self.wordle.is_solved:
            self.display_message("You've solved the puzzle!", "green")
        elif not self.wordle.can_attempt:
            self.display_message(f"You failed to solve the puzzle! The secret word was: {self.wordle.secret}", "red")

    def update_grid(self, row, result):
        for col, letter in enumerate(result):
            label = self.grid_layout.itemAtPosition(row, col).widget()
            label.setText(letter.character)  # Set letter in the label

            if letter.is_in_position:
                label.setStyleSheet("background-color: green; color: white; border: 2px solid black;")
            elif letter.is_in_word:
                label.setStyleSheet("background-color: yellow; color: black; border: 2px solid black;")
            else:
                label.setStyleSheet("background-color: gray; color: white; border: 2px solid black;")

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
