def read_input(filepath: str) -> tuple[list[list[int | None]], list[str]]:
    """Read digit grid and operators from input file."""
    digit_rows = []
    operators = []

    with open(filepath, "r") as file:
        for line in file:
            if not line.strip():
                continue

            if any(op in line for op in ["+", "*"]):
                operators = [char for char in line.strip() if char in "+*"]
            else:
                digits = []
                for char in line.rstrip("\n"):
                    if char.isdigit():
                        digits.append(int(char))
                    elif char == " ":
                        digits.append(None)

                if digits:
                    digit_rows.append(digits)

    return digit_rows, operators


def math(numbers: list[int], operator: str) -> int:
    """Perform addition (+) or multiplication (*) on a list of numbers."""
    if not numbers:
        return 0

    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        raise ValueError(f"Unsupported operator: {operator}. Use '+' or '*'")


def solve_part2(digit_rows: list[list[int | None]], operators: list[str]) -> int:
    """Solve part 2: Read columns right-to-left, build numbers top-to-bottom, group by space columns, and calculate."""
    if not digit_rows:
        return 0

    num_columns = max(len(row) for row in digit_rows)
    num_rows = len(digit_rows)

    # Process columns from right to left
    problem_groups = []
    current_group = []

    for col_idx in range(num_columns - 1, -1, -1):
        # Check if this column is all spaces (separates problems)
        # Note: operator row is the last row, so we exclude it when reading digits
        is_space_column = True
        column_digits = []

        for row_idx in range(num_rows):  # All rows in digit_rows are digit rows
            if col_idx < len(digit_rows[row_idx]):
                cell = digit_rows[row_idx][col_idx]
                if cell is not None:
                    is_space_column = False
                    column_digits.append(str(cell))

        if is_space_column:
            # This is a separator column - finish current problem
            if current_group:
                problem_groups.append(current_group)
                current_group = []
        else:
            # This column has digits - build number from top to bottom
            if column_digits:
                number = int("".join(column_digits))
                current_group.append(number)

    # Don't forget the last group
    if current_group:
        problem_groups.append(current_group)

    # Calculate each problem with its operator
    # Operators are read left-to-right, but problems are read right-to-left,
    # so we need to reverse the operators to match
    operators_reversed = list(reversed(operators))
    problem_results = []
    for idx, group in enumerate(problem_groups):
        if idx < len(operators_reversed):
            operator = operators_reversed[idx]
            result = math(group, operator)
            problem_results.append(result)

    # Sum all problem results
    return sum(problem_results)


# Main execution
if __name__ == "__main__":
    digit_rows, operators = read_input("input.txt")
    answer = solve_part2(digit_rows, operators)
    print(f"Answer: {answer}")
