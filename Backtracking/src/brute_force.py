from shared import is_valid, print_board
    
def brute_force(board: list[int], counter: int) -> None:
    """
    Brute-force solution to the 4 Queens problem using four nested loops.

    Args:
        board (list[int]): Board to be 
        counter (int): Keeps track of the number of solutions
    """
    # first row
    for col1 in range(len(board)):
        # place the first queen in column q1, e.g., [0, q1]
        board[0] = col1
        
        # second row
        for col2 in range(len(board)):
            # place the first queen in column q2, e.g., [1, q2]
            board[1] = col2
            
            # third row
            for col3 in range(len(board)):
                # place the first queen in column q1, e.g., [2, q3]
                board[2] = col3
                
                # fourth row
                for col4 in range(len(board)):
                    # place the first queen in column q1, e.g., [3, q4]
                    board[3] = col4
                    
                    # Check if the placement forms a valid solution
                    if is_valid(board):
                        counter += 1
                        print_board(board, counter) # Print the board
                        
    print(f"Total number of solutions: {counter}")

if __name__ == "__main__":
    n = 4
    counter = 0 # to count and print the solution number
    board = [-1] * n # the index represents row; the value represent column

    # Run the brute-force solution
    brute_force(board, counter)