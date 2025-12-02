class Range:
    def __init__(self, range: str):
        self.range = range
        self.start, self.end = map(int, range.split("-"))

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return f"{self.start}-{self.end}"


def input_reader(file_path: str) -> list[Range]:
    with open(file_path, "r") as file:
        ranges: list[Range] = []
        for line in file:
            parts = [part.strip() for part in line.split(",") if part.strip()]
            ranges.extend(Range(part) for part in parts)
        return ranges
