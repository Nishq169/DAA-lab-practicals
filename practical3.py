# =========================================================
# Heap Sort (Max Heap)
#
# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)
#
# Space Complexity:
# O(1)
#
# Note:
# Heap Sort first builds a Max Heap and then repeatedly
# swaps the root (largest element) with the last element.
# =========================================================

# Function to heapify a subtree
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Heap Sort Function
def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Display Array
def print_array(arr):
    print("\nSorted Array:")
    print(*arr)


# Main Function
def main():
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements:\n").split()))

    heap_sort(arr)

    print_array(arr)


if __name__ == "__main__":
    main()