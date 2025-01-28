# Algorithm Techniques
Solutions to assignments for COP 4534.

## Backtracking
### 4 Queens Problem
#### Usage
```bash
python brute_force.py
```

#### Complexity
* Time Complexity: $O(N^N)$
* Space Complexity: $O(N)$

### 4 Queens Problem using Recursion
#### Usage
```bash
python recursion.py
```

#### Complexity
* Time Complexity: $O(N!)$
* Space Complexity: $O(N)$

### Eight Numbers in a Cross-shape board
#### Usage
```bash
python eight_numbers.py
```

#### Complexity
* Time Complexity: $O(N!)$
* Space Complexity: $O(N)$

## Graph Algorithms
### Depth First Search (DFS)
#### Usage
```bash
python dfs.py
```

#### Pseudocode
```
Algorithm DFS(grid, start, end):
    Input:
        grid: 2D maze composed of 0s and 1s, with the former indicating a walkable path and the latter indicating a wall.
        start: Starting point coordinates (i.e. xi, yi).
        goal: Ending point coordinates (i.e. xj, yj).
    Output:
        Shortest path from start to goal, if it exists. Else, no path exists.

    initialize a stack S
    initialize a 2D array ‘visited’ with False values
    add starting coordinates and steps (xi, yi, 0) to S
    initialize min_steps with infinity (i.e. min_steps == inf)
    initialize found with False (i.e. found = False)

    while S is not empty:
        (xk, yk, steps) = S.pop()

        if goal is reached (i.e. (xk, yk) == (xj, yj)):
            min_steps = min(min_steps, steps)
            found = True
            continue

        mark (xk, yk) as visited

        for each neighboring coordinate (dx, dy) (i.e. north, south, east, and west of xk, yk):
            get neighbor’s coordinates (nx, ny)
            if (nx, ny) is within grid bounds AND grid[nx][ny] == 0 (i.e. not blocked) AND visited[nx][ny] == False (i.e. unvisited coordinate):
                Add (nx, ny, steps + 1) to S

    return min_steps if goal is reached (i.e. found = True), else return -1 (i.e. no solution)
```

### Breadth First Search (BFS)
#### Usage
```bash
python bfs.py
```

#### Pseudocode
```
Algorithm BFS(grid, start, end):
    Input:
        grid: 2D maze composed of 0s and 1s, with the former indicating a walkable path and the latter indicating a wall.
        start: Starting point coordinates (i.e. xi, yi).
        end: Ending point coordinates (i.e. xj, yj).
    Output:
        Shortest path from start to goal, if it exists. Else, no path exists.

    initialize a queue Q
    initialize a 2D array ‘visited’ with False values
    add starting coordinates and steps (xi, yi, 0) to Q
    mark starting point as visited (i.e. visited[xi][yi] = True)

    while Q is not empty:
        (xk, yk, steps) = Q.dequeue()

        If goal is reached (i.e. (xk, yk) == (xj, yj)):
            return steps

        for each neighboring coordinate (dx, dy) (i.e. north, south, east, and west of xk, yk):
            get neighbor’s coordinates (nx, ny)
            if (nx, ny) is within grid bounds AND grid[nx][ny] == 0 (i.e. not blocked) AND visited[nx][ny] == False (i.e. unvisited coordinate):
                mark (nx, ny) as visited (i.e. visited[nx][ny] == True)
                Add (nx, ny, steps + 1) to Q

    return -1 if goal is not reached
```

## Homework 2
### Number of Islands
#### Usage
```bash
python islands.py
```

#### Pseudocode
```
Algorithm count_islands(map):
    Input:
        map: 2D map composed of 0s and 1s, with the former indicating water and the latter being land.
    Output:
        Number of islands counted (i.e. non-negative integer).

    return 0 if map is empty or invalid (i.e. not 2D array)
    initialize a counter with 0 to keep track of island count (i.e. counter = 0)

    traverse the map both horizontally and vertically (via double for-loop) to check each coordinate i, j:
        if land is detected (i.e. map[i][j] == 1)
            increment the counter by 1 (i.e. counter += 1)
            use BFS on map and current coordinates (i.e. BFS(map, i, j))
```

#### Complexity
$M$ = Number of rows, $N$ = Number of columns
* Time Complexity: $O(M * N)$
* Space Complexity: $O(M * N)$

### 8-Puzzle Games
#### Usage
```bash
python puzzle.py
```

