from common import MODULUS, Direction, Instruction, load_input


def count_zero_hits(start: int, end: int) -> int:
    """Count how many clicks land on 0 while moving from start to end."""
    if start == end:
        return 0

    if start < end:
        return end // MODULUS - start // MODULUS

    return (start - 1) // MODULUS - (end - 1) // MODULUS


def move(position: int, instruction: Instruction) -> tuple[int, int]:
    """Return (new_position, zero_hits) for a single rotation."""
    delta = (
        -instruction.distance
        if instruction.direction == Direction.L
        else instruction.distance
    )
    end_position = position + delta
    zero_hits = count_zero_hits(position, end_position)
    return end_position % MODULUS, zero_hits


def solve(instructions: list[Instruction]) -> int:
    position = 50
    zero_counter = 0
    for instruction in instructions:
        position, zero_hits = move(position, instruction)
        zero_counter += zero_hits
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
