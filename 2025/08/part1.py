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

    def get_component_sizes(self):
        """Return list of sizes of all connected components."""
        components = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            components[root] = self.size[root]
        return list(components.values())


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


def solve(points, num_connections=1000):
    """Connect num_connections closest pairs and return product of three largest circuit sizes."""
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

    # Make connections - process num_connections pairs (even if some are already connected)
    connections_attempted = 0
    for dist, i, j in distances:
        # Try to connect (will return False if already in same circuit)
        uf.union(i, j)
        connections_attempted += 1
        if connections_attempted == num_connections:
            break

    # Get circuit sizes
    sizes = sorted(uf.get_component_sizes(), reverse=True)

    # Multiply the three largest
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
    else:
        result = 0

    return result


if __name__ == "__main__":
    # Read points from file
    points = read_points("test.txt")

    print(f"Read {len(points)} junction boxes")

    # Make 1000 connections
    result = solve(points, num_connections=1000)
    print(f"Result after 1000 connections: {result}")
