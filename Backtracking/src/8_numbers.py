def isValid(board: list[int], curr: int) -> bool:
    """
    Check if board configuration is valid.

    Args:
        board (list[int]): Board to validate.
        curr (int): Current square.

    Returns:
        bool: True if the board is valid, False otherwise.
    """
    # Neighbor list for each square
    neighbors = [
        [-1],             # 0
        [0, -1],          # 1
        [0, 1, -1],       # 2
        [0, 2, -1],       # 3
        [1, 2, -1],       # 4
        [1, 2, 3, 4, -1], # 5
        [2, 3, 5, -1],    # 6
        [4, 5, 6, -1]     # 7
    ]

    for i in range(curr):
        # Check if number has already been used
        if board[curr] == board[i]:
            return False


    # For each neighbor of current square
    for i in range(len(neighbors[curr]) - 1):
        if (board[neighbors[curr][i]] + 1 == board[curr]) or (board[neighbors[curr][i]] - 1 == board[curr]):
            return False

    return True

def print_board(board: list[int]) -> None:
    """
    Print the given board.

    Args:
        board (list[int]): Board to be printed.
    """
    global solutions
    print(f"Solutions #{solutions + 1}:")
    print(f"  {board[1]}{board[4]}")
    print(f" {board[0]}{board[2]}{board[5]}{board[7]}")
    print(f"  {board[3]}{board[6]}\n")
    solutions += 1

def solve(board: list[int], curr: int) -> None:
    """
    Recursive function to find the next solution.

    Args:
        board (list[int]): Board to be solved.
        curr (int): _description_
    """
    if curr == 8: print_board(board)
        
    else:
        for board[curr] in range(1, 9):
            if isValid(board, curr):
                solve(board, curr + 1)

if __name__ == "__main__":
    board = [-1] * 8
    solutions = 0
    solve(board, solutions)
    print(f"Total number of solutions: {solutions}")