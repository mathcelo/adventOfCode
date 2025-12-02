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
    instructions = [instruction_parse(line) for line in open("document.txt")]
    print(solve(instructions))


if __name__ == "__main__":
    main()
