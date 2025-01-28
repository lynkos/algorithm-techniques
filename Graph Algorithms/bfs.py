from collections import deque
from shared import isValid, START, END, NEIGHBORS, MAZE

def BFS(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> int:
    """
    Find the optimal path in a maze using BFS.

    Args:
        maze (list[list[int]]): Maze to traverse.
        start (tuple[int, int]): Coordinate (x1, y1) of the starting position.
        end (tuple[int, int]): Coordinate (x2, y2) of the end position.

    Returns:
        int: The minimum number of steps to reach the end position from start, or -1 if no path exists.
    """
    # Initialize queue with starting position
    queue = deque([ (start[0], start[1], 0) ])

    # Initialize visited 2D array
    visited = [ [ False for _ in range(len(maze)) ] for _ in range(len(maze[0])) ]

    # Mark starting position as visited
    visited[start[0]][start[1]] = True

    # While queue is not empty
    while queue:
        # Dequeue current position and steps
        x, y, steps = queue.popleft()

        # If goal is reached, return steps
        if (x, y) == end: return steps

        # Explore all neighbors in all possible directions
        for dx, dy in NEIGHBORS:
            # Calculate neighbor position (i.e. x-coordinates and y-coordinates)
            nx, ny = x + dx, y + dy

            # Check if the neighbor is valid (i.e. within bounds and not blocked) and has not been visited
            if isValid(maze, nx, ny) and not visited[nx][ny]:
                # Mark neighbor as visited
                visited[nx][ny] = True

                # Add to queue
                queue.append((nx, ny, steps + 1))

    # If no path exists, return -1
    return -1
    
if __name__ == "__main__":
    # Find optimal path using BFS
    path = BFS(MAZE, START, END)

    # If path not found, print message
    if path == -1:
        print(f"No path found from {START} to {END}.")

    # Else, if path found, print message
    else:
        print(f"Optimal path from {START} to {END} found in {path} steps.")