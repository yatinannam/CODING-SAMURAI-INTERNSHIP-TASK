# Initial empty board
board = [0 for _ in range(9)]  # 0 = empty, 1 = X (player), 2 = O (computer)

# Display the board
def display_board():
    symbols = [' ', 'X', 'O']
    for i in range(3):
        row = [symbols[board[3*i + j]] for j in range(3)]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")

# Player move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == 0:
                board[move] = 1
                break
        print("Invalid move. Try again.")

# Check win condition
def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combinations)

# Check draw condition
def is_draw():
    return all(cell != 0 for cell in board)

# Minimax algorithm
def minimax(board_state, is_maximizing):
    if check_winner(2): return 1      # Computer wins
    if check_winner(1): return -1     # Player wins
    if is_draw(): return 0            # Draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board_state[i] == 0:
                board_state[i] = 2
                score = minimax(board_state, False)
                board_state[i] = 0
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board_state[i] == 0:
                board_state[i] = 1
                score = minimax(board_state, True)
                board_state[i] = 0
                best_score = min(score, best_score)
        return best_score

# Computer move using minimax
def computer_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == 0:
            board[i] = 2
            score = minimax(board, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = 2
        print(f"Computer plays at position {best_move + 1}")

# Game loop
if __name__ == "__main__":
    while True:
        display_board()
        player_move()
        display_board()

        if check_winner(1):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw!")
            break

        computer_move()
        display_board()

        if check_winner(2):
            print("Computer wins! 🤖")
            break
        if is_draw():
            print("It's a draw!")
            break
        