def read_input(filepath: str) -> list[list[str]]:
    """Read input file and create an m×n matrix where each entry is a character."""
    matrix = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            if line:
                matrix.append(list(line))
    return matrix


def count_paths_from(matrix: list[list[str]], row: int, col: int, memo: dict) -> int:
    """Recursively count all paths from position (row, col) to the bottom using memoization."""
    m = len(matrix)
    n = len(matrix[0]) if matrix else 0

    # Check memo first
    if (row, col) in memo:
        return memo[(row, col)]

    # Base case: reached beyond the bottom of the matrix
    if row >= m:
        return 1  # This is one complete path

    # Out of bounds horizontally
    if col < 0 or col >= n:
        return 0

    cell = matrix[row][col]
    result = 0

    if cell == "^":
        # Splitter: count paths going left AND right
        left_paths = count_paths_from(matrix, row + 1, col - 1, memo)
        right_paths = count_paths_from(matrix, row + 1, col + 1, memo)
        result = left_paths + right_paths

    elif cell == "." or cell == "S":
        # Empty space or start: continue straight down
        result = count_paths_from(matrix, row + 1, col, memo)

    else:
        # Unknown cell type or obstacle
        result = 0

    # Store in memo
    memo[(row, col)] = result
    return result


def count_quantum_timelines(matrix: list[list[str]]) -> int:
    """Count the number of quantum timelines (all possible paths through the manifold)."""
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0]) if matrix else 0

    # Memoization dictionary
    memo = {}

    # Find the starting position 'S'
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "S":
                return count_paths_from(matrix, i, j, memo)

    return 0


# Main execution
if __name__ == "__main__":
    matrix = read_input("input.txt")
    quantum_timelines = count_quantum_timelines(matrix)
    print(f"Number of quantum timelines: {quantum_timelines}")
