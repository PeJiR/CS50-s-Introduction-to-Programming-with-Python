def tic_tac_toe():
  """Plays a game of tic-tac-toe."""
  board = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]
  turn = 'X'

  while True:
    print_board(board)

    # Get the user's move.
    row, col = get_move(turn)

    # Make the move.
    board[row][col] = turn

    # Check for a winner.
    winner = check_winner(board)
    if winner:
      print(f'{winner} wins!')
      break

    # Switch turns.
    turn = 'O' if turn == 'X' else 'X'

def print_board(board):
  """Prints the tic-tac-toe board."""
  for row in board:
    print(' '.join(row))

def get_move(turn):
  """Gets the user's move."""
  while True:
    row = input(f'Player {turn}, enter your row (1-3): ')
    col = input(f'Player {turn}, enter your column (1-3): ')

    row = int(row) - 1
    col = int(col) - 1

    if row < 0 or row >= 3 or col < 0 or col >= 3:
      print('Invalid move. Please enter a row and column between 1 and 3.')
      continue

    if board[row][col] != ' ':
      print('That space is already taken. Please choose another space.')
      continue

    return row, col

def check_winner(board):
  """Checks for a winner in the tic-tac-toe board."""
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2] != ' ':
      return board[row][0]

  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] != ' ':
      return board[0][col]

  if board[0][0] == board[1][1] == board[2][2] != ' ':
    return board[0][0]

  if board[0][2] == board[1][1] == board[2][0] != ' ':
    return board[0][2]

  return None