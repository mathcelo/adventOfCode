import math
from collections import defaultdict


class UnionFind:
    """Union-Find data structure for tracking connected components."""

    def __init__(self, n):
        """Initialize Union-Find with n elements."""
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        """Find the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union two elements, returns True if successfully connected."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Union by size
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True  # Successfully connected

    def num_components(self):
        """Return the number of connected components."""
        roots = set()
        for i in range(len(self.parent)):
            roots.add(self.find(i))
        return len(roots)


def distance_3d(p1, p2):
    """Calculate Euclidean distance between two 3D points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def read_points(filename):
    """Read junction box positions from file, returning list of [x, y, z] coordinates."""
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                coords = list(map(int, line.split(",")))
                points.append(coords)
    return points


def solve_until_connected(points):
    """Connect closest pairs until all boxes are in one circuit, return product of X coordinates of last connection."""
    n = len(points)

    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance_3d(points[i], points[j])
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Use Union-Find to track circuits
    uf = UnionFind(n)

    # Keep connecting until all boxes are in one circuit
    last_connection = None
    for dist, i, j in distances:
        # Try to connect (will return False if already in same circuit)
        if uf.union(i, j):
            # This was a successful connection
            # Check if we now have only one component
            if uf.num_components() == 1:
                # This is the last connection that made everything connected
                last_connection = (i, j)
                break

    if last_connection is None:
        return 0

    # Multiply X coordinates of the last two boxes
    i, j = last_connection
    result = points[i][0] * points[j][0]
    return result


if __name__ == "__main__":
    # Read points from file
    points = read_points("input.txt")

    print(f"Read {len(points)} junction boxes")

    # Connect until all are in one circuit
    result = solve_until_connected(points)
    print(f"Product of X coordinates of last connection: {result}")

