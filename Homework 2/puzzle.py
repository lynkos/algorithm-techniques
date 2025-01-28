from heapq import heappush, heappop
from copy import deepcopy

def h(state: list[list[int]], goal: list[list[int]]) -> int:
    """
    Calculate the Manhattan distance heuristic = summation of abs(x1 - x2) + abs(y1 - y2) for each tile.

    Args:
        state (list[list[int]]): Current state of the puzzle.
        goal (list[list[int]]): Goal state of the puzzle.

    Returns:
        int: Manhattan distance heuristic.
    """
    # Initialize total Manhattan distance
    distance = 0

    # Calculate Manhattan distance for each tile
    for i in range(len(state)):
        for j in range(len(state[0])):
            # If current tile's state is valid and not blank
            if (state[i][j] != goal[i][j]) and (state[i][j] != 0):
                # Calculate Manhattan distance
                goal_x, goal_y = next((x, y) for x, row in enumerate(goal) for y, val in enumerate(row) if val == state[i][j])
                distance += abs(goal_x - i) + abs(goal_y - j)

    # Return total Manhattan distance
    return distance

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

def get_neighbors(state: list[list[int]]) -> list[list[list[int]]]:
    """
    Generate all possible moves (i.e. neighbors) from the current state.

    Args:
        state (list[list[int]]): Puzzle's current state.

    Returns:
        list[list[list[int]]]: List of all possible moves.
    """
    # Initialize neighbors list
    neighbors = [ ]

    # Find the blank tile (i.e. 0) in the current state
    x, y = next((i, j) for i, row in enumerate(state) for j, val in enumerate(row) if val == 0)

    # Explore all neighbors in all horizontal and vertical directions
    for dx, dy in [ (-1, 0), (1, 0), (0, -1), (0, 1) ]:
        # Calculate neighbor position (i.e. x-coordinates and y-coordinates)
        nx, ny = x + dx, y + dy

        # If neighbor is valid (i.e. within bounds)
        if within_bounds(state, nx, ny):
            # Swap blank tile with neighbor tile
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            
            # Add new state to the neighbors list
            neighbors.append(new_state)

    # Return list of neighbors (i.e. all possible moves for current state)
    return neighbors

def a_star(start: list[list[int]], goal: list[list[int]]) -> list | int:
    """
    A* search algorithm to find the shortest path from the start state to the goal state.

    Args:
        start (list[list[int]]): Start state of the puzzle.
        goal (list[list[int]]): Goal state of the puzzle.

    Returns:
        list | int: List of steps to reach the goal state, else -1 if no path found.
    """
    # Initialize priority queue
    priority_queue = [ ]

    # Initialize visited set
    visited = set()

    # Initialize g_score where g_score[start] = 0
    g_score = { str(start): 0 }

    # Initialize dict f_score where f_score[start] = h(start, goal)
    f_score = { str(start): h(start, goal) }

    # Initialize a came_from to track the path
    came_from = { }

    # Add start to priority_queue with priority f_score[start]
    heappush(priority_queue, (f_score[str(start)], start))

    # While priority queue is not empty
    while priority_queue:
        # Get the node in priority_queue with lowest f_score
        _, current = heappop(priority_queue)

        # If puzzle's complete (i.e. its current state is the goal state)
        if current == goal:
            path = [ ]

            # Reconstruct path
            while str(current) in came_from:
                path.append(current)
                current = came_from[str(current)]

            # Reverse path for correct order (i.e. start to goal)
            path.reverse()

            # Return path
            return path

        # Mark current as visited
        visited.add(str(current))

        # For each neighbor of current
        for neighbor in get_neighbors(current):
            # Check if the neighbor is valid
            if str(neighbor) not in visited:
                # Each move costs 1
                curr_g_score = g_score[str(current)] + 1

                if str(neighbor) not in visited or curr_g_score < g_score[str(neighbor)]:
                    # This path to neighbor is better, so record it
                    came_from[str(neighbor)] = current
                    g_score[str(neighbor)] = curr_g_score

                    # f(n) = g(n) + h(n)
                    f_score[str(neighbor)] = curr_g_score + h(neighbor, goal)

                    # Add neighbor to priority_queue, if applicable
                    if neighbor not in priority_queue:
                        heappush(priority_queue, (f_score[str(neighbor)], neighbor))

    # Return -1 if no path found
    return -1

if __name__ == "__main__":
    # Puzzle's start state
    puzzle_start = [
        [0, 2, 4],
        [6, 1, 3],
        [7, 8, 5]
    ]

    # Puzzle's goal state
    puzzle_goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # Find the shortest path from start to goal using A*
    path = a_star(puzzle_start, puzzle_goal)

    # If no path found, print message
    if path == -1: print("No path found")

    # Else, print path
    else:
        # type: ignore included in the next line to suppress error message
        for step in path: # type: ignore
            for row in step:
                print(row)
            print()