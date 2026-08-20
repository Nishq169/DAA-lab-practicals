# =========================================================
# 0/1 Knapsack using Dynamic Programming
#
# Time Complexity:
# Best Case    : O(n * W)
# Average Case : O(n * W)
# Worst Case   : O(n * W)
#
# Space Complexity:
# O(n * W)
#
# Where:
# n = Number of items
# W = Maximum capacity of knapsack
# =========================================================

def knapsack(wt, val, n, W):
    # Create DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill DP Table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# ======================= Main =======================
def main():
    n = int(input("Enter number of items: "))

    wt = list(map(int, input("Enter weights:\n").split()))
    val = list(map(int, input("Enter values:\n").split()))

    W = int(input("Enter knapsack capacity: "))

    print("\nMaximum Profit =", knapsack(wt, val, n, W))


if __name__ == "__main__":
    main()