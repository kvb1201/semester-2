import numpy as np
import random
import matplotlib.pyplot as plt


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(board, row):
    """
    Solve the 8-queens problem using backtracking with a randomized column order.
    """
    if row == 8:
        return True  # If all queens are placed successfully, return True

    cols = np.arange(8)  # Create array [0,1,2,3,4,5,6,7]
    np.random.shuffle(cols)  # Shuffle columns for randomness

    for col in cols:
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            if solve_n_queens(board, row + 1):
                return True
            board[row] = -1  # Backtrack

    return False


def print_solution(board):
    """
    Print the chessboard with queens in the terminal.
    """
    chessboard = np.full((8, 8), ".", dtype=str)  # Create empty board with "."
    for i in range(8):
        chessboard[i, board[i]] = "Q"  # Place queens
    print("\n".join([" ".join(row) for row in chessboard]), "\n")



def main():
    board = np.full(8, -1)  # Initialize 1D board with -1 (no queen placed)
    while not solve_n_queens(board, 0):  # Keep trying until a valid solution is found
        pass
    print_solution(board)


if __name__ == "__main__":
    main()