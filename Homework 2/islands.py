from collections import deque

def within_bounds(map: list[list[int]], x: int, y: int) -> bool:
    """
    Check if a given coordinate is within the bounds of the map.

    Args:
        map (list[list[int]]): Map to check against.
        x (int): X-coordinate to check.
        y (int): Y-coordinate to check.

    Returns:
        bool: True if (x, y) is within the bounds of map, else False.
    """
    return (0 <= x < len(map)) and (0 <= y < len(map[0]))

def is_valid(map: list[list[int]], x: int, y: int) -> bool:
    """
    Check if a given coordinate is valid in a given map.

    Args:
        map (list[list[int]]): Map to validate.
        x (int): X-coordinate to check.
        y (int): Y-coordinate to check.

    Returns:
        bool: True if (x, y) is valid, else False.
    """
    # Check if the coordinate is within the bounds of the map and is land
    return (within_bounds(map, x, y)) and (map[x][y] == 1)

def count_islands(map: list[list[int]]) -> int:
    """
    Count the number of islands in a given map using BFS.

    Args:
        map (list[list[int]]): Map to traverse.

    Returns:
        int: Number of counted islands in the map.
    """
    # If map is empty or not a 2D array (i.e. no xy-coordinates), return 0
    if not map or not map[0]: return 0

    # Initialize counter to keep track of number of islands
    counter = 0

    # Traverse map horizontally
    for i in range(len(map)):
        # Traverse map vertically
        for j in range(len(map[0])):
            # If land is found
            if map[i][j] == 1:
                # Increment counter
                counter += 1

                # Submerge adjacent land
                BFS(map, i, j)
                
    # Return number of islands
    return counter
    
def BFS(map: list[list[int]], i: int, j: int):
    """
    Given the map and starting position, submerge adjacent land using BFS.

    Args:
        map (list[list[int]]): Map to traverse.
        i (int): X-coordinate of the starting position.
        j (int): Y-coordinate of the starting position.
    """
    # Initialize queue with starting position
    queue = deque( [ (i, j) ] )

    map[i][j] = 0

    # While queue is not empty
    while queue:
        # Dequeue current position
        x, y = queue.popleft()

        # Explore all neighbors in all horizontal and vertical directions
        for dx, dy in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
            # Calculate neighbor position (i.e. x-coordinates and y-coordinates)
            nx, ny = x + dx, y + dy

            # Check if the neighbor is valid (i.e. within bounds and is land)
            if is_valid(map, nx, ny):
                # Add to queue
                queue.append((nx, ny))
                
                map[nx][ny] = 0
                
if __name__ == "__main__":
    matrix = [ 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
            ]
    
    # Count number of islands using BFS
    numIslands = count_islands(matrix)

    # If no islands counted, print message
    if numIslands == 0:
        print(f"No islands found in given map.")

    # Else if 1 island counted, print message
    elif numIslands == 1:
        print(f"{numIslands} island found in given map.")

    # Else (if several islands counted), print message
    else:
        print(f"{numIslands} islands found in given map.")
