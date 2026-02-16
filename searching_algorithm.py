def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    sample = [3, 6, 8, 12, 14, 17, 20, 25, 28, 30]
    target = 17

    print("Original Array:", sample)

    index_linear = linear_search(sample, target)
    print(f"Linear Search: Found {target} at index", index_linear)

    index_binary = binary_search(sample, target)
    print(f"Binary Search: Found {target} at index", index_binary)
