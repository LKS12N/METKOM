import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"  # Player starts as X
        self.board = [[None, None, None] for _ in range(3)]
        self.create_widgets()
        
    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 36), width=5, height=2, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button
                
        self.status_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=('Arial', 16))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)
    
    def make_move(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                self.end_game(f"Player {self.current_player} wins!")
            elif self.is_board_full():
                self.end_game("It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
                
                if self.current_player == "O":  # Bot's turn
                    self.root.after(500, self.bot_move)
    
    def bot_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.make_move(row, col)
    
    def find_best_move(self):
        best_val = -float('inf')
        best_move = None
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None:
                    self.board[r][c] = "O"
                    move_val = self.minimax(0, False)
                    self.board[r][c] = None
                    if move_val > best_val:
                        best_move = (r, c)
                        best_val = move_val
        return best_move
    
    def minimax(self, depth, is_max):
        score = self.evaluate_board()
        if score == 10:
            return score
        if score == -10:
            return score
        if self.is_board_full():
            return 0
        
        if is_max:
            best = -float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] is None:
                        self.board[r][c] = "O"
                        best = max(best, self.minimax(depth + 1, not is_max))
                        self.board[r][c] = None
            return best
        else:
            best = float('inf')
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] is None:
                        self.board[r][c] = "X"
                        best = min(best, self.minimax(depth + 1, not is_max))
                        self.board[r][c] = None
            return best
    
    def evaluate_board(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] is not None:
                if row[0] == "O":
                    return 10
                elif row[0] == "X":
                    return -10
                
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] is not None:
                if self.board[0][col] == "O":
                    return 10
                elif self.board[0][col] == "X":
                    return -10
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            if self.board[0][0] == "O":
                return 10
            elif self.board[0][0] == "X":
                return -10
        if self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            if self.board[0][2] == "O":
                return 10
            elif self.board[0][2] == "X":
                return -10
        
        return 0

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] is not None:
                return True
                
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] is not None:
                return True
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            return True
        
        return False

    def is_board_full(self):
        for row in self.board:
            if None in row:
                return False
        return True
    
    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
