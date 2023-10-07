# Tic-Tac-Toe-o-x-Game


This Python program allows you to play Tic-Tac-Toe (also known as o-x) against an AI opponent that uses the minimax algorithm to make its moves.

Introduction
Tic-Tac-Toe (o-x) is a classic two-player game where one player uses the symbol 'X,' and the other uses 'O.' The game is played on a 3x3 grid, and the goal is to form a line of your symbol either horizontally, vertically, or diagonally.

This Python program lets you play against an AI opponent that uses the minimax algorithm to make intelligent moves.

Game Rules
The game follows standard Tic-Tac-Toe rules:

The game is played on a 3x3 grid.
Players take turns placing their symbol ('X' or 'O') on an empty cell.
The first player to form a line of their symbol horizontally, vertically, or diagonally wins the game.
If all cells are filled, and no player has won, the game ends in a draw.
Algorithm Used
This program utilizes the minimax algorithm for decision-making. The minimax algorithm is a recursive search algorithm used in two-player games to determine the best move for a player by considering all possible moves and their outcomes. In Tic-Tac-Toe, it helps the AI opponent make optimal moves to either win or force a draw.

Usage
To play the game, follow these steps:

Run the Python program.
The game board is displayed on the console.
Enter the number (1-9) corresponding to the cell where you want to place your 'X'.
The AI opponent will make its move using the minimax algorithm.
Continue taking turns until the game ends.
The program will announce the winner or declare a draw.
Implementation Details
The game board is represented as a list, initially filled with empty spaces.
The minimax algorithm is used to determine the AI opponent's moves.
Functions are defined to check for wins, draws, and to print the game board.
The program ensures valid user input and handles errors.
The game loop continues until a winner is declared or a draw occurs.
Future Improvements
Possible enhancements and features to consider for future development include:

Implementing a graphical user interface (GUI) for a more interactive user experience.
Adding difficulty levels for the AI opponent (easy, medium, hard).
Implementing a multiplayer mode for two human players to play against each other.
Keeping a record of game statistics and displaying them at the end.
Contributing
Contributions to this project are welcome! If you have ideas for improvements or new features, please feel free to fork the repository and submit pull requests.
