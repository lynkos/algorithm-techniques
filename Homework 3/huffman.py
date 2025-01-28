from heapq import heapify, heappop, heappush

class HuffmanNode:
    def __init__(self, freq, char = None, left = None, right = None):
        self.freq = freq # Frequency of the character
        self.char = char # Character (None for internal nodes)
        self.left = left # Left child
        self.right = right # Right child

    # Define comparison operators for the priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(characters, frequencies):
    # Create a priority queue (min-heap) with leaf nodes for each character
    heap = [ HuffmanNode(freq, char) for char, freq in zip(characters, frequencies) ]
    heapify(heap)
    
    # Build the Huffman tree
    while len(heap) > 1:
        # Extract two nodes with the smallest frequencies
        left = heappop(heap)
        right = heappop(heap)

        # Create a new internal node with these two nodes as children
        merged = HuffmanNode(left.freq + right.freq, left = left, right = right)

        # Add the new node to the heap
        heappush(heap, merged)

    # The remaining node is the root of the Huffman tree
    root = heap[0]
    
    # Traverse the Huffman tree to assign codes
    codes = { }

    def assign_codes(node, code):
        if node.char is not None:
            # It's a leaf node, assign the code
            codes[node.char] = code
            return

        # Traverse left and right children
        if node.left: assign_codes(node.left, code + '0')
        if node.right: assign_codes(node.right, code + '1')

    assign_codes(root, '')
    
    return codes

# Example usage
if __name__ == "__main__":
    characters = [ 'A', 'B', 'C', 'D', 'E' ]
    frequencies = [ 10, 15, 30, 40, 5 ]
    
    codes = huffman_coding(characters, frequencies)
    
    print("Huffman Codes:")
    for i in range(len(characters)):
        char = characters[i]
        huffman_code = codes[char]
        
        # Total Cost = Frequency * Length of Huffman Code
        total_cost = frequencies[i] * len(huffman_code)
        
        print(f"Character: {char}, Code: {huffman_code}, Total Cost: {total_cost}")