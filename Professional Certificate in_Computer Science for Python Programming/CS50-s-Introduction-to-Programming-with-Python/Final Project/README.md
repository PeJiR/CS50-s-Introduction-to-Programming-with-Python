# Project Title: Tic-Tac-Toe Game in Python

### [Video Demo](https://youtu.be/T85OjtX9J4k)

### [Play this game online](https://www.online-python.com/oQn49MZL3r)

### Description:

This project is a simple tic-tac-toe game implemented in Python. The game can be played by two players, who take turns placing their marks (X or O) on a 3x3 grid. The first player to get three of their marks in a row, column, or diagonal wins the game.

**Features** :

Two-player support
Command-line interface
Basic game logic
Error checking

**Installation:**

To install the game, simply clone the repository to your local machine:

    git clone https://github.com/PeJiR/Professional-Certificates.git


**Usage:**

To play the game, simply navigate to the project directory and run the following command:

    python project.py

You will be prompted to enter the names of the two players. The game will then begin, and the players will take turns placing their marks on the board.

**Controls:**

To place a mark on the board, simply enter the row and column number of the space you want to mark. For example, to place your mark in the middle space, you would enter 2 2.

**Winning the Game:**

The first player to get three of their marks in a row, column, or diagonal wins the game. If the board is full and there is no winner, the game is a draw.

**Design Choices:**

The design choices for this project were made with the following goals in mind:

Simplicity: The game should be easy to play and understand for players of all ages and skill levels.
Fairness: The game should be fair and balanced for both players.
Portability: The game should be playable on any platform that has a Python interpreter.

**Additional Considerations:**

In addition to the design choices listed above, the following considerations were also made when developing this project:

Error checking: The game should prevent players from making invalid moves, such as placing their mark in a space that is already taken.
Code quality: The game code should be well-written and easy to maintain.

**Conclusion:**

This project is a simple but complete implementation of a tic-tac-toe game in Python. The game is fair, portable, and easy to play. The code is also well-written and easy to maintain.

```python

def tic_tac_toe():
    """Plays a game of tic-tac-toe."""
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    turn = 'X'

    print('Welcome to Tic-Tac-Toe!')
    print('This is a game for two players. Each player will take turns placing their mark (X or O) on a 3x3 grid.')
    print('The first player to get three of their marks in a row, column, or diagonal wins the game.')
    print('To make a move, enter the row and column of the space you want to place your mark. For example, to place your mark in the middle space, you would enter 2 2.')
    print('The game will continue until there is a winner or the board is full. If the board is full and there is no winner, the game is a draw.')
    print('Let\'s play!')

    # Get the user's name.
    player1_name = input('Player 1, enter your name: ')
    player2_name = input('Player 2, enter your name: ')

    while True:
        print_board(board)

        # Get the user's move.
        if turn == 'X':
            player_name = player1_name
        else:
            player_name = player2_name
        row, col = get_move(turn, player_name, board)

        # Make the move.
        board[row][col] = turn

        # Check for a winner.
        winner = check_winner(board)
        if winner:
            print_board(board)  # Display the final board before announcing the winner.
            print(f'{player_name} wins!')
            break

        # Check for a draw.
        if is_full(board):
            print_board(board)  # Display the final board before announcing the draw.
            print("It's a draw!")
            break

        # Switch turns.
        turn = 'O' if turn == 'X' else 'X'

def print_board(board):
    """Prints the tic-tac-toe board."""
    for row in board:
        print(' '.join(row))

def get_move(turn, player_name, board):
    """Gets the user's move."""
    while True:
        try:
            move = input(f'{player_name}, enter your move (row column): ')
            row, col = map(int, move.split())

            if row < 1 or row > 3 or col < 1 or col > 3:
                print('Invalid move. Please enter row and column numbers between 1 and 3.')
                continue

            if board[row - 1][col - 1] != ' ':
                print('That space is already taken. Please choose another space.')
                continue

            return row - 1, col - 1
        except ValueError:
            print('Invalid input. Please enter your move as two numbers (row column).')

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

def is_full(board):
    """Checks if the board is full."""
    for row in board:
        if ' ' in row:
            return False
    return True

# Start the game
tic_tac_toe()
```



#### [Back to main Menu](https://github.com/PeJiR/Harvard-University-Certificates/tree/main)
