from operator import le


def input_reader(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        batteries: list[int] = []
        for line in file:
            batteries.append((line.strip()))
        return batteries


def solve(batteries: list[str], verbose: bool = False) -> int:
    sum = 0
    for battery in batteries:
        max_index = max_number(battery[:-1])

        remaining = battery[max_index + 1 :]
        second_max_index = max_index + 1 + max_number(remaining)

        str_battery = battery[max_index] + battery[second_max_index]
        sum += int(str_battery)

    return sum


def max_number(battery: str) -> int:

    length = len(battery)
    max_number = battery[0]
    max_index = 0
    for i in range(length):
        if battery[i] > max_number:
            max_number = battery[i]
            max_index = i
    return max_index


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
