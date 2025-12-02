# Advent of Code Solutions

This repository contains my solutions to [Advent of Code](https://adventofcode.com/) problems.

## Structure

Each day's solution follows a consistent structure:

```
2025/
  XX/
    input.txt          # Main puzzle input
    test_input.txt     # Example/test input (optional)
    part1.py           # Solution for part 1
    part2.py           # Solution for part 2
```

## Running Solutions

### Using `uv` (recommended):
```bash
cd 2025/XX
uv run part1.py
uv run part2.py
```

### Run with test input:
```bash
cd 2025/XX
uv run part1.py test
uv run part2.py test
```

### Alternative: Using Python directly:
```bash
cd 2025/XX
python3 part1.py
python3 part2.py
```

## Setup

### Using `uv` (recommended):
```bash
uv sync
```

### Alternative: Using pip:
```bash
pip install -e ".[dev]"
```

## Testing

Run tests with pytest:
```bash
uv run pytest
# or
pytest
```
