from common import Range, input_reader


def is_number_invalid(number: int) -> bool:
    """Check if a number is invalid (made of a sequence repeated twice)."""
    str_number = str(number)
    length = len(str_number)
    if length % 2 != 0:
        return False
    half = length // 2
    first, second = str_number[:half], str_number[half:]
    if first.startswith("0"):
        return False
    return first == second


def solve(ranges: list[Range], verbose: bool = False) -> int:
    """Calculate sum of invalid numbers in ranges."""
    sum = 0
    for rng in ranges:
        for number in range(rng.start, rng.end + 1):
            if is_number_invalid(number):
                if verbose:
                    print(f"Invalid number: {number} in range {rng}")
                sum += number
    return sum


def main():
    from pathlib import Path

    script_dir = Path(__file__).parent
    ranges = input_reader(str(script_dir / "input.txt"))
    result = solve(ranges, verbose=True)
    print(f"Sum of invalid numbers: {result}")


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


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        main()