#### Pseudocode
```
Algorithm AStar(start, goal):
    Input:
        start: The starting state of the puzzle.
        goal: The goal state of the puzzle.
    
    Output:
        -1 if no path is found, else a list of steps to take for the shortest path from start to goal.

    initialize priority queue
    initialize visited
    initialize g_score[start] = 0
    initialize f_score[start] = Manhattan distance heuristic from start to goal
    initialize came_from to track path
    add start to priority_queue with priority f_score[start]

    while priority_queue is not empty:
        get node in priority_queue with lowest f-score

        if goal is found:
            return path

        mark node as visited

        for each of node’s neighbors:
            increment current g_score by 1
        
            if neighbor is unvisited or its g_score is greater than the current g_score:
                record the neighbor’s path in came_from
                update neighbor’s g_score (i.e. g_score[neighbor] = current g_score)

                calculate neighbor’s f_score (i.e. f_score[neighbor] = current g_score + Manhattan distance of neighbor and goal)

                add neighbor and its f_score to priority_queue, if not already there
```

#### Complexity
$b$ = Branching factor, $d$ = Number of nodes
* Time Complexity: $O(b^d)$
* Space Complexity: $O(b^d)$

## Homework 3
### Dijkstra's Algorithm
#### Usage
```bash
python dijkstra.py
```

#### Pseudocode
```
Algorithm Dijkstra(graph, source, target):
    Input:
        graph: Directed and weighted graph containing N vertices
        source: Starting vertex.
        target: Ending vertex.
    Output:
        Shortest distance (dist) from source to target.

    for each vertex v in graph:
        dist[v] = ∞
        prev[v] = None
    dist[source] = 0

    Create priority queue Q
    Insert source into Q

    while Q is not empty:
        dist_so_far, u = Q.pop()
        if dist_so_far > dist[u]:
            continue

        for each (v, weight) in graph[u]:
            if dist[u] + weight(u, v) < dist[v]:
                dist[v] = dist[u] + weight(u, v)
                prev[v] = u
                push v into the Q

    path = [ ]

    while current is not null:
        insert current at the beginning of path
        current = prev[current]

    return path
```

#### Complexity
$V$ = Vertex, $E$ = Edge
* Time Complexity: $O((V + E) \log V)$
* Space Complexity: $O(V + E)$

### Huffman Coding
#### Usage
```bash
python huffman.py
```

#### Pseudocode
```
Algorithm HuffmanCoding(characters, frequencies):
    Input:
        characters[1..n]: List of characters.
        frequencies[1..n]: Corresponding frequencies.
    Output:
        Huffman codes for each character.

    create a min-heap Q containing all nodes (each character and its frequency).

    while Q has more than one node:
        extract two nodes x and y with the smallest frequencies from Q.
        create a new internal node z with frequency z.freq = x.freq + y.freq.
        set z.left = x, z.right = y.
        insert z back into Q.

    the remaining node in Q is the root of the Huffman tree.

    traverse the Huffman tree to assign codes to characters:
        assign '0' to a left edge and '1' to a right edge.
        for each leaf node (character), record the path from the root as its code.
    
    return the codes for each character.
```

### Minimum Number of Jumps to Reach the End
#### Usage
```bash
python jumps.py
```

#### Pseudocode
```
Algorithm MinJumps(max_jumps):
    Input:
        max_jumps [1..n]: Array of positive integers where each element represents the maximum number of steps.
    Output:
        Minimum number of jumps required to reach the end of the array (starting at index 0).
    
    if max_jumps only has 1 element:
        return 0

    if unable to move from start (i.e. index 0):
        return -1

    initialize jump to 1
    set current_end and farthest to 1st element in max_jumps

    for each val in max_jumps:
        update farthest with current farthest value
        
        if current index equals current_end:
            if current_end is last index:
                return jumps
            increment jumps by 1
            set current_end equal to farthest
            if current_end is greater than or equal to the last index:
                return jumps
    return -1
```

#### Complexity
$n$ = Array length
* Time Complexity: $O(n)$
* Space Complexity: $O(1)$

### Job Scheduling with Deadlines
#### Usage
```bash
python jobs.py
```

#### Pseudocode
```
Algorithm JobScheduling(jobs):
    Input:
        jobs[1..n]: List of jobs.
    Output:
        Max profit from optimized job scheduling.

    sort jobs by profit in descending order.
    create min-heap Q to track scheduled jobs.

    for each job in jobs:
        if heap has space:
            push job to Q
        else if heap is full and job has a higher profit than any job in Q:
            replace the latter with the former
        calculate total profit by summing the profits of all jobs in Q

    return the total profit
```

#### Complexity
$n$ = Number of jobs
* Time Complexity: $O(n \log n)$
* Space Complexity: $O(n)$