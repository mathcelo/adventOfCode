from typing import List, Tuple

def read_file(file: str) -> Tuple[List[List[int]], List[int]]:
    ranges: List[List[int]] = []
    ids: List[int] = []
    
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            
            if not line:
                continue
            elif "-" in line:
                lower, upper = line.split("-")
                ranges.append([int(lower), int(upper)])
            else:
                ids.append(int(line))
    
    return ranges, ids

def solve(ranges: List[List[int]], ids: List[int]) -> int:
    count = 0
    for id in ids:
        for rng in ranges:
            if rng[0] <= id <= rng[1]:
                count += 1
                break
    return count

ranges, ids = read_file("input.txt")
# ranges, ids = read_file("test-input.txt")
count = solve(ranges, ids)
print(count)


def solve2(ranges: List[List[int]]) -> int:
    if not ranges:
        return 0
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    # Merge overlapping ranges
    merged = [sorted_ranges[0]]
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:  # Overlapping or adjacent
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    # Count total IDs covered by merged ranges
    total = sum(rng[1] - rng[0] + 1 for rng in merged)
    return total

sum = solve2(ranges)
print(sum)

