def read_input(filepath: str) -> list[list[str]]:
    """Read input file and create an m×n matrix where each entry is a character."""
    matrix = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            if line:
                matrix.append(list(line))
    return matrix


def flow(matrix: list[list[str]]) -> int:
    """
    Simulate tachyon beam flow and count splits.
    Iterates through all rows. Beams move downward.
    """
    if not matrix:
        return 0

    m = len(matrix)
    n = len(matrix[0]) if matrix else 0

    # Find the starting position 'S'
    start_row = -1
    start_col = -1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "S":
                start_row = i
                start_col = j
                break
        if start_row != -1:
            break

    if start_row == -1:
        return 0

    # Create a copy to track beam positions (|)
    beam_matrix = [["." for _ in range(n)] for _ in range(m)]
    beam_matrix[start_row][start_col] = "|"  # Start the beam at S

    split_count = 0

    # Iterate through all rows from top to bottom
    for row in range(m):
        # Create a new state for this iteration
        new_beam_matrix = [row[:] for row in beam_matrix]

        for col in range(n):
            # If [m][n] == '^' and [m-1][n] == '|', create beams left and right
            if matrix[row][col] == "^" and row > 0 and beam_matrix[row - 1][col] == "|":
                if col > 0:
                    new_beam_matrix[row][col - 1] = "|"
                if col < n - 1:
                    new_beam_matrix[row][col + 1] = "|"
                split_count += 1
            # Else if [m][n] == '.' and [m-1][n] == '|', continue beam downward
            elif (
                matrix[row][col] == "." and row > 0 and beam_matrix[row - 1][col] == "|"
            ):
                new_beam_matrix[row][col] = "|"

        beam_matrix = new_beam_matrix

    return split_count


# Main execution
if __name__ == "__main__":
    matrix = read_input("input.txt")
    splits = flow(matrix)
    print(f"Number of splits: {splits}")
