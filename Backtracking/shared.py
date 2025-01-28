def is_valid(board: list[int]) -> bool:
    """
    Check if the current board configuration is valid.

    Args:
        board (list[int]): Board to be validated

    Returns:
        bool: True if the board is valid, False otherwise
    """
    # index rows one by one
    for i in range(len(board)):
        # check the remaining rows
        for j in range(i + 1, len(board)):
            # Check any two queens in the same column or diagonals
            if (board[i] == board[j]) or (abs(board[i] - board[j]) == abs(i - j)):
                return False

    return True

def print_board(board: list[int], solution_number: int) -> None:
    """
    Print the board with Qs for queens and * for empty spaces.

    Args:
        board (list[int]): Board to be printed
        solution_number (int): _description_
    """
    print(f"Solution {solution_number}:")
    
    for i in range(len(board)):
        row = ['*'] * len(board)
        row[board[i]] = 'Q'
        
        # transfer row to a string; otherwise, print the array on the screen.
        print(' '.join(row))
        
    # Add a new line for spacing between solutions
    print("\n")