from shared import isValid, START, END, NEIGHBORS, MAZE

def DFS(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> float | int:
    """
    Find the optimal path in a maze using DFS.

    Args:
        maze (list[list[int]]): Maze to traverse.
        start (tuple[int, int]): Coordinate (x1, y1) of the starting position.
        end (tuple[int, int]): Coordinate (x2, y2) of the end position.

    Returns:
        float | int: -1 if no path found, else the minimum number of steps to reach the end position from start.
    """
    # Initialize stack with starting position
    stack = [ (start[0], start[1], 0) ]

    # Initialize visited 2D array
    visited = [ [ False for _ in range(len(maze)) ] for _ in range(len(maze[0])) ]

    # Initialize minimum steps
    min_steps = float("inf")

    # Initialize found flag
    found = False

    # While stack is not empty
    while len(stack) > 0:
        # Pop current position and steps
        x, y, steps = stack.pop()

        # If goal is reached
        if (x, y) == end:
            # Update minimum steps
            min_steps = min(min_steps, steps)

            # Update found flag (i.e. path exists)
            found = True

            # Continue finding all possible paths
            continue

        # Mark current position as visited
        visited[x][y] = True

        # Explore all neighbors in all possible directions
        for dx, dy in NEIGHBORS:
            # Calculate neighbor position (i.e. x-coordinates and y-coordinates)
            nx, ny = x + dx, y + dy

            # Check if the neighbor is valid (i.e. within bounds and not blocked) and has not been visited
            if isValid(maze, nx, ny) and not visited[nx][ny]:
                # Add to stack
                stack.append((nx, ny, steps + 1))

    # Return minimum steps if path found
    if found: return min_steps

    # Else, if no path exists, return -1
    else: return -1
    
if __name__ == "__main__":
    # Find optimal path using DFS
    path = DFS(MAZE, START, END)

    # If path not found, print message
    if path == -1:
        print(f"No path found from {START} to {END}.")

    # Else, if path found, print message
    else:
        print(f"Optimal path from {START} to {END} found in {path} steps.")