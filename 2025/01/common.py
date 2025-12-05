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


def load_input(file_path: str) -> list[Instruction]:
    """Load instructions from input file."""
    with open(file_path, "r") as f:
        return [instruction_parse(line.strip()) for line in f if line.strip()]
