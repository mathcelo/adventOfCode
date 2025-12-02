from enum import Enum

MODULUS = 100


class Direction(Enum):
    L = "L"
    R = "R"


class Instruction:
    def __init__(self, direction: Direction, distance: int):
        self.direction = direction
        self.distance = distance


def instruction_parse(instruction: str) -> Instruction:
    direction = Direction(instruction[0])
    distance = int(instruction[1:])
    return Instruction(direction, distance)


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
    instructions = [instruction_parse(line) for line in open("document.txt")]
    print(solve(instructions))


if __name__ == "__main__":
    main()
