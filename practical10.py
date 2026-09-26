# =========================================================
# Kruskal's Algorithm (Minimum Spanning Tree)
#
# Time Complexity:
# Best Case    : O(E log E)
# Average Case : O(E log E)
# Worst Case   : O(E log E)
#
# Space Complexity:
# O(V + E)
#
# Where:
# V = Number of Vertices
# E = Number of Edges
#
# Note:
# Finds the Minimum Spanning Tree (MST)
# using Greedy Approach.
# =========================================================


# ======================= Edge Class =======================

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


# ======================= Find Parent =======================

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


# ======================= Union of Sets =======================

def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    # Union by rank
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b

    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a

    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return True


# ======================= Main =======================

def main():

    vertices = int(input("Enter number of vertices: "))
    edges_count = int(input("Enter number of edges: "))

    edges = []

    print("\nEnter Source Destination Weight:")

    for i in range(edges_count):

        u, v, w = map(int, input().split())

        # Check valid vertices
        if u < 0 or u >= vertices or v < 0 or v >= vertices:
            print("Invalid vertex number!")
            return

        edges.append(Edge(u, v, w))

    # Initialize parent and rank
    parent = [i for i in range(vertices)]
    rank = [0] * vertices

    # Sort edges according to weight
    edges.sort(key=lambda edge: edge.w)

    total_cost = 0
    edge_count = 0

    print("\nEdges in Minimum Spanning Tree:")

    # Process edges
    for edge in edges:

        if union(parent, rank, edge.u, edge.v):

            print(
                f"{edge.u} --> {edge.v}  Cost = {edge.w}"
            )

            total_cost += edge.w
            edge_count += 1

            # MST contains V - 1 edges
            if edge_count == vertices - 1:
                break

    # Check if MST is possible
    if edge_count != vertices - 1:
        print("\nGraph is not connected.")
        return

    print(f"\nMinimum Cost = {total_cost}")


# ======================= Program Start =======================

if __name__ == "__main__":
    main()