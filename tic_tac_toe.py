import tkinter as tk
import math

game_board = [""] * 9
window = tk.Tk()
window.title("Minimax Tic-Tac-Toe")

btn_list = []

def check_win(player_mark):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # cols
        (0, 4, 8), (2, 4, 6)             # diagonals
    ]
    for x, y, z in win_combinations:
        if game_board[x] == game_board[y] == game_board[z] == player_mark:
            return True
    return False

def minimax_algo(is_maximizing):
    if check_win("O"): return 1
    if check_win("X"): return -1
    if "" not in game_board: return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if game_board[i] == "":
                game_board[i] = "O"
                best_score = max(best_score, minimax_algo(False))
                game_board[i] = ""
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if game_board[i] == "":
                game_board[i] = "X"
                best_score = min(best_score, minimax_algo(True))
                game_board[i] = ""
        return best_score

def make_ai_move():
    best_score = -math.inf
    chosen_move = None
    for i in range(9):
        if game_board[i] == "":
            game_board[i] = "O"
            score = minimax_algo(False)
            game_board[i] = ""
            if score > best_score:
                best_score = score
                chosen_move = i
                
    if chosen_move is not None:
        game_board[chosen_move] = "O"
        btn_list[chosen_move]["text"] = "O"

def handle_click(position):
    if game_board[position] != "":
        return
    game_board[position] = "X"
    btn_list[position]["text"] = "X"
    
    if check_win("X"):
        status_label.config(text="Result: You Win!")
        return
        
    make_ai_move()
    if check_win("O"):
        status_label.config(text="Result: AI Wins!")
        return
    elif "" not in game_board:
        status_label.config(text="Result: It's a Draw!")
        return

for i in range(9):
    button = tk.Button(window, text="", width=10, height=5, font=('Arial', 24),
                       command=lambda i=i: handle_click(i))
    button.grid(row=i//3, column=i%3)
    btn_list.append(button)

status_label = tk.Label(window, text="Your turn (X)", font=('Arial', 16))
status_label.grid(row=4, column=0, columnspan=3)

if __name__ == "__main__":
    window.mainloop()
