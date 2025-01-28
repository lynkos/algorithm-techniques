from shared import is_valid, print_board
    
def recursive(board: list[int], cur_row: int, solutions: list[list[int]]) -> None:
    """
    Brute-force solution to the 4 Queens problem using recursion.

    Args:
        board (list[int]): Board to be solved
        cur_row (int): Current row in board
        solutions (list[list[int]]): List of solutions (i.e. valid board configurations)
    """
    # terminate condition for recursion
    if cur_row == len(board):
        # if valid, one correct placement, so save it.
        if is_valid(board):
            # use board[:] instead of board only to avoid the shallow copy problem in python
            solutions.append(board[:])
        return
        
    # for each column in the current row
    for col in range(len(board)):
        # place one queen in column col, e.g., [cur_cow, col]
        board[cur_row] = col
        
        # go to the next row
        recursive(board, cur_row + 1, solutions)

if __name__ == "__main__":
    n = 4
    board = [-1] * n # the index represents row; the value represent column
    solutions = []
    
    # Run the recursive brute-force solution
    recursive(board, 0, solutions)
    
    # Print all solutions
    for i, solution in enumerate(solutions):
        # since i is from 0, we print i+1 for users
        print_board(solution, i + 1)
        
    print(f"Total number of solutions: {len(solutions)}")