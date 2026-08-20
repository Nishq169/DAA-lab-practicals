# =========================================================
# Sorting Algorithms in Python
# =========================================================

# =========================================================
# Bubble Sort
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n^2)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(1)
# =========================================================
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# =========================================================
# Selection Sort
# Time Complexity:
# Best Case    : O(n^2)
# Average Case : O(n^2)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(1)
# =========================================================
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# =========================================================
# Insertion Sort
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n^2)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(1)
# =========================================================
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# =========================================================
# Merge Sort
# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)
#
# Space Complexity:
# O(n)
# =========================================================
def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# =========================================================
# Quick Sort
# Time Complexity:
# Best Case    : O(n log n)
# Average Case : O(n log n)
# Worst Case   : O(n^2)
#
# Space Complexity:
# O(log n) (Recursion Stack)
# =========================================================
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


# ================== Display Function ==================
def print_array(arr):
    print("\nSorted Array:")
    print(*arr)


# ======================= Main =======================
def main():
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements:\n").split()))

    print("\nSorting Algorithms")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        bubble_sort(arr)

    elif choice == 2:
        selection_sort(arr)

    elif choice == 3:
        insertion_sort(arr)

    elif choice == 4:
        merge_sort(arr, 0, n - 1)

    elif choice == 5:
        quick_sort(arr, 0, n - 1)

    else:
        print("Invalid Choice")
        return

    print_array(arr)


if __name__ == "__main__":
    main()