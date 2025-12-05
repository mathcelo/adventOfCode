def input_reader(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        batteries: list[str] = []
        for line in file:
            batteries.append(line.strip())
        return batteries


def largest_12_digit_number(s: str) -> str:
    """Find the largest 12-digit number by selecting 12 characters from a string."""
    if len(s) < 12:
        raise ValueError("String must have at least 12 characters")

    result = []
    to_drop = len(s) - 12  # How many characters we need to drop

    for digit in s:
        while result and result[-1] < digit and to_drop > 0:
            result.pop()
            to_drop -= 1
        result.append(digit)

    return "".join(result[:12])


def solve(batteries: list[str], verbose: bool = False) -> int:
    sum = 0
    for battery in batteries:
        if len(battery) >= 12:
            subsequence = largest_12_digit_number(battery)
            sum += int(subsequence)
    return sum


def test():
    """Test with example input if test_input.txt exists."""
    from pathlib import Path

    script_dir = Path(__file__).parent
    try:
        ranges = input_reader(str(script_dir / "test_input.txt"))
        result = solve(ranges, verbose=False)
        print(f"Test result: {result}")
        return result
    except FileNotFoundError:
        print("test_input.txt not found, skipping test")
        return None


def main():
    """Test with example input if test_input.txt exists."""
    from pathlib import Path

    script_dir = Path(__file__).parent
    ranges = input_reader(str(script_dir / "input.txt"))
    result = solve(ranges, verbose=True)
    print(f"Sum of batteries: {result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        main()
