import tkinter as tk
from tkinter import messagebox

# pip install tkinter

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("600x500")

        self.username1 = ""
        self.username2 = ""
        self.score1 = 0
        self.score2 = 0

        self.current_player = "X"
        self.board = [""] * 9

        self.username_label = tk.Label(root, text="Enter usernames:")
        self.username_label.pack()

        self.username_frame = tk.Frame(root)
        self.username1_label = tk.Label(self.username_frame, text="Player 1:")
        self.username1_label.pack(side=tk.LEFT)
        self.username1_entry = tk.Entry(self.username_frame)
        self.username1_entry.pack(side=tk.LEFT)
        self.username2_label = tk.Label(self.username_frame, text="Player 2:")
        self.username2_label.pack(side=tk.LEFT)
        self.username2_entry = tk.Entry(self.username_frame)
        self.username2_entry.pack(side=tk.LEFT)
        self.username_frame.pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.score_label = tk.Label(root, text="Scores: {} - {} :{}".format(self.score1, self.score2, "Tie"))
        self.score_label.pack()

        self.buttons_frame = tk.Frame(root)
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.buttons_frame, text="", width=10, height=3, command=lambda i=i: self.make_move(i))
            self.buttons.append(button)
            button.grid(row=i // 3, column=i % 3)
        self.buttons_frame.pack()

    def start_game(self):
        self.username1 = self.username1_entry.get()
        self.username2 = self.username2_entry.get()
        self.start_button.config(state=tk.DISABLED)
        self.username1_entry.config(state=tk.DISABLED)
        self.username2_entry.config(state=tk.DISABLED)

    def make_move(self, index):
        if not self.board[index]:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.update_scores()
                self.show_winner()
            elif "" not in self.board:
                self.update_scores(tie=True)
                self.show_tie()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def update_scores(self, tie=False):
        if tie:
            self.score1 += 1
            self.score2 += 1
        elif self.current_player == "X":
            self.score1 += 1
        else:
            self.score2 += 1
        self.score_label.config(text="Scores: {} - {} :{}".format(self.score1, self.score2, "Tie" if tie else ""))

    def show_winner(self):
        winner = self.username1 if self.current_player == "X" else self.username2
        messagebox.showinfo("Game Over", "Congratulations! {} wins!".format(winner))
        self.reset_board()

    def show_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
