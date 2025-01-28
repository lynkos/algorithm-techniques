# SHARED CONSTANTS
START = (0, 0)
END = (9, 9)
NEIGHBORS = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
MAZE = [
        [ 0, 0, 1, 0, 0, 0, 1, 1, 1, 0 ],
        [ 1, 0, 1, 1, 0, 1, 0, 0, 0, 0 ],
        [ 0, 0, 0, 0, 0, 1, 1, 0, 1, 1 ],
        [ 0, 1, 1, 1, 0, 0, 0, 1, 1, 0 ],
        [ 0, 0, 0, 0, 0, 1, 0, 0, 1, 0 ],
        [ 1, 1, 1, 0, 1, 1, 0, 1, 1, 0 ],
        [ 0, 0, 1, 0, 0, 0, 0, 0, 1, 1 ],
        [ 1, 0, 1, 0, 1, 1, 1, 0, 0, 0 ],
        [ 1, 0, 0, 0, 0, 0, 0, 1, 1, 0 ],
        [ 0, 1, 1, 1, 1, 0, 0, 0, 0, 0 ]
        ]

# SHARED METHODS
def withinBounds(maze: list[list[int]], x: int, y: int) -> bool:
    """
    Check if a given coordinate is within the bounds of the maze.

    Args:
        maze (list[list[int]]): Maze to check against.
        x (int): X-coordinate to check.
        y (int): Y-coordinate to check.

    Returns:
        bool: True if (x, y) is within the bounds of maze, else False.
    """
    return (0 <= x < len(maze)) and (0 <= y < len(maze[0]))

def isValid(maze: list[list[int]], x: int, y: int) -> bool:
    """
    Check if a given coordinate is valid in a given maze.

    Args:
        maze (list[list[int]]): The maze to check against.
        x (int): X-coordinate to check.
        y (int): Y-coordinate to check.

    Returns:
        bool: True if the coordinate is valid, else False.
    """
    # Check if the coordinate is within the bounds of the maze and is not a wall
    return (withinBounds(maze, x, y)) and (maze[x][y] == 0)