class Range:
    def __init__(self, range: str):
        self.range = range
        self.start, self.end = map(int, range.split("-"))

    def __str__(self):
        return f"{self.start}-{self.end}"

    def __repr__(self):
        return f"{self.start}-{self.end}"


def input_reader(file_path: str) -> list[Range]:
    with open(file_path, "r") as file:
        ranges: list[Range] = []
        for line in file:
            parts = [part.strip() for part in line.split(",") if part.strip()]
            ranges.extend(Range(part) for part in parts)
        return ranges


def is_number_invalid(number: int) -> bool:
    str_number = str(number)
    length = len(str_number)
    if length % 2 != 0:
        return False
    half = length // 2
    first, second = str_number[:half], str_number[half:]
    if first.startswith("0"):
        return False
    return first == second


def maxCommStr(s1: str, s2: str) -> str:
    m = len(s1)
    n = len(s2)

    # Create a table to store lengths of longest
    # common suffixes of substrings.
    LCSuf = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_idx_s1 = 0

    # Build LCSuf[m+1][n+1] in bottom-up fashion.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                LCSuf[i][j] = LCSuf[i - 1][j - 1] + 1
                if LCSuf[i][j] > max_len:
                    max_len = LCSuf[i][j]
                    end_idx_s1 = i
            else:
                LCSuf[i][j] = 0

    if max_len == 0:
        return ""
    return s1[end_idx_s1 - max_len : end_idx_s1]


def main():
    ranges = input_reader("input.txt")
    sum = 0
    for rng in ranges:
        for number in range(rng.start, rng.end + 1):
            if is_number_invalid(number):
                print(f"Invalid number: {number} in range {rng}")
                sum += number
    print(f"Sum of invalid numbers: {sum}")


if __name__ == "__main__":
    main()
