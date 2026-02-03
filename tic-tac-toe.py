# Tic Tac Toe Game in Python (Console)

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

def play_game():
    current_player = "X"
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1 to 9")
    print_board()

    while True:
        move = input(f"Player {current_player}, enter position (1-9): ")

        if not move.isdigit():
            print("Invalid input. Enter a number.")
            continue

        move = int(move) - 1

        if move < 0 or move > 8:
            print("Position out of range.")
            continue

        if board[move] != " ":
            print("Position already taken.")
            continue

        board[move] = current_player
        print_board()

        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if check_draw():
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
