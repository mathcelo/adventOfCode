from common import MODULUS, Direction, Instruction, load_input


def move(position: int, instruction: Instruction) -> int:
    if instruction.direction == Direction.L:
        return (position - instruction.distance) % MODULUS
    else:
        return (position + instruction.distance) % MODULUS


def solve(instructions: list[Instruction]) -> int:
    position = 50
    zero_counter = 0
    for instruction in instructions:
        position = move(position, instruction)
        if position == 0:
            zero_counter += 1
    return zero_counter


def main():
    from pathlib import Path

    script_dir = Path(__file__).parent
    instructions = load_input(str(script_dir / "input.txt"))
    print(solve(instructions))


def test():
    """Test with example input if test_input.txt exists."""
    from pathlib import Path

    script_dir = Path(__file__).parent
    try:
        instructions = load_input(str(script_dir / "test_input.txt"))
        result = solve(instructions)
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
