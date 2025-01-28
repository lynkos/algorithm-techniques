def minimum_jumps(max_jumps):
    if len(max_jumps) == 1: return 0 # Only 1 element
    if max_jumps[0] == 0: return -1 # Cannot move forward from the first position

    jumps = 1
    current_end = farthest = max_jumps[0]

    for i in range(1, len(max_jumps)):
        # Update the farthest point reachable
        farthest = max(farthest, i + max_jumps[i])

        if i == current_end:
            if i == len(max_jumps) - 1: return jumps # Last index
            
            jumps += 1

            # Update next jump's range
            current_end = farthest 
            
            # If updated range >= last index
            if current_end >= len(max_jumps) - 1: return jumps

    return -1

# Example usage
if __name__ == "__main__":
    jumps = [ 2, 3, 1, 1, 4 ]
    output = minimum_jumps(jumps)
    print("Output:", "N/A" if output == -1 else output)