# =========================================================
# Graph Traversal using DFS and BFS
# =========================================================

from collections import deque

# =========================================================
# Depth First Search (DFS)
#
# Time Complexity:
# Best Case    : O(V + E)
# Average Case : O(V + E)
# Worst Case   : O(V + E)
#
# Space Complexity:
# O(V)
#
# Where:
# V = Number of Vertices
# E = Number of Edges
# =========================================================
def dfs(graph, visited, v, n):
    visited[v] = True
    print(v, end=" ")

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, visited, i, n)


# =========================================================
# Breadth First Search (BFS)
#
# Time Complexity:
# Best Case    : O(V + E)
# Average Case : O(V + E)
# Worst Case   : O(V + E)
#
# Space Complexity:
# O(V)
#
# Where:
# V = Number of Vertices
# E = Number of Edges
# =========================================================
def bfs(graph, visited, start, n):
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


# ======================= Main =======================
def main():
    n = int(input("Enter number of vertices: "))

    print("Enter Adjacency Matrix:")
    graph = []

    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    start = int(input("Enter starting vertex: "))

    print("\n1. DFS")
    print("2. BFS")

    choice = int(input("\nEnter your choice: "))

    visited = [False] * n

    if choice == 1:
        print("\nDFS Traversal:", end=" ")
        dfs(graph, visited, start, n)

    elif choice == 2:
        print("\nBFS Traversal:", end=" ")
        bfs(graph, visited, start, n)

    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()