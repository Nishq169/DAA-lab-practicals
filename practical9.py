# =========================================================
# Prim's Algorithm (Minimum Spanning Tree)
#
# Time Complexity:
# Best Case    : O(V^2)
# Average Case : O(V^2)
# Worst Case   : O(V^2)
#
# Space Complexity:
# O(V^2)
#
# Where:
# V = Number of Vertices
#
# Note:
# Finds the Minimum Spanning Tree (MST) of a
# connected weighted graph.
# =========================================================

INF = float('inf')


def prim_mst(graph, n):
    selected = [False] * n
    selected[0] = True       # Start from vertex 0

    edge_count = 0
    total_cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    while edge_count < n - 1:
        minimum = INF
        x = -1
        y = -1

        # Find the minimum-cost edge
        # from selected vertex to unselected vertex
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

        # If no edge is found, graph is disconnected
        if x == -1 or y == -1:
            print("\nGraph is not connected.")
            return

        print(f"{x} --> {y}  Cost = {graph[x][y]}")

        total_cost += graph[x][y]
        selected[y] = True
        edge_count += 1

    print(f"\nMinimum Cost = {total_cost}")


# ======================= Main =======================

def main():
    n = int(input("Enter number of vertices: "))

    print("Enter Cost Adjacency Matrix:")

    graph = []

    for i in range(n):
        row = list(map(int, input().split()))

        # Replace 0 (no edge) with INF
        # Diagonal is also kept as INF
        for j in range(n):
            if row[j] == 0:
                row[j] = INF

        graph.append(row)

    prim_mst(graph, n)


if __name__ == "__main__":
    main()