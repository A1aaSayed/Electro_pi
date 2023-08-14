def print_board(board):
    print('   0   1   2')
    for i, row in enumerate(board):
        print(f'{i}  {" | ".join(row)}')
        if i < len(board) - 1:
            print('   ' + '-' * 11)


def player_move(board, player):
    row = int(input(f'Player {player}, Enter a row number: '))
    while row > 2 or row < 0:
        print('Invalid move, Please try again!')
        row = int(input(f'Player {player}, Enter a row number: '))

    col = int(input(f'Player {player}, Enter a column number: '))
    while col > 2 or col < 0:
        print('Invalid move, Please try again!')
        col = int(input(f'Player {player}, Enter a column number: '))

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


def play_again():
    while True:
        playAgain = input('Do you want to play again? Choose yes or no: ').lower()
        if playAgain == 'yes':
            play_game()
        elif playAgain == 'no':
            print('Ok')
        break


def play_game():
    board = [[' '] * 3 for _ in range(3)]
    current_player = input('Choose your player X or O: ').upper()
    while True:
        print_board(board)
        player_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            play_again()
            break

        if check_tie(board):
            print("It's a tie!")
            play_again()
            break
        current_player = 'X' if current_player == 'O' else 'O'


play_game()