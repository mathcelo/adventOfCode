def read_input(filepath: str) -> tuple[list[list[int]], list[str]]:
    """Read numbers and operators from input file."""
    numbers = []
    operators = []

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if parts[0].isdigit():
                numbers.append(list(map(int, parts)))
            else:
                operators = parts

    return numbers, operators


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


def solve(numbers: list[list[int]], operators: list[str]) -> int:
    """Process each column with its corresponding operator, then sum all results."""
    results = []
    num_columns = len(numbers[0]) if numbers else 0

    for col_idx in range(num_columns):
        column = [row[col_idx] for row in numbers]
        operator = operators[col_idx]
        result = math(column, operator)
        results.append(result)

    return math(results, "+")


# Main execution
numbers, operators = read_input("input.txt")
answer = solve(numbers, operators)
print(f"Answer: {answer}")
