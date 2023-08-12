def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def player_move(board, player):
    move = input(f'Player {player}, enter your move (row and column): ')
    row, col = map(int, move.split())
    if board[row][col] == ' ':
        board[row][col] = player
    else:
        print("Invalid move, try again!")
        player_move(board, player)


def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def check_tie(board):
    return all(all(square != ' ' for square in row) for row in board)


def play_game():
    board = [[' '] * 3 for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            break
        if check_tie(board):
            print("It's a tie!")
            break
        current_player = 'X' if current_player == 'O' else 'O'


play_game()