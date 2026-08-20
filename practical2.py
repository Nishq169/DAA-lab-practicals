# =========================================================
# Search Algorithms in Python
# =========================================================

# =========================================================
# Linear Search
#
# Time Complexity:
# Best Case    : O(1)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(1)
# =========================================================
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# =========================================================
# Binary Search
#
# Note:
# Array must be sorted in ascending order.
#
# Time Complexity:
# Best Case    : O(1)
# Average Case : O(log n)
# Worst Case   : O(log n)
#
# Space Complexity:
# O(1)
# =========================================================
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ======================= Main =======================
def main():
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements:\n").split()))

    key = int(input("Enter element to search: "))

    print("\nSearch Algorithms")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        pos = linear_search(arr, key)

    elif choice == 2:
        pos = binary_search(arr, key)

    else:
        print("Invalid Choice")
        return

    if pos == -1:
        print("\nElement Not Found.")
    else:
        print(f"\nElement Found at Position {pos + 1}")


if __name__ == "__main__":
    main()